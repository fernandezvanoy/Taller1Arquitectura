from django.shortcuts import render, redirect, get_object_or_404
from .forms import EntrepreneurForm, ProductForm
from .models import Entrepreneur, Product
from django.http import HttpResponse
from django.conf import settings
 # se importa storage.py
from django.utils.module_loading import import_string


# StorageClass = import_string(settings.IMAGE_STORAGE_CLASS)
# storage = StorageClass()

from .factory import StorageFactory
storage = StorageFactory.create_storage()

# Create your views here.
def create_entrepreneur(request):
    if request.method == "POST":
        form = EntrepreneurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EntrepreneurForm()
    return render(request, 'create_entrepreneur.html', {'form': form})

def delete_entrepreneur(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    if request.method == 'POST':
        entrepreneur.delete()
        return redirect('entrepreneur_list')
    return render(request, 'confirm_delete.html', {'entrepreneur': entrepreneur})

def success(request):
    return render(request, 'success.html')

def entrepreneur_list(request):
    entrepreneurs = Entrepreneur.objects.prefetch_related('products')  
    return render(request, 'entrepreneur_list.html', {'entrepreneurs': entrepreneurs})

def add_product(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse("Formulario inválido", status=400)

        # ---- Mapeo y validación de categoría ----
        category_mapping = {
            "1": "Dulcesito",
            "2": "Saladito",
            "3": "Accesorios",
            "4": "Bebidas",
            "5": "Servicios",
            "6": "Candies",
        }
        category_id = request.POST.get('category')
        category_name = category_mapping.get(category_id)
        if not category_name:
            return HttpResponse("Categoría inválida.", status=400)

        try:
            # Subir la imagen con el storage configurado
            image_file = form.cleaned_data['image_file']
            secure_url = storage.upload(image_file, folder="products/")

            # Crear producto
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                category=category_name,
                entrepreneur=entrepreneur,
                image_url=secure_url
            )
            return redirect('product_success', pk=entrepreneur.pk)

        except Exception as e:
            return HttpResponse(f"Error al subir imagen: {e}", status=500)

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {
        'entrepreneur': entrepreneur,
        'form': form
    })

def view_products(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    products = Product.objects.filter(entrepreneur=entrepreneur)
    return render(request, 'view_products.html', {'entrepreneur': entrepreneur, 'products': products})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    entrepreneur = product.entrepreneur

    if request.method == 'POST':
        name        = request.POST.get('name')
        description = request.POST.get('description')
        price       = request.POST.get('price')
        image_file  = request.FILES.get('image_file')
        category_id = request.POST.get('category')

        category_mapping = {
            "1": "Dulcesito",
            "2": "Saladito",
            "3": "Accesorios",
            "4": "Bebidas",
            "5": "Servicios",
            "6": "Candies",
        }
        category_name = category_mapping.get(category_id)

        if not all([name, description, price, category_name]):
            return HttpResponse("Error: Todos los campos excepto imagen son obligatorios.", status=400)

        try:
            product.name        = name
            product.description = description
            product.price       = price
            product.category    = category_name

            if image_file:
                product.image_url = storage.upload(image_file, folder="products/")

            product.save()
            return redirect('view_products', pk=entrepreneur.pk)

        except Exception as e:
            return HttpResponse(f"Error al actualizar el producto: {e}", status=500)

    reverse_mapping = {v: k for k, v in {
        "1": "Dulcesito",
        "2": "Saladito",
        "3": "Accesorios",
        "4": "Bebidas",
        "5": "Servicios",
        "6": "Candies",
    }.items()}
    current_cat_value = reverse_mapping.get(product.category, "")

    return render(request, 'edit_product.html', {
        'product': product,
        'entrepreneur': entrepreneur,
        'current_category': current_cat_value,
    })

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('view_products', pk=product.entrepreneur.pk)
    return render(request, 'confirm_delete_product.html', {'product': product})

def product_success(request, pk):
    entrepreneur = get_object_or_404(Entrepreneur, pk=pk)
    return render(request, 'product_success.html', {'entrepreneur': entrepreneur})

def catalogo(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    categorized_products = {category: Product.objects.filter(category=category) for category in categories}
    return render(request, 'catalogo.html', {'categorized_products': categorized_products})
