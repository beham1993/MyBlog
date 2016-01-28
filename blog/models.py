# -*- coding: utf-8 -*-
from django.db import models
from transmeta import TransMeta
from ckeditor.fields import RichTextField

class Article(models.Model):
	__metaclass__ = TransMeta
	head = models.CharField(max_length=128, verbose_name=u'Заголовок')
	sub_head = models.CharField(max_length=128, verbose_name=u'Підзаголовок')
	date_of_article = models.DateField(verbose_name=u'Дата публікації')
	article_image = models.ImageField(upload_to='images/', verbose_name=u'Фото до статті')
	text_article = RichTextField(verbose_name=u'Текст статті')
	likes = models.IntegerField(default=0)
	twitters = models.IntegerField(default=0)
	facebooks = models.IntegerField(default=0)
	vks = models.IntegerField(default=0)

	def __unicode__(self):
		return self.head

	def get_absolute_url(self):
		return "/article/%i/" % self.id

	class Meta:
		ordering = ['-date_of_article']
		translate = ('head', 'sub_head', 'text_article')

class Person(models.Model):
	name = models.CharField(max_length=64, verbose_name=u"Ім'я")
	birthday_date = models.DateField(verbose_name=u"День народження")
	location = models.CharField(max_length=64, verbose_name=u"Місто")
	email = models.EmailField(max_length=64, verbose_name=u"Електронна пошта")
	skype = models.CharField(max_length=64, verbose_name=u"Скайп")
	vk = models.CharField(max_length=64, verbose_name=u"Вконтакті")
	facebook = models.CharField(max_length=64, verbose_name=u"Фейсбук")
	bio = RichTextField(verbose_name=u"Про себе")

	def __unicode__(self):
		return self.name

class Quote(models.Model):
	quote_text = models.TextField(max_length=256, verbose_name=u"Текст цитати")
	quote_author = models.CharField(max_length=128, verbose_name=u"Автор цитати")
	def __unicode__(self):
		return self.quote_author

