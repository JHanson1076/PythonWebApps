from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hero.html'


    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }

   
 
class Black_WidowView(TemplateView):
    template_name = 'hero.html'


    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'id': 'Natasha Ramanoff',
            'image': '/static/images/black_widow.jpg'
        }      