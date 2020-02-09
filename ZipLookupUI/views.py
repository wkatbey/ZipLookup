from django.views.generic import TemplateView


class UIView(TemplateView):
    template_name = 'ZipLookupUI/index.html'
