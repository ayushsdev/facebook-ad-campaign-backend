from django.urls import path
from .views import hello_world, feature_importances, ad_spend_vs_clicks

urlpatterns = [
    path('hello/', hello_world),
    path('feature_importances/', feature_importances),
    path('ad_spend_vs_clicks/', ad_spend_vs_clicks),
]
