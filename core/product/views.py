from django.shortcuts import render
from .forms import CreateProductForm
from .models import Category
# Create your views here.

def show_categories(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request,'all-cat.html',context)



