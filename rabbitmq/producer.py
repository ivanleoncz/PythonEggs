""" Produces messages on RabbitMQ. """

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='hello')

msg = '{"Name":"ivanleoncz", "Country":"Brazil", "Role":"Software Developer"}'
msg1 = '{"Name":"Linus Torvalds", "Country":"Finland", "Role":"Kernel Dictator"}'


channel.basic_publish(exchange='', routing_key='hello', body=msg1)
print(" [x] Sent 'Hello World!' ")

connection.close()
