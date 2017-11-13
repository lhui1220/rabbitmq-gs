#!/usr/bin/python

import pika, time

DIST_QUEUE = 'dist_queue'
DEAD_LETTER_EX = 'dead-letter-ex'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=DIST_QUEUE, durable=True)

channel.queue_bind(exchange=DEAD_LETTER_EX,routing_key=DIST_QUEUE,queue=DIST_QUEUE)

def callback(ch, method, props, body):
    now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(" [%s] Received %s" % (now,body), flush=True)

channel.basic_consume(callback, queue=DIST_QUEUE, no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)

channel.start_consuming()
