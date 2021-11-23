from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Zone, Agency, User, Profile


class ZoneListView(ListView):
    model = Zone


class ZoneDetailView(DetailView):
    model = Zone


class ZoneCreateView(CreateView):
    model = Zone
    fields = "__all__"


class ZoneUpdateView(UpdateView):
    model = Zone
    fields = "__all__"
    template_name_suffix = "_update_form"
