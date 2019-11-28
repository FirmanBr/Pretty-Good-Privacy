from django.conf.urls import url
from django.urls import path
from apps import views


app_name = 'apps'

urlpatterns=[
    url(r'^cakey/$',views.cakey,name='cakey'),
    url(r'^historykey/$',views.historykey,name='historykey'),
]
