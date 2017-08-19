from django.conf.urls import include,url
from organizer.views import NewsLinkCreate



urlpatterns = [

    url(r'^create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
]