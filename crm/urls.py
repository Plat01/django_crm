from django.urls import path
from .views import *

app_name = 'crm'

urlpatterns = [
    path('product/', ProductsListAddView.as_view(), name='products_add'),
    # path('products-add/', ProductCreateAndListView.as_view(), name='products_create_view'),
    path('products-add/', ProductCreateAndListView.as_view(), name='products_combined_view'),
    path('employs/', EmploysCreateAndListView.as_view(), name='employ_list'),
    path('employs/delete/<int:pk>', EmployDeleteView.as_view(), name='employ_delete')
]