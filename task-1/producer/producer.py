import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task-1')

while True:
	print('Enter your messege:')
	msg = input('> ')

	if msg == 'quit':
		break

	channel.basic_publish(exchange='', routing_key='task-1', body=msg)
	print("[x] Sent \"%s\"" % msg)

connection.close()
