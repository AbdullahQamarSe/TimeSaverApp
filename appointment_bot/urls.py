from django.urls import path,include
from appointment_bot import views
urlpatterns = [
    path("", views.base, name="base"),
    path("scrap", views.scrap, name="scrap"),
]
