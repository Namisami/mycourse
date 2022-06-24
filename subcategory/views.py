from ast import Sub
from multiprocessing import context
from django.shortcuts import render
from subcategory.models import Subcategory

def subcategory(request, subcategory_id):
    subcategory = Subcategory.objects.get(id=subcategory_id)
    context = {
        'subcategory': subcategory,
    }
    return render(request, 'subcategory/subcategory.html', context)