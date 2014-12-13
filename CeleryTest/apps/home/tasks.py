# -*- coding: utf-8 -*-
__author__ = 'alex'
from celery import shared_task


@shared_task()
def send_email_async(email):
    import time
    print "Inicia el envío del email..."
    repeats = range(8)
    for n_repeat in repeats:
        time.sleep(1)
        print "{0} sec.".format((n_repeat+1))
    print "email enviado a %s" % email