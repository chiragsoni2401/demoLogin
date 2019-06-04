from . import views
from django.urls import path
#app name
app_name = 'socialLogin'

urlpatterns = [
     path('',views.index, name='index_page'),
     path('logged-in/',views.success,name='success_page')
]