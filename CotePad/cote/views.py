from django.views.generic import TemplateView


from .models import Cote


class CoteListView(TemplateView):
    template_name = 'cotes.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Cote.objects.all()
        }


class CoteDetailView(TemplateView):
    template_name = 'cote.html'

    def get_context_data(self, **kwargs):
        return {
            'cote': Cote.objects.get(pk=kwargs['pk'])
        }