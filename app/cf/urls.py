from django.contrib import admin
from django.urls import path

from zones import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.ZoneListView.as_view(), name="zone-list"),
    path("zone-detail-<slug:slug>", views.ZoneDetailView.as_view(), name="zone-detail"),
]
