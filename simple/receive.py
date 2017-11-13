#!/usr/bin/python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create the queue named 'simple'
channel.queue_declare(queue='simple')

def callback(ch, method, properties, body):
    print(" [x] Received %s" % body, flush=True)

channel.basic_consume(callback, queue='simple', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)

channel.start_consuming()
