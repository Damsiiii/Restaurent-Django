from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('booking/', views.booking_view, name='booking'),
    path('contact/', views.contact_view, name='contact'),
    path('qr/', views.qr_code_view, name='qr'),
]

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('booking/', views.booking_view, name='booking'),
    path('booking/<int:res_id>/', views.booking_detail_view, name='booking_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('qr/', views.qr_code_view, name='qr'),
]