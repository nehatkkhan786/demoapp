from django.shortcuts import render

# Create your views here.
def add_product(request,id):
	if request.method == 'POST':
		quantity = request.POST.get('quantity')
		Product.quantity += quantity

		

