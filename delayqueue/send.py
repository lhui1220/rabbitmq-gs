import pika, time, random

DELAY_QUEUE = 'delay_queue'
DIST_QUEUE = 'dist_queue'
DEAD_LETTER_EX = 'dead-letter-ex'

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

# create exchange for dead-letter message routing
exchange = channel.exchange_declare(exchange=DEAD_LETTER_EX, exchange_type='direct')

# create delay queue and setup how to handle dead-letter message
args = {'x-dead-letter-exchange':DEAD_LETTER_EX,'x-dead-letter-routing-key':DIST_QUEUE}
queue = channel.queue_declare(queue=DELAY_QUEUE,durable=True,arguments=args)

# publish message
msg = str(time.time())
expires = str(random.randint(10,20)*1000)
props = pika.spec.BasicProperties(expiration=expires)

channel.basic_publish(exchange='',routing_key=DELAY_QUEUE,body=msg,properties=props)

now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print('[%s] send %s,delay:%sms' % (now,msg,expires))
