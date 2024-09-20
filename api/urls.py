from django.urls import path
from .views import hello_world, feature_importances

urlpatterns = [
    path('hello/', hello_world),
    path('feature_importances/', feature_importances),
]
