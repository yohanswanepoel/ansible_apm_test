from django.conf.urls import url

from django.views.generic import TemplateView
from django.views import defaults as default_views

from . import views
from . import views_api

app_name="accounts"

urlpatterns = [
    url(r'^$', views.AccountsMainView.as_view(), name='home'),
    url(r'^api/account_list/(?P<user_id>[0-9a-f-]+)/$', views_api.get_accounts, name='account_list_api')
]
