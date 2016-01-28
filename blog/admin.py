from django.contrib import admin
from blog.models import Article, Person, Quote

class ArticleAdmin(admin.ModelAdmin):
	fields = ['head_uk', 'head_en', 'sub_head_uk', 'sub_head_en', 'date_of_article', 'article_image', 'text_article_uk', 'text_article_en'],
	list_display = ('head_uk', 'head_en', 'sub_head_uk', 'sub_head_en', 'article_image', "date_of_article")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person)
admin.site.register(Quote)
