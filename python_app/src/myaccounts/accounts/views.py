from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

@method_decorator(login_required(login_url='home'), name='dispatch')
class AccountsMainView(TemplateView):
    template_name='listaccounts.html'
    def get(self, request):
        context = {}
        return render(request, self.template_name,context)
