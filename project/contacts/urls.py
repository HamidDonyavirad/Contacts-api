from django.urls import path
from . import views


urlpatterns = [
    path('cantants/',views.ContactstUserView.as_view(),name='cantact-list'),
]