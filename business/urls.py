
from . import views
from django.urls import path

urlpatterns = [    
    path("", views.index, name="index"),    
    path("<int:customer_id>/", views.customer_detail, name="customer_detail")
]