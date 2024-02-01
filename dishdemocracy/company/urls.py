from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='index'),
    path('register', views.register, name='register_owner'),
    path('registerEmployee/', views.registerEmployee, name='register_employee'),
    path('employee_page', views.employee_page, name='employee_page'),
    path('restaurant_page', views.restaurant_page, name='restaurant_page'),
    path('winner/',views.winner,name='winner')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)