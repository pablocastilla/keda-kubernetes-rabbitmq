from time import sleep
import pika

print("Starting consumer.py")


def callback(ch, method, properties, body):
    sleep(0.1)
    print(f"Received {body}")

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('172.17.0.2'))
channel = connection.channel()
channel.basic_qos(prefetch_count=1)

# Declare queue
channel.queue_declare(queue='task_queue')

# Register callback function
channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

# Start consuming
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
