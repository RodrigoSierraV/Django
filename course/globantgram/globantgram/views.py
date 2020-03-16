from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %d, %Y - %H:%M')
    return HttpResponse('Hello, world now {}'.format(now))

def sorted_integers(request):
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    numbers = [int(i) for i in numbers]
    numbers = sorted(numbers)
    data = {
        'status': 'OK',
        'numbers': numbers,
        'message': 'Integers Successfully sorted.'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed HERE'.format(name)
    else:
        message = 'Hello, {}, Welcome to Globantgram'.format(name)
    return HttpResponse(message)
