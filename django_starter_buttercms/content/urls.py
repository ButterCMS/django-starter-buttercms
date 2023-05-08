from django.urls import path

from .views import (
    ButterCMSBlogPostView,
    ButterCMSBlogSearchView,
    ButterCMSBlogView,
    ButterCMSPageView,
)

app_name = "content"
urlpatterns = [
    # HomePage Routes

    # The default home page is under "landing-page-with-components" slug, so let's add a root path to reflect that
    path("", ButterCMSPageView.as_view(), {"slug": "landing-page-with-components"}, name="home",),

    # Let's also add a backup landing-page route. This allows the user to create and test multiple 
    # landing pages and allows for configuration of both '/' and '/landing-page/' in Butter
    # iframe preview panel.
    path (
        "landing-page/<str:slug>/",
        ButterCMSPageView.as_view(),
        name="landing-pages",
    ),

    #Blog List View
    path("blog/", ButterCMSBlogView.as_view(), {"locale_slug": "en"}, name="blog"),

    # Blog Search View
    path("blog/search/", ButterCMSBlogSearchView.as_view(), {"locale_slug": "en"}, name="blog_search"),
    
    #Blog Detail View
    path("blog/<str:slug>/", ButterCMSBlogPostView.as_view(), {"locale_slug": "en"}, name="blog_post"),

    # Blog Categories View
    path(
        "blog/category/<str:category_slug>/",
        ButterCMSBlogView.as_view(),
        {"locale_slug": "en"},
        name="blog_category",
    ),
    # Blog Tag View
    path(
        "blog/tag/<str:tag_slug>/", ButterCMSBlogView.as_view(), {"locale_slug": "en"}, name="blog_tags"
    ),

    # Note: Deleted catchall route due to conflict with locale_home view

    # Localized Views:

    # Localized Home View:
    path("<str:locale_slug>/", ButterCMSPageView.as_view(), {"slug":"landing-page-with-components"},
        name="home",
    ),

    # Landing Page Backup Route
    path (
        "<str:locale_slug>/landing-page/<str:slug>/",
        ButterCMSPageView.as_view(),
        name="landing-pages",
    ),

    # Blog List Paths
    path("<str:locale_slug>/blog/", ButterCMSBlogView.as_view(), name="blog"),

    # Blog Search View
    path("<str:locale_slug>/blog/search/", ButterCMSBlogSearchView.as_view(), name="blog_search"),
    
    #Blog Detail View
    path("<str:locale_slug>/blog/<str:slug>/", view=ButterCMSBlogPostView.as_view(), name="blog_post"),

    # Blog Categories View
    path(
        "<str:locale_slug>/blog/category/<str:category_slug>/",
        view=ButterCMSBlogView.as_view(),
        name="blog_category",
    ),
    # Blog Tag View
    path(
        "<str:locale_slug>/blog/tag/<str:tag_slug>/", view=ButterCMSBlogView.as_view(), name="blog_tags"
    ),
    # And a path for all the other slugs, that can be accessed directly
    path("<str:locale_slug>/<str:slug>/", view=ButterCMSPageView.as_view(), name="buttercms_view"),
]
