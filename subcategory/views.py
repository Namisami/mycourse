from ast import Sub
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from category.models import Category
from subcategory.models import Subcategory
from subcategory.forms import SubcategoryForm

def subcategory(request, subcategory_id, category_id):
    subcategory = Subcategory.objects.get(id=subcategory_id)
    context = {
        'subcategory': subcategory,
    }
    return render(request, 'subcategory/subcategory.html', context)

def create(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            subcategory = Subcategory.objects.create(title=request.POST.get("title"),
                                    description = request.POST.get("description"),
                                    category = category)
            return HttpResponseRedirect(reverse('subcategory', kwargs={'subcategory_id': subcategory.id, 'category_id': category_id}))
    else:
        form = SubcategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'subcategory/create.html', context)