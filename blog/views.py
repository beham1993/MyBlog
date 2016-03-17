from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Article, Person, Quote


def logout(request):
    auth_logout(request)
    return redirect('/')


class ArticleListView(ListView):
	model = Article
	template_name = 'index.html'
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super(ArticleListView, self).get_context_data(**kwargs)
		random_idx = random.randint(0, Quote.objects.count() - 1)
		context ['quote'] = Quote.objects.all()[random_idx]
		context ['last_article'] = Article.objects.filter().order_by('-date_of_article')[:4]
		return context

class ArchiveListView(ListView):
	model = Article
	template_name = 'archive.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(ArchiveListView, self).get_context_data(**kwargs)
		random_idx = random.randint(0, Quote.objects.count() - 1)
		context ['quote'] = Quote.objects.all()[random_idx]
		context ['last_article'] = Article.objects.filter().order_by('-date_of_article')[:4]
		return context


class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		random_idx = random.randint(0, Quote.objects.count() - 1)
		context ['quote'] = Quote.objects.all()[random_idx]
		context ['last_article'] = Article.objects.filter().order_by('-date_of_article')[:4]
		return context


class PersonPageView(TemplateView):
	template_name = 'about_me.html'

	def get_context_data(self, **kwargs):
		context = super(PersonPageView, self).get_context_data(**kwargs)
		random_idx = random.randint(0, Quote.objects.count() - 1)
		context ['quote'] = Quote.objects.all()[random_idx]
		context ['last_article'] = Article.objects.filter().order_by('-date_of_article')[:4]
		return context
