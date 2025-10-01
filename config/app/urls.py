from django.urls import path
from .views import CarAPIView, BrandAPIView

urlpatterns = [
    path('cars/', CarAPIView.as_view()),
    path('cars/<int:pk>', CarAPIView.as_view()),
    path('brands/', BrandAPIView.as_view()),
]
