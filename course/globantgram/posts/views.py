from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Rodri',
        'timestamp': datetime.now().strftime('%b %d, %Y - %H:%M'),
        'picture': 'https://i.picsum.photos/id/903/200/200.jpg'
    }
]

def list_posts(request):
    return render(request, 'feed.html', {'posts':posts})

#    def list_posts(request):
#        content = []
#        for post in posts:
#            content.append("""
#                <p><strong>{name}</strong></p>
#                <p><small>{user} - <i>{timestamp}</i></small></p>
#                <figure><img src={picture}></figure>
#            """.format(**post))
#        return HttpResponse('<br>'.join(content))

