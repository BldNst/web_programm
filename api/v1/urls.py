from django.urls import path, include


urlpatterns = [
    path('client/', include('api.v1.client.urls')),
]