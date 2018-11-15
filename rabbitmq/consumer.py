""" Consumes RabbitMQ messages. """

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

#channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received message: ", body)


channel.basic_consume(callback, queue="hello", no_ack=True)
print(" [*] Waiting for messages... ")
channel.start_consuming()

