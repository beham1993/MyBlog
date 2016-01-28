from django.conf.urls import patterns, url, include
from blog.views import ArticleListView, ArticleDetailView, PersonPageView, ArchiveListView
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
	urlpatterns = patterns(
	    '',
	    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
		url(r'^i18n/', include('django.conf.urls.i18n')),
	    url(r'^$', ArticleListView.as_view(), name='index'),
	    url(r'^article/(?P<pk>\d+)/$', ArticleDetailView.as_view()),
	    url(r'^archive/$', ArchiveListView.as_view(), name='archive'),
	    url(r'^about_me/$', PersonPageView.as_view(), name="about_me"),
	)