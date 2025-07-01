from django.conf import settings
from django.http import Http404
from django.utils import dateparse
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.views.decorators.clickjacking import xframe_options_exempt
from requests.exceptions import HTTPError

from common.buttercms import client
import logging
logger = logging.getLogger(__name__)

class ButterCMSPageView(TemplateView):
    template_name = "content/page.html"

    @xframe_options_exempt
    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
            preview = request.GET.get("preview")
            page = self.get_page("landing-page", slug, preview=preview)
            
            # Prepare template names for components
            for component in page.get("fields", {}).get("body", []):
                # Check that the this project has a template for this component
                template_name = f"content/component/{component.get('type')}.html"
                try:
                    get_template(template_name)
                except TemplateDoesNotExist:
                    # Template doesn't seem to exist, so let's set it to fallback
                    template_name = "content/partials/missing-component.html"

                component["template_name"] = template_name
        

            context["page"] = page
            context["blog_posts"] = self.get_blog_posts()
            context["navigation_menu"] = self.get_navigation_menu()
        else:
            context["no_token"] = True

        return self.render_to_response(context)

    def get_page(self, page_type, slug, preview=None):
        """
        Return page from ButterCMS. Raise 404 if the page is not found
        """
        params = {"preview": 1} if preview else None
        
        try:
            butter_page = client.pages.get(
                page_type, slug, params=params
            )  # Use "*" to search through all Page Types
        except HTTPError as error:
            if str(error) == "401":
                # log error if token is invalid
                logger.error(
                    """***Your Butter token is set to an invalid value. Please verify your token is correct.***"""
                )
                raise Http404("""***Your Butter token is set to an invalid value. Please verify your token is correct.***""")
            else:
                logger.error(
                    """***Couldn't fetch page.***"""
                )
                raise Http404

        return butter_page.get("data")


    def get_blog_posts(self, category_slug=None, tag_slug=None, preview=None):
        """
        Return a list of blog posts from ButterCMS. Raise 404 if the page is not found
        """
        kwargs = {"page_size": 3, "page": 1, "exclude_body": "true"}
        if category_slug:
            kwargs.update({"category_slug": category_slug})
        if tag_slug:
            kwargs.update({"tag_slug": tag_slug})
        if preview:
            kwargs.update({"preview": preview})
        try:
            blog_posts = client.posts.all(params=kwargs)
            blog_posts_data = blog_posts.get("data", [])
            for post in blog_posts_data:
                post['published'] = dateparse.parse_datetime(post['published'])
        except HTTPError as error:
            if str(error) == "401":
                # log error if token is invalid
                logger.error(
                    """***Your Butter token is set to an invalid value. Please verify your token is correct.***"""
                )
                raise Http404("""***Your Butter token is set to an invalid value. Please verify your token is correct.***""")
            else:
                logger.error(
                    """***Couldn't fetch page.***"""
                )
                raise Http404

        return blog_posts_data

    def search_blog_posts(self, query, preview=None):
        """
        Return a list of blog posts from ButterCMS that match the search query.

        Raise 404 if the page is not found.
        """
        kwargs = {"page_size": 3, "page": 1, "exclude_body": "true"}
        if preview:
            kwargs.update({"preview": preview})
        try:
            blog_posts = client.posts.search(query=query, params=kwargs)
            blog_posts_data = blog_posts.get("data", [])
            for post in blog_posts_data:
                post['published'] = dateparse.parse_datetime(post['published'])
        except HTTPError as error:
            if str(error) == "401":
                # log error if token is invalid
                logger.error(
                    """***Your Butter token is set to an invalid value. Please verify your token is correct.***"""
                )
                raise Http404("""***Your Butter token is set to an invalid value. Please verify your token is correct.***""")
            else:
                logger.error(
                    """***Couldn't fetch page.***"""
                )
                raise Http404
        return blog_posts_data

    def get_navigation_menu(self):
        """
        Return a navigation menu from ButterCMS. Raise 404 if the "Main menu" is not found
        """
        butter_navigation_menu = client.content_fields.get(["navigation_menu"])
        navigation_menus = butter_navigation_menu.get("data", {}).get(
            "navigation_menu", []
        )

        main_menu = [
            menu for menu in navigation_menus if menu.get("name") == "Main menu"
        ]

        if not main_menu:
            raise Http404

        return main_menu[0]


class ButterCMSBlogView(ButterCMSPageView):
    template_name = "content/blog.html"

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
            preview = request.GET.get("preview")
            category_slug = kwargs.get("category_slug")
            tag_slug = kwargs.get("tag_slug")
            context["blog_posts"] = self.get_blog_posts(
                category_slug=category_slug, tag_slug=tag_slug, preview=preview
            )
            context["category_slug"] = category_slug
            context["tag_slug"] = tag_slug
            context["categories"] = client.categories.all().get("data")
            context["navigation_menu"] = self.get_navigation_menu()
        else:
            context["no_token"] = True

        return self.render_to_response(context)


class ButterCMSBlogSearchView(ButterCMSPageView):
    template_name = "content/blog.html"

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
            search_query = request.GET.get("q")
            preview = request.GET.get("preview")
            context["blog_posts"] = self.search_blog_posts(search_query)
            context["search_query"] = search_query
            context["categories"] = client.categories.all().get("data")
            context["navigation_menu"] = self.get_navigation_menu()
        else:
            context["no_token"] = True

        return self.render_to_response(context)


class ButterCMSBlogPostView(ButterCMSBlogView):
    template_name = "content/blog-post.html"

    @xframe_options_exempt
    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
            preview = request.GET.get("preview")
            blog_post = self.get_blog_post(slug)
            context["blog_post"] = blog_post
            context["categories"] = client.categories.all().get("data")
            context["navigation_menu"] = self.get_navigation_menu()
        else:
            context["no_token"] = True

        return self.render_to_response(context)

    def get_blog_post(self, slug):
        """
        Return a blog post from ButterCMS. Raise 404 if the post is not found
        """
        try:
            butter_post = client.posts.get(slug)
            post_data = butter_post.get("data")
            post_data['published'] = dateparse.parse_datetime(post_data['published'])

            return post_data
        except HTTPError as error:
            if str(error) == "401":
                # log error if token is invalid
                logger.error(
                    """***Your Butter token is set to an invalid value. Please verify your token is correct.***"""
                )
                raise Http404("""***Your Butter token is set to an invalid value. Please verify your token is correct.***""")
            else:
                logger.error(
                    """***Couldn't fetch page.***"""
                )
                raise Http404
