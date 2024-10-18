from django.shortcuts import render, redirect
from .categoryForm import CategoryForm  

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')  
    else:
        form = CategoryForm()
    return render(request, 'category.html', {'form': form})


