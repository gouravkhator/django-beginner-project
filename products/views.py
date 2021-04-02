from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductCreateForm, RawProductForm

# Create your views here.
# Form creation using in built Form class
# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()

#     context = {
#         'form': my_form
#     }
#     return render(request, 'products/product_create.html', context)

# Form creation by our own but handling form submit here
# def product_create_view(request):
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
        
#     context = {}
#     return render(request, 'products/product_create.html', context)


# Form creation using in built ModelForm class
def product_create_view(request):
    initial_data = {
        'title': 'This is my initial title',
        'description': 'Hello initialiser',
        'price': 1.52
    }
    form = ProductCreateForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

def product_list_view(request):
    object_list = Product.objects.all()
    context = {
        'object_list': object_list,
    }
    return render(request, 'products/product_list.html', context=context)

# editing only product with passed id
def product_edit_view(request, id):
    obj = Product.objects.get(id=id)

    form = ProductCreateForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        form = ProductCreateForm(instance=obj)

    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

# product details for that passed id
def product_detail_view(request, id):
    obj= get_object_or_404(Product, id=id)

    context = {
        'object':obj,
    }
        
    return render(request, 'products/product_detail.html', context)

# product deletion
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
        
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context=context)