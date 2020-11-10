from django.urls import path
from . import views

urlpatterns = [
    path("", views.item_page, name = "item"),
    path("<int:pk>", views.AutoDatail.as_view(), name = "auto")
]