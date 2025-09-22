from django.shortcuts import render
from django.views.generic import View

class BaseView(View):
    def get(self, request):
        return render(request, 'main.html')
    
    def post(self, request):
        pass
    
def base_view(request):
    return render(request, 'main.html')
