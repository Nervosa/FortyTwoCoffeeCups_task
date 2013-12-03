from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FortyTwoCoffeeCups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^requests/', 'FortyTwoCoffeeCups.views.show_requests', name='requests'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^FortyTwoCoffeeCups/media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )