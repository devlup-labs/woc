from django.views.generic import TemplateView


class VueView(TemplateView):
    template_name = 'index.html'
