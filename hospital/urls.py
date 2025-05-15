from django.urls import path
from . import views
urlpatterns=[
    path('signup/',views.sign_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
    path('logout/', views.logout_view, name='logout'),

]