from django.shortcuts import render
from django.views.generic import ListView, CreateView

from  .models import  Product,  Category

# Create your views here.


class  ContegoryListView(ListView):
    model =  Category
    context_object_name = 'category_list'
    template_name = 'categories/list.html'
    paginate_by = 10


class CategotyCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'categories/add.html'
    success_url = 'category-list'