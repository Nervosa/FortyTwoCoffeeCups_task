from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from models import PersonBio, Http_Request_for_DB
from annoying.decorators import render_to
from FortyTwoCoffeeCups.c_forms import PersonBioForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User


@render_to("index.html")
def home(request):
    persons = PersonBio.objects.all()
    message = '42 Coffee Cups Test Assignment.'
    return {'message': message,
            'persons': persons,
            'current_user_active': request.user.is_active,
            }


@render_to("requests.html")
def show_requests(request):
    quantity = Http_Request_for_DB.objects.all().count()
    if quantity > 10:
        quantity = 9
    else:
        quantity -= 1
    last_10_requests = Http_Request_for_DB.objects.all()[0:quantity]
    return {'last_10_requests': last_10_requests}

@login_required()
@render_to("edit_page.html")
def edit_user_info(request):
    form = PersonBioForm()
    return {'form': form}


class LoginView(FormView):
    template_name = 'login_page.html'
    form_class = LoginForm
    success_url = '/edit_info/'

    def form_valid(self, form):
        entered_user = User.objects.all().filter(username=form.cleaned_data['username'])
        if entered_user:
            super(LoginView, self).form_valid(form)
            return HttpResponseRedirect('/edit_info/')
        else:
            super(LoginView, self).form_valid(form)
            return HttpResponseRedirect('/')

'''
@render_to("login_page.html")
def login(request):
    if not request.is_ajax() and request.method == 'GET':
        return {'form': LoginForm(),
                'ajax_message': 'Just entered this page',}
    if request.method == "POST":

        return {'form': LoginForm(request.POST),
                'ajax_message': 'Going to edit page',}
'''