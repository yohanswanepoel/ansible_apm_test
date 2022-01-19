from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import platform

class MainView(TemplateView):
    template_name='pages/home.html'
    def get(self, request):
        context = {
            "machine": platform.machine(),
            "node": platform.node(),
            "platform": platform.platform(aliased=True),
            "release": platform.release(),
            "system": platform.system()

        }
        return render(request, self.template_name,context)