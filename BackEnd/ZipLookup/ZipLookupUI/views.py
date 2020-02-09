from django.views.generic import TemplateView


class UIView(TemplateView):
    template_name = 'ZipLookupUI/dist/index.html'
