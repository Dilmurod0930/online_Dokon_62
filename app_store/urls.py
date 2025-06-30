from  django.urls  import path
from  .views import (
    ContegoryListView,
    CategotyCreateView,
    ProductListView
)


urlpatterns = [
    path('', ContegoryListView.as_view(), name='contact_list'),
    path('add-category/', CategotyCreateView.as_view(), name='add_category'),
    path('products/', ProductListView.as_view(), name='product_list'),

]