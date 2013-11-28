from models import PersonBio
from annoying.decorators import render_to


@render_to("base.html")
def home(request):
    persons = PersonBio.objects.all()
    message = '42 Coffee Cups Test Assignment.'
    return {'message': message,
            'persons': persons,
            }
