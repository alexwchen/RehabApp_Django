from django.conf.urls.defaults import *
from portal.views import *

urlpatterns = patterns('',

    # Main web portal entrance.
    (r'^$', portal_main_page),
    (r'^register$', register),

    
    (r'^article/(?P<article_name>\w+)$', get_article_text),

    (r'^article/(?P<article_name>\w+)/author$', get_article_author),
)
