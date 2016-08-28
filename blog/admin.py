from django.contrib import admin
from blog.models import Article, Person, Quote, Tag, Source

class ArticleAdmin(admin.ModelAdmin):
	fields = ['head_uk', 'head_en', 'sub_head_uk', 'sub_head_en', 'date_of_article', 'article_image', 'text_article_uk', 'text_article_en', 'tag', 'source'],
	list_display = ('head_uk', 'head_en', 'sub_head_uk', 'sub_head_en', 'article_image', 'date_of_article')
	filter_horizontal = ('tag', 'source')
	

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person)
admin.site.register(Quote)
admin.site.register(Tag)
admin.site.register(Source)
