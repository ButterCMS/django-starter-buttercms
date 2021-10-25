from butter_cms import ButterCMS

from django.conf import settings


auth_token = settings.BUTTERCMS_API_TOKEN
client = ButterCMS(auth_token)
