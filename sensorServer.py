from flask import Flask
from flask_restful import Resource, Api, reqparse
import database
from datetime import datetime
import pytz

app = Flask(__name__)
api = Api(app)

class Driveway(Resource):
	def get(self):
		sql = """
			SELECT
				id, time, notes
			FROM
				driveway_sensor
		"""
		results = database.fetchAll(sql, {})
		return {'data': results}, 200

	def post(self):
		time_zone = pytz.timezone('America/Denver')
		time = datetime.now(time_zone)
		new = database.fetchOne("""
			INSERT INTO
				driveway_sensor (
					time
				) VALUES (
					'{time}'
				)
			RETURNING id, time, notes;
			""", {'time': time})
		if new:
			data = {'id': new[0], 'time': new[1], 'notes':new[2]}
		else:
			data = new
		return {'data': data}, 200

api.add_resource(Driveway, '/driveway')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, threaded=True)
