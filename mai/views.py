from django.shortcuts import render
from django.views.generic import View

class baseView(View):
    def get(self, request):
        return render(request, 'base.html')
    
    def post(self, request):
        pass

class loginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        pass

class aboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
    def post(self, request):
        pass

class registerView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        pass

class informationView(View):
    def get(self, request):
        return render(request, 'information.html')
    
    def post(self, request):
        pass

class anketaView(View):
    def get(self, request):
        return render(request, 'anketa.html')
    
    def post(self, request):
        pass

