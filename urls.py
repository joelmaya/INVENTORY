from django.urls import path
from .views import order
from.views import OrderCreateView
from .import views

app_name = 'stock'
urlpatterns = [
	path('order/',views.purchase, name='order'),
	path('order/update/<int:pk>', views.Update, name = 'update_item'),
	path('order/delete/<int:pk>', views.delete_view, name='delete'),
	path('order/new/',OrderCreateView.as_view(),name = 'order-create'),
	#path('dashboard/', views.item_list, name='item_list'),
	path('my_item/', views.Issues_view, name='order_item'),
	path('issues/<int:pk>', views.Issues_view, name='issue_item'),
]


