from django.conf.urls import include,url
from .views import PostCreate,PostDetail,PostList,PostUpdate,PostDelete


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

]