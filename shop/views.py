from django.shortcuts import render
from . models import Product 
from django.core.paginator import Paginator

# Create your views here.

def index(request):
	products = Product.objects.all()

	#Search code

	item_name = request.GET.get('item_name')
	if item_name != '' and item_name is not None:
		products = products.filter(title__icontains=item_name)

	#Pagination Code
	paginator = Paginator(products, 3)
	page = request.GET.get('page')
	products = paginator.get_page(page)

	return render(request, 'index.html', {'products':products})
