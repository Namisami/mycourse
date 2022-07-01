from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from category.models import Category
from subcategory.models import  Subcategory
from category.forms import CategoryForm

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'category/categories.html', context)

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategories = Subcategory.objects.filter(category=category.id)
    context = {
        'category': category,
        'subcategories': subcategories,
    }
    return render(request, 'category/categories.html', context)

def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return HttpResponseRedirect(reverse('category', kwargs={'category_id': category.id}))
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'category/create.html', context)