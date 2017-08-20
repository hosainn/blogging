from django.conf.urls import include,url
from .views import PostCreate,PostDetail,PostList,PostUpdate,PostDelete,PostArchiveYear,PostArchiveMonth


urlpatterns=[
    url(r'^create/$',
        PostCreate.as_view(),
        name='blog_post_create'),

    url(r'^(?P<slug>[\w\-]+)/detail/$',
        PostDetail.as_view(),
        name='blog_post_detail'),

    url(r'^$',
        PostList.as_view(),
        name='blog_post_list'),

    url(r'^(?P<slug>[\w\-]+)/update/$',
        PostUpdate.as_view(),
        name='blog_post_update'),

    url(r'^(?P<slug>[\w\-]+)/delete/$',
        PostDelete.as_view(),
        name='blog_post_delete'),

    url(r'^(?P<year>[0-9]{4})/$',
        PostArchiveYear.as_view(),
        name='blog_post_archive_year'),

    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        PostArchiveMonth.as_view(),
        name='blog_post_archive_month'),

]