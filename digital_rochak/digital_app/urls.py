from django.urls import path
from .views.main_views import home_view,about_view,services_view,contact_view

urlpatterns = [
    path('',home_view,name='home'),
    path('about/',about_view,name='about'),
    path('services/',services_view,name='services'),
    path('contact/',contact_view,name='contact'),
]
