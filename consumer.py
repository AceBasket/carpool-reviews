#i want this to recieve information from the producer, which is information from a database with reviews
#using pika
import json
import pika
import django
from sys import path
from os import environ

path.append('/Users/manol/Desktop/reviews/reviews/settings.py') #Your path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviews.settings') 
django.setup()

from reviews_app.models import Review

params = pika.URLParameters('amqps://qwsrvkqg:4s2YX68Qo_XGjW5zIl-2DHYXEAL5oYQR@hog.rmq5.cloudamqp.com/qwsrvkqg')
connection = pika.BlockingConnection(params)

channel = connection.channel()  # Create a channel object

channel.queue_declare(queue='reviews')

def callback(ch, method, properties, body):
    print('Received in reviews')
    print(body)
    data = body
    print(data)
    if Review.objects.filter(trip=data).exists():
        print('trip is in the database')
        if properties.content_type == 'trip_deleted':
            try: 
                Trip = Review.objects.filter(trip=data)
                Trip.delete()
            except:
                print('Trip '+str(data)+' does not exist')
            if Review.objects.filter(trip=data).exists()==False:
                print('Reviews from trip '+str(data)+' deleted')
            if Review.objects.filter(trip=data).exists():
                print('Reviews not deleted')
    elif Review.objects.filter(trip=data).exists()==False:
        print('trip is not in the database')



channel.basic_consume(queue='reviews', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

#try:
channel.start_consuming()
#except Exception as e:
#    print(f"An error occurred: {e}")

channel.close()
