from  django.urls  import path
from  .views import ContegoryListView, CategotyCreateView


urlpatterns = [
    path('', ContegoryListView.as_view(), name='contact_list'),
    path('add-category/', CategotyCreateView.as_view(), name='add_category'),

]