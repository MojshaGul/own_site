from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product
from .forms import createproduct
from django.contrib.auth.mixins import *

class baseView(LoginRequiredMixin ,View):
    login_url = 'register'
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page = request.GET.get("page")
        page_product = paginator.get_page(page)

        return render(request, 'products.html', context={"page_product":page_product})
    
    def post(self, request):
        pass


class aboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
    def post(self, request):
        pass

class anketaView(LoginRequiredMixin ,View):
    def get(self, request):
        form = createproduct()
        return render(request, 'anketa.html', context={"form": form})
    
    def post(self, request):
        form = createproduct(data=request.POST)
        if form.is_valid():
            a = (form.save())
            print(a)
            return redirect("cbv_page")

class iteminfo(LoginRequiredMixin ,View):
    def get(self, request, id):
        item_data = Product.objects.filter(id = id).last()
        return render(request, 'iteminfo.html', context={"item_data": item_data})
    
    def post(self, request):
        pass

