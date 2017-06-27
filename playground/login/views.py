from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login


class LoginView(TemplateView):
    template_name = 'login/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'login/login.html', {
                'error_message': 'Successful login!'
            })
        else:
            return render(request, 'login/login.html', {
                'error_message': 'Failed login'
            })

    def get_context_data(self, **kwargs):
        context = {}
        return context
