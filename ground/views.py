from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render
from ground.models import Ground
import json

class GroundListView(ListView):
    model = Ground
    template_name = 'ground/ground_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(Ground.objects.values()))
        return context

# class based detail view for ground
class GroundDetailView(DetailView):
    model = Ground
    template_name = 'ground/ground_detail.html'

# function based view for landing page
def home(request):
    return render(request, 'landing.html')

def go(request):
    return render(request, 'go.html')