from django.urls import path

from .views import ButterCMSPageView

app_name = "content"
urlpatterns = [
    # The default home page is under "landing-page-with-components" slug, so let's add a root path to reflect that
    path("", ButterCMSPageView.as_view(), {"slug": "landing-page-with-components"}, name="buttercms_view"),
    # And a path for all the other slugs, that can be accessed directly
    path("<str:slug>/", view=ButterCMSPageView.as_view(), name="buttercms_view"),
]
