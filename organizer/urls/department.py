from django.conf.urls import include,url
from organizer.views import (DepartmentCreate,DepartmentList,DepartmentDetail,NewsLinkUpdate,
                             DepartmentDelete,DepartmentUpdate,NewsLinkCreate,NewsLinkDelete)



urlpatterns = [
    url(r'^$',
        DepartmentList.as_view(),
        name='organizer_department_list'),

    url(r'^create/$',
        DepartmentCreate.as_view(),
        name='organizer_department_create'),

    url(r'^(?P<dept_slug>[\w\-]+)/add_link/$',
        NewsLinkCreate.as_view(),
        name='department_newslink_create'),

    url(r'^(?P<slug>[\w\-]+)/detail/$',
        DepartmentDetail.as_view(),
        name='organizer_department_detail'),

    url(r'^(?P<slug>[\w\-]+)/delete/$',
        DepartmentDelete.as_view(),
        name='organizer_department_delete'),

    url(r'^(?P<slug>[\w\-]+)/update/$',
        DepartmentUpdate.as_view(),
        name='organizer_department_update'),

    url(r'^(?P<department_slug>[\w\-]+)/'
        r'(?P<newslink_slug>[\w\-]+)/'
        r'delete/$',
        NewsLinkDelete.as_view(),
        name='department_newslink_delete'),

    url(r'^(?P<department_slug>[\w\-]+)/'
        r'(?P<newslink_slug>[\w\-]+)/'
        r'update/$',
        NewsLinkUpdate.as_view(),
        name='department_newslink_update'),
]