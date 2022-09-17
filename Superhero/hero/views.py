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



class Iron_ManView(TemplateView):
    template_name = 'hero.html'


    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'id': 'Tony Stark',
            'image': '/static/images/iron_man.jpg'
        }   

class Ghost_RiderView(TemplateView):
    template_name = 'hero.html'


    def get_context_data(self, **kwargs):
        return {
            'title': 'Ghost Rider',
            'id': 'Johnny Blaze',
            'image': '/static/images/Ghost_Rider.jpg'
        }   

class Spider_ManView(TemplateView):
    template_name = 'hero.html'


    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider-Man',
            'id': 'Peter Parker',
            'image': '/static/images/spider_man.jpg'
        }   


   