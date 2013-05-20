from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from module.models import Module


class CMSPluginModule(CMSPluginBase):
    model = Module
    name = _("Module")
    render_template = "module/plugin.html"
    module = _("TheHerk")

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(CMSPluginModule)
