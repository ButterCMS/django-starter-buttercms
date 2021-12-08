from django.urls import path

from .views import ButterCMSPageView, ButterCMSBlogView, ButterCMSBlogPostView

app_name = "content"
urlpatterns = [
    # The default home page is under "landing-page-with-components" slug, so let's add a root path to reflect that
    path("", ButterCMSPageView.as_view(), {"slug": "landing-page-with-components"}, name="home"),
    # Blog paths
    path("blog/", ButterCMSBlogView.as_view(), name="blog"),
    path("blog/<str:slug>/", view=ButterCMSBlogPostView.as_view(), name="blog_post"),
    path("blog/category/<str:category_slug>/", view=ButterCMSBlogView.as_view(), name="blog_category"),
    path("blog/tag/<str:tag_slug>/", view=ButterCMSBlogView.as_view(), name="blog_tags"),
    # And a path for all the other slugs, that can be accessed directly
    path("blog/search/?q=<str:query>/", view=ButterCMSBlogView.as_view(), name="blog_search"),
    path("<str:slug>/", view=ButterCMSPageView.as_view(), name="buttercms_view"),
]
