from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [

	path('list/', views.product_list, name='list'),
	path('list/<int:pk>', views.product_detail, name='detail'),
	path('list/<int:pk>/add/', views.add_quantity, name = 'add_quantity'),
	path('list/<int:pk>/delete/', views.delete_quantity, name = 'delete_quantity'),


]