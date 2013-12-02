from models import PersonBio, Http_Request_for_DB
from annoying.decorators import render_to


@render_to("base.html")
def home(request):
    persons = PersonBio.objects.all()
    message = '42 Coffee Cups Test Assignment.'
    return {'message': message,
            'persons': persons,
            }


@render_to("requests.html")
def show_requests(request):
    quantity = Http_Request_for_DB.objects.all().count()
    last_10_requests = Http_Request_for_DB.objects.all()[quantity-10:quantity]
    return {'last_10_requests': last_10_requests }