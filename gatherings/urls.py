from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from gatherings import views


urlpatterns = [
    path(
        "gatherings/",
        views.GatheringSet.as_view({'get': 'list'}),
        name="gathering-list",
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
