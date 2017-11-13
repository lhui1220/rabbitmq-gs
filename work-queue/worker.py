import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create and persistent the queue
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
	print('[x] Recv %r' % body)
	time.sleep(body.count(b'.'))
	print('[x] Done')
	
channel.basic_consume(callback, queue='task_queue',no_ack=True)

# wait for messages
channel.start_consuming()

