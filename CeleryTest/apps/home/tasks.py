# -*- coding: utf-8 -*-
__author__ = 'alex'
from celery import shared_task
from .models import Subscriber


@shared_task()
def send_email(email):
    import time
    print "Inicia el envío del email..."
    repeats = range(8)
    for n_repeat in repeats:
        time.sleep(1)
        print "{0} sec.".format((n_repeat+1))
    print "email enviado a %s" % email


@shared_task()
def send_news():
	usuarios = Subscriber.objects.all()
	for usuario in usuarios:
		print "Enviando noticias a : {0}".format(usuario.email)