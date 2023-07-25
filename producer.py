import pika

print(f"Starting producer.py")

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='task_queue')

# Send messages
for i in range(10000000):
    channel.basic_publish(exchange='', routing_key='task_queue', body='Hello World!')

print("Messages sent")

# Close connection
connection.close()
