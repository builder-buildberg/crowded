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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ground = context['object']
        structured_data = {
            "@context": "https://schema.org",
            "@type": "SportsActivityLocation",
            "name": ground.name,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": ground.address,
                "addressLocality": ground.city,
                "addressRegion": ground.area
            },
            "description": ground.description,
            "amenityFeature": [
                {
                    "@type": "LocationFeatureSpecification",
                    "name": "Number of Courts",
                    "value": ground.num_of_courts
                },
                {
                    "@type": "LocationFeatureSpecification",
                    "name": "Sports Type",
                    "value": ground.sports_type
                }
            ],
            "telephone": ground.owner_contact,
            "priceRange": str(ground.price),
            "image": ground.image.url,
            "hasMap": ground.map_link,
            "additionalProperty": [
                {
                    "@type": "PropertyValue",
                    "name": "Has Lights",
                    "value": ground.has_lights
                },
                {
                    "@type": "PropertyValue",
                    "name": "Has Drinks",
                    "value": ground.has_drinks
                }
            ]
        }
        context['structured_data'] = json.dumps(structured_data)
        return context

# function based view for landing page
def home(request):
    return render(request, 'landing.html')

def go(request):
    return render(request, 'go.html')