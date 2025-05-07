from django.urls import re_path

from .views import *

urlpatterns = [
    re_path(r'^dictionary$', dictionary_list),
    re_path(r'^dictionary/check$', dictionary_detail),

    re_path(r'^log$', public_log_list),
]
