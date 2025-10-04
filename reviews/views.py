from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from negocios.models import Product
from .forms import ReviewForm
from .factory import ReviewFactory
from .proxy import ReviewProxy

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    proxy = ReviewProxy(ReviewFactory)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                proxy.create_review(
                    user=request.user,
                    product=product,
                    rating=form.cleaned_data['rating'],
                    comment=form.cleaned_data['comment']
                )
                return redirect('product_detail', product_id=product.id)
            except PermissionError as e:
                return render(request, 'reviews/error.html', {'message': str(e)})
    else:
        form = ReviewForm()

    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})

def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews})
