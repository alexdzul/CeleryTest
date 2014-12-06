# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Subscriber


class IndexView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        try:
            email = request.POST['email']
            subs = Subscriber()
            subs.email = email
            subs.save()
            enviar_email(email)  # Enviamos un email
            message = "Gracias por Registrarte  :)"
        except ValueError:
            message = "Error en la información recibida"
        return render(request, "index.html", {'message': message})


def enviar_email(email):
    import time
    print "Inicia el envío del email..."
    repeats = range(8)
    for n_repeat in repeats:
        time.sleep(1)
        print "{0} sec.".format((n_repeat+1))
    print "email enviado a %s" % email