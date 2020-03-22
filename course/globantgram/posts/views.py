from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import flightradar24

from . forms import AirlineForm

def list_posts(request):
    form = AirlineForm()
    return render(request, 'feed.html', {'form': form })

def book_flights(request):
    fr = flightradar24.Api()
    print(dir(fr))
    flights = fr.get_flights(request.POST['choose_airline'])
    print(dir(flights))
    return render(request, 'flights.html', {'flights': flights.items()})
#    def list_posts(request):
#        content = []
#        for post in posts:
#            content.append("""
#                <p><strong>{name}</strong></p>
#                <p><small>{user} - <i>{timestamp}</i></small></p>
#                <figure><img src={picture}></figure>
#            """.format(**post))
#        return HttpResponse('<br>'.join(content))

