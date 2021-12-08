from django.conf import settings
from django.http import Http404
from django.utils import dateparse
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic import TemplateView

from common.buttercms import client


class ButterCMSPageView(TemplateView):
    template_name = "content/page.html"

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
            preview = request.GET.get("preview")
            page = self.get_page(slug, preview=preview)

            if page.get("page_type") == "landing-page":
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
            else:
                # Since there are no implementations for other page types,
                # we raise 404 in this case.
                raise Http404

            context["page"] = page

            context["blog_posts"] = self.get_blog_posts()

            context["navigation_menu"] = self.get_navigation_menu()
        else:
            context["no_token"] = True

        return self.render_to_response(context)

    def get_page(self, slug, preview=None):
        """
        Return page from ButterCMS. Raise 404 if the page is not found
        """
        params = {"preview": 1} if preview else None
        butter_page = client.pages.get(
            "*", slug, params=params
        )  # Use "*" to search through all Page Types
        page_data = butter_page.get("data")

        # If "data" is not in the payload, the page was not fetched successfully
        if page_data is None:
            raise Http404

        return page_data

    def get_blog_posts(self, category_slug=None, tag_slug=None, query=''):
        """
        Return a list of blog posts from ButterCMS. Raise 404 if the page is not found
        """
        kwargs = {"page_size": 10, "page": 1, "exclude_body": "true"}
        if category_slug:
            kwargs.update({"category_slug": category_slug})
        if tag_slug:
            kwargs.update({"tag_slug": tag_slug})
        if query:
            blog_posts = client.posts.search(query)
        else:
            blog_posts = client.posts.all()
            # put something here to handle blank search query #
        blog_posts_data = blog_posts.get("data", [])
        for post in blog_posts_data:
            post['published'] = dateparse.parse_datetime(post['published'])

        # If "data" is not in the payload, the page was not fetched successfully
        if blog_posts_data is None:
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

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
            query = request.GET.get('q')
            category_slug = kwargs.get("category_slug")
            tag_slug = kwargs.get("tag_slug")
            context["blog_posts"] = self.get_blog_posts(
                category_slug=category_slug, tag_slug=tag_slug, query=query)
            context['query'] = query
            context["category_slug"] = category_slug
            context["tag_slug"] = tag_slug
            context["categories"] = client.categories.all().get("data")
            context["navigation_menu"] = self.get_navigation_menu()
        else:
            context["no_token"] = True

        return self.render_to_response(context)

class ButterCMSBlogPostView(ButterCMSBlogView):
    template_name = "content/blog-post.html"

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
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
        butter_post = client.posts.get(slug)
        post_data = butter_post.get("data")
        post_data['published'] = dateparse.parse_datetime(post_data['published'])


        # If "data" is not in the payload, the page was not fetched successfully
        if post_data is None:
            raise Http404

        return post_data
