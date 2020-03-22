from django.http import HttpResponse
from datetime import datetime
import json

def hello(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Hello World, server time {}'.format(now))

def sorted_num(request):
    print(request)
    numbers = request.GET['numbers']
    numbers = numbers.split(',')
    numbers = [int(num) for num in numbers]
    numbers = sorted(numbers)
    dic = {
        'status': 'OK',
        'numbers': numbers
    }
    js = json.dumps(dic, indent=4)
    return HttpResponse(js, content_type='application/json')

def hi(request, name, age):
    return HttpResponse(name+str(age))
