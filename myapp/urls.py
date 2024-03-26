from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
     path('submit_contact_form/', views.submit_contact_form, name='submit_contact_form'),

]