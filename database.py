import psycopg2
import psycopg2.extras
from configparser import ConfigParser
from datetime import date, datetime

def json_serial(obj):
	if isinstance(obj, (datetime, date)):
		return obj.isoformat()
	else:
		return obj

def config(filename='database.ini', section='postgresql'):
	parser = ConfigParser()
	parser.read(filename)

	db = {}
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			db[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))
	return db


def fetchOne(sql, params):
	try:
		db_config_params = config()
		conn = psycopg2.connect(**db_config_params)
		with conn:
			cursor = conn.cursor()
			cursor.execute(sql.format(**params))
			results = cursor.fetchone()
			to_return = [json_serial(res) for res in results]
			return(to_return)


	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')

def fetchAll(sql, params):
	try:
		db_config_params = config()
		conn = psycopg2.connect(**db_config_params)
		with conn:
			cursor = conn.cursor()
			cursor.execute(sql.format(**params))
			results = cursor.fetchall()
			to_return = [[json_serial(item) for item in line] for line in results]
			return(to_return)

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')

def execute(sql, params):
	try:
		db_config_params = config()
		conn = psycopg2.connect(**db_config_params)
		with conn:
			cursor = conn.cursor()
			cursor.execute(sql.format(**params))


	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')

