from models import PersonBio, Http_Request_for_DB
from annoying.decorators import render_to


@render_to("index.html")
def home(request):
    persons = PersonBio.objects.all()
    message = '42 Coffee Cups Test Assignment.'
    return {'message': message,
            'persons': persons,
            }


@render_to("requests.html")
def show_requests(request):
    quantity = Http_Request_for_DB.objects.all().count()
    if quantity > 10:
        quantity = 10
    else:
        quantity += 1
    last_10_requests = Http_Request_for_DB.objects.all()[0:quantity]
    return {'last_10_requests': last_10_requests }