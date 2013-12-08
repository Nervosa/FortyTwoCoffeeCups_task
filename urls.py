from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from FortyTwoCoffeeCups.views import LoginView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'FortyTwoCoffeeCups.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', 'FortyTwoCoffeeCups.views.show_requests', name='requests'),
    url(r'^edit_info/', 'FortyTwoCoffeeCups.views.edit_user_info', name='edit'),
    url(r'^login/', LoginView.as_view(), name='login')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )