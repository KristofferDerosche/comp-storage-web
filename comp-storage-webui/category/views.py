from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Category

# Create your views here.

def new(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        parents_ids = request.POST.getlist('parents')
        category = Category(name=name, description=description)
        category.save()
        if parents_ids:
            parents = Category.objects.filter(id__in=parents_ids)
            category.parents.set(parents)
        return redirect('category_details', category_id=category.id)
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'category/new.html', {'categories': categories})
    

def details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.exclude(pk=category_id)
    return render(request, 'category/details.html', {'category': category, 'categories': categories})

def list(request):
    categories = Category.objects.all()
    return render(request, 'category/list.html', {'categories': categories})

def update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        parents_ids = request.POST.getlist('parents')
        category.save()
        if parents_ids:
            parents = Category.objects.filter(id__in=parents_ids)
            category.parents.set(parents)
        return redirect('category_details', category_id=category.id)
    categories = Category.objects.exclude(pk=category_id)
    return render(request, 'category/details.html', {'category': category, 'categories': categories})

def delete(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('category_list')