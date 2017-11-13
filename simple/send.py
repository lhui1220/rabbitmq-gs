#!usr/bin/python

import pika

'''
simple pub-sub use RabbitMQ

'''

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel  = connection.channel()

channel.queue_declare(queue='simple')

message = 'Hello RabbitMQ'
channel.basic_publish(exchange='', routing_key='simple', body=message)

print("[x] send '%s'"%message)

connection.close()