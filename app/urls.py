from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('appointment', views.appointment, name='appointment'),
    path('add_record', views.add_record, name='add_record'),
    path('record_list/', views.record_list, name='record_list'),
    path('contact', views.contact_Us, name='contact'),
    path('update_record/<int:pk>/', views.update_record, name='update_record'),
    path('record_details/<int:pk>', views.record_details, name='record_details'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
    path('search_record', views.search_record, name='search_record'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
