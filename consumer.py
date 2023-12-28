# I want this to recieve information from the producer, which is information from a database with reviews
# using pika
import json
import pika
import django
from sys import path
from os import environ

# Your path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviews.settings')
django.setup()

from reviews_app.models import Review  # noqa

params = pika.URLParameters(
    'amqps://qwsrvkqg:4s2YX68Qo_XGjW5zIl-2DHYXEAL5oYQR@hog.rmq5.cloudamqp.com/qwsrvkqg')
connection = pika.BlockingConnection(params)

channel = connection.channel()  # Create a channel object

channel.queue_declare(queue='reviews')


def callback(ch, method, properties, body):
    if properties.content_type == 'trip_deleted':
        try:
            Review.objects.filter(trip=body).delete()
            print(f"Deleted reviews for trip {body}")
        except Exception as exc:
            print(f"An error occurred during review deletion: {exc}")
    else:
        print('Unknown content type')


channel.basic_consume(
    queue='reviews', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

try:
    channel.start_consuming()
except Exception as e:
    print(f"An error occurred: {e}")

channel.close()
