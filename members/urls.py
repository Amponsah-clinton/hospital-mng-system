from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('opd/', views.opd, name='opd'),
    path('theater/', views.Theater, name='theater'),
    path('maternity/', views.Maternity, name='maternity'),
    path('MFP/', views.MFP, name='MFP'),
    path('Emergency /', views.Emergency , name='Emergency'),
    path('Records/', views.Records, name='Records'),
    path('Pharmacy/', views.Pharmacy, name='Pharmacy'),
    path('Laboratory/', views.Laboratory, name='Laboratory'),
    path('AC/', views.AC, name='AC'),
    path('add_vitals', views.add_vitals, name='add_vitals'),
    path('patients_history', views.patients_history, name='patients_history'),
    path('add_lab_results', views.add_lab_results, name='add_lab_results'),
    path('AC_vitals_records', views.AC_vitals_records, name='AC_vitals_records'),
    path('general_notes', views.general_notes, name='general_notes'),
    path('theater_records', views.theater_records, name='theater_records'),
    path('maternity_notes_records', views.maternity_notes_records, name='maternity_notes_records'),
    path('emergency_notes_records', views.emergency_notes_records, name='emergency_notes_records'),
    path('mfp_records', views.mfp_records, name='mfp_records'),
    path('department_list',views.department_list, name='department_list'),
    
]