from django.urls import path

from .views import ButterCMSPageView, ButterCMSBlogView, ButterCMSBlogPostView

app_name = "content"
urlpatterns = [
    # The default home page is under "landing-page-with-components" slug, so let's add a root path to reflect that
    path("", ButterCMSPageView.as_view(), {"slug": "landing-page-with-components"}, name="home"),
    path("blog/", ButterCMSBlogView.as_view(), name="blog"),
    # And a path for all the other slugs, that can be accessed directly
    path("<str:slug>/", view=ButterCMSPageView.as_view(), name="buttercms_view"),
    path("blog/<str:slug>/", view=ButterCMSBlogPostView.as_view(), name="blog_post"),
]
