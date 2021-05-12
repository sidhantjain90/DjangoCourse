# Create a simple view for homepage
# and then link it to urls!

from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

#Add test and thanks page
class TestPage(TemplateView):
    template_name='test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'    
