from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from category.models import Category
from subcategory.models import  Subcategory
from category.forms import CategoryForm
from authentication.models import User


@login_required
def categories(request):
    user = User.objects.get(id=request.user.id)
    categories = Category.objects.filter(owner=user)
    context = {
        'categories': categories,
    }
    return render(request, 'category/categories.html', context)

@login_required
def category(request, category_id):
    user = User.objects.get(id=request.user.id)
    category = get_object_or_404(Category, id=category_id, owner=user)
    subcategories = Subcategory.objects.filter(category=category.id)
    context = {
        'category': category,
        'subcategories': subcategories,
    }
    return render(request, 'category/categories.html', context)

@login_required
def create(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = user
            category.save()
            return HttpResponseRedirect(reverse('category', kwargs={'category_id': category.id}))
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'category/create.html', context)

@login_required
def delete(request, category_id):
    user = User.objects.get(id=request.user.id)
    category = get_object_or_404(Category, id=category_id, owner=user)
    category.delete()
    return HttpResponseRedirect(reverse('categories'))

@login_required
def edit(request, category_id):
    user = User.objects.get(id=request.user.id)
    category = get_object_or_404(Category, id=category_id, owner=user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = user
            category.save()
            return HttpResponseRedirect(reverse('category', kwargs={'category_id': category.id}))
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
    }
    return render(request, 'category/edit.html', context)