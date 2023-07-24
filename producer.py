import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='task_queue')

# Send message
for i in range(10000000):
    channel.basic_publish(exchange='', routing_key='task_queue', body='Hello World!')
print("Sent 'Hello World!'")

# Close connection
connection.close()
