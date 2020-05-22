from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

urlpatterns = [
    path('webapp/', views.employeeList.as_view()),
    path('webapp/<int:pk>/', views.employeeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)