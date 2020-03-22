from django.views.generic import ListView
from leagues.models import League

class Home(ListView):
    queryset = League.objects.all()
    template_name = 'home.html'
    context_object_name = 'league_list'