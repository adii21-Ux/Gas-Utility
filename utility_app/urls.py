from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/customer/', views.customer_registration,
         name='customer_registration'),
    path('register/representative/', views.representative_registration,
         name='representative_registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),

    # Service
    path('create/', views.create_service_request, name='create_service_request'),
    path('service-requests/', views.user_service_requests,
         name='user_service_requests'),
    path('service-requests/<int:request_id>/',
         views.service_request_details, name='service_request_details'),

    # Representative
    path('all-service-requests/',
         views.all_service_requests, name='representative_dashboard'),
    path('update_service_request/<int:request_id>/',
         views.update_service_request, name='update_service_request'),
    path('update_resolved_at/<int:request_id>/',
         views.update_resolved_at, name='update_resolved_at'),
]
