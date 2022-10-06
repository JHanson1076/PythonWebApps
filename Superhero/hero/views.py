from django.shortcuts import render

# Create your views here.
class PhotoView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        p = kwargs['name']
        p = f'/static/images/{p}'
        return dict(photo=p)
    
class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }
        
class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'id': 'Tony Stark',
            'image': '/static/images/iron_man.jpg'
        }
class BlackWidow(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'id': 'Natasha Ramonav',
            'image': '/static/images/black_widow.jpg'
        }
class GhostRider(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Ghost Rider',
            'id': 'Johnny Blaze',
            'image': '/static/images/Ghost_Rider.jpg'
        }
class Spiderman(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider Man',
            'id': 'Peter Parker',
            'image': '/static/images/spider_man.jpg'
        }
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'heroes.html'        