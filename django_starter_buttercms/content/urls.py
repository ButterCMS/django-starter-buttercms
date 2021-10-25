from django.urls import path

from .views import ButterCMSPageView

app_name = "users"
urlpatterns = [
    path("<str:slug>/", view=ButterCMSPageView.as_view(), name="buttercms_view"),
]
