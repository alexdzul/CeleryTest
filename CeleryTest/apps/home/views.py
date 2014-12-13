# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Subscriber
from .tasks import send_email_async

class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST['email']
            subs = Subscriber()
            subs.email = email
            subs.save()
            send_email_async.delay(email)  # Enviamos un email
            message = "Gracias por Registrarte  :)"
        except ValueError:
            message = "Error en la información recibida"
        return render(request, "index.html", {'message': message})