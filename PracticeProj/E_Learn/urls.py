from django.urls import path
from .views import (  
    UserListCreateView, UserRetrieveUpdateDestroyView,
    CourseListCreateView, CourseRetrieveUpdateDestroyView,
    EnrollmentListCreateView, EnrollmentRetrieveUpdateDestroyView,
    EnrollmentItemListCreateView, EnrollmentItemRetrieveUpdateDestroyView
)
 
urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-retrieve-update-destroy'),
    path('enrollment-items/', EnrollmentItemListCreateView.as_view(), name='enrollment-item-list-create'),
    path('enrollment-items/<int:pk>/', EnrollmentItemRetrieveUpdateDestroyView.as_view(), name='enrollment-item-retrieve-update-destroy'),
]