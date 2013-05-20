from cms.models.pluginmodel import CMSPlugin
from django.db import models


class Module(CMSPlugin):
    name = models.CharField(max_length=24)
    body = models.TextField(help_text='Must be html. Use text plugin if this is a problem.')
