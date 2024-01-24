from django.contrib.admin import ModelAdmin, register

from gatherings.models import Gathering


@register(Gathering)
class GatheringAdmin(ModelAdmin):
    list_display = ("id", "ig_name", "ig_link", "plus_code")
