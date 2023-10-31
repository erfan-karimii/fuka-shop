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



def create_product(request,cat):
    form = CreateProductForm()
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            print('pass')
        else:
            print(form.error)
    context = {
        'form' : form
    }
    return render(request,'create-product.html',context)