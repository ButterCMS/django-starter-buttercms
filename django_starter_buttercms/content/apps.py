from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentConfig(AppConfig):
    name = "django_starter_buttercms.content"
    verbose_name = _("Content")
