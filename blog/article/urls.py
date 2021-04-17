from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
	path('article-display/<str:tag>', views.article_display, name='article_display'),
	path('article-index/', views.article_index, name='article_index'),
	path('article-write/', views.article_write, name='article_write'),
	path('article-detail/<int:id>', views.article_detail, name='article_detail'),

]