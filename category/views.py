from django.shortcuts import render
from category.models import Category
from subcategory.models import  Subcategory

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