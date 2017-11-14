import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create and persistent the queue
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, props, body):
	print('[x] Recv %r,delivery_tag=%s' % (body,method.delivery_tag))
	time.sleep(20)
	print('[x] Done')
	ch.basic_ack(delivery_tag=method.delivery_tag)
	
channel.basic_consume(callback, queue='task_queue',no_ack=False)

# wait for messages
channel.start_consuming()

