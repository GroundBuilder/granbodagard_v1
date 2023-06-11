from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shoppingbag, name='view_shoppingbag'),
    path('add/<item_id>/', views.add_to_shoppingbag, name='add_to_shoppingbag'),
]