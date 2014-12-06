# -*- coding: utf-8 -*-
from django.db import models


class Subscriber(models.Model):
    """
    Modelo que almacena información de los suscriptores
    """
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email