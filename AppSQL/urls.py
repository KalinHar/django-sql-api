from django.conf.urls import url
from AppSQL import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^clients$',views.clientsApi),
    url(r'^client$',views.clientApi),
    url(r'^client/([0-9]+)$',views.clientApi),

    url(r'^note$',views.noteApi),
    url(r'^note/([0-9]+)$',views.noteApi),
]