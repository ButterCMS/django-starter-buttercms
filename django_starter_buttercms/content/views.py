from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView

from common.buttercms import client


class ButterCMSPageView(TemplateView):
    template_name = "content/page.html"

    def get(self, request, slug, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Check if API Token is set properly
        if settings.BUTTERCMS_API_TOKEN:
            page = self.get_page(slug)
            if page.get("page_type") == "landing-page":
                # Prepare template names for components
                for component in page.get("fields", {}).get("body", []):
                    component["template_name"] = f"content/component/{component.get('type')}.html"

            context["page"] = page

            context["blog_posts"] = self.get_blog_posts()
        else:
            context["no_token"] = True

        return self.render_to_response(context)

    def get_page(self, slug):
        """
        Return page from ButterCMS. Raise 404 if the page is not found
        """
        butter_page = client.pages.get("*", slug)  # Use "*" to search through all Page Types
        page_data = butter_page.get("data")

        # If "data" is not in the payload, the page was not fetched successfully
        if page_data is None:
            raise Http404

        return page_data

    def get_blog_posts(self):
        """
        Return a list of blog posts from ButterCMS. Raise 404 if the page is not found
        """
        blog_posts = client.posts.all({'page_size': 3, 'page': 1, 'exclude_body': 'true'})
        blog_posts_data = blog_posts.get("data", [])

        # If "data" is not in the payload, the page was not fetched successfully
        if blog_posts_data is None:
            raise Http404

        return blog_posts_data
