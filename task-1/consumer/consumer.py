import pika
import psycopg2

db = psycopg2.connect("dbname=postgres user=postgres password=postgres host=postgres port=5432")
cursor = db.cursor()

cursor.execute("DROP TABLE storage")
cursor.execute("CREATE TABLE storage (msg TEXT)")
db.commit()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task-1')

def callback(ch, method, properties, body):
	cur = db.cursor()
	print("[x] Received {}".format(body.decode()))
	cur.execute("INSERT INTO storage(msg) VALUES('{}')".format(body.decode()))
	db.commit()

channel.basic_consume(callback, queue='task-1', no_ack=True)
channel.start_consuming()


