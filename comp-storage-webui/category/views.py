from django.shortcuts import render

# Create your views here.

def new_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        print(name, description)

    return render(request, 'category/new.html')