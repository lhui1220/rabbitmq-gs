import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#persistent the queue
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello RabbitMQ'

#mark delivery_mode=2 to persitent message 
channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasiceProperties(delivery_mode=2))
