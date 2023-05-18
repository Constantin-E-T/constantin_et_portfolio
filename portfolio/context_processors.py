# context_processors.py
from .models import Footer

def footer(request):
    footer = Footer.objects.first()
    return {'footer': footer}
