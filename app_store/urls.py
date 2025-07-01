from  django.urls  import path
from  .views import (
    ContegoryListView,
    CategotyCreateView,
    ProductListView,
    product_create,
    base
)


urlpatterns = [
    path('', base,  name='base'),
    path('category_list', ContegoryListView.as_view(), name='category_list'),
    path('add_category/', CategotyCreateView.as_view(), name='add_category'),
    path('products_lst/', ProductListView.as_view(), name='product_lst'),
    path('add_prpduct/', product_create, name='add_product'),

]