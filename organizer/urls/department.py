from django.conf.urls import include,url
from organizer.views import DepartmentCreate,DepartmentList,DepartmentDetail,DepartmentDelete,DepartmentUpdate



urlpatterns = [
    url(r'^$',
        DepartmentList.as_view(),
        name='organizer_department_list'),

    url(r'^create/$',
        DepartmentCreate.as_view(),
        name='organizer_department_create'),

    url(r'^(?P<slug>[\w\-]+)/detail/$',
        DepartmentDetail.as_view(),
        name='organizer_department_detail'),

    url(r'^(?P<slug>[\w\-]+)/delete/$',
        DepartmentDelete.as_view(),
        name='organizer_department_delete'),

    url(r'^(?P<slug>[\w\-]+)/update/$',
        DepartmentUpdate.as_view(),
        name='organizer_department_update'),
]