from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import ProductForm
from .models import  Product,  Category

# Create your views here.


def  base(request):
    return render(request, 'base.html')

class  ContegoryListView(ListView):
    model =  Category
    context_object_name = 'category_list'
    template_name = 'categories/list.html'
    paginate_by = 10


class CategotyCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'categories/add.html'
    success_url = reverse_lazy('category_list')




"""Praduct  Start"""

class  ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/product_lst.html'
    paginate_by = 10


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=None)
        if form.is_valid():
            product = form.save(commit=False)
            product.full_clean()
            product.save()
            return redirect('product_lst')
        return render(request, 'products/product_add.html', {'form': form})
    form = ProductForm()
    return render(request, 'products/product_add.html', {'form': form})
