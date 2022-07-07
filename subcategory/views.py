from ast import Sub
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from authentication.models import User
from category.models import Category
from subcategory.models import Subcategory
from subcategory.forms import SubcategoryForm


@login_required
def subcategory(request, subcategory_id, category_id):
    user = User.objects.get(id=request.user.id)
    subcategory = get_object_or_404(Subcategory, id=subcategory_id, owner=user)
    context = {
        'subcategory': subcategory,
    }
    return render(request, 'subcategory/subcategory.html', context)

@login_required
def create(request, category_id):
    user = User.objects.get(id=request.user.id)
    category = get_object_or_404(Category, id=category_id, owner=user)
    if request.method == 'POST' and category:
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            subcategory = Subcategory.objects.create(title=request.POST.get("title"),
                                    description = request.POST.get("description"),
                                    category = category,
                                    owner=user)
            return HttpResponseRedirect(reverse('subcategory', kwargs={'subcategory_id': subcategory.id, 'category_id': category_id}))
    else:
        form = SubcategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'subcategory/create.html', context)

@login_required
def delete(request, subcategory_id, category_id):
    user = User.objects.get(id=request.user.id)
    subcategory = get_object_or_404(Subcategory, id=subcategory_id, owner=user)
    subcategory.delete()
    return HttpResponseRedirect(reverse('category', kwargs={'category_id': category_id}))

@login_required
def edit(request, category_id, subcategory_id):
    user = User.objects.get(id=request.user.id)
    category = get_object_or_404(Category, id=category_id, owner=user)
    subcategory = get_object_or_404(Subcategory, id=subcategory_id, owner=user)
    if request.method == 'POST' and category:
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subcategory', kwargs={'subcategory_id': subcategory.id, 'category_id': category_id}))
    else:
        form = SubcategoryForm(instance=subcategory)
    context = {
        'form': form,
    }
    return render(request, 'subcategory/edit.html', context)