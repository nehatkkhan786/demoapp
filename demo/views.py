from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Product
from django.urls import reverse
# Create your views here.
def product_list(request):
	products = Product.objects.all()
	return render(request, 'product_list.html', {'products':products})

def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	return render(request, 'product_detail.html', {'product':product})


def add_quantity(request,pk):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=pk)
		quantity = request.POST.get('quantity')
		int_quantity = int(quantity)
		product.quantity += int_quantity
		product.save()
		return redirect('/demo/list/' + str(product.id))

def delete_quantity(request, pk):
	if request.method == 'POST':
		product = get_object_or_404(Product,pk=pk)
		quantity = request.POST.get('quantity')
		int_quantity = int(quantity)
		product.quantity -=int_quantity
		product.save()
		return redirect('/demo/list/' + str(product.id))