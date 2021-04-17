#引入表单类
from django import forms
#引入我们的文章模型类
from .models import ArticlePost


#创建写文章的表单类，它继承自forms.ModelForm
class ArticlePostForm(forms.ModelForm):
	class Meta:
		#指明数据模型来源
		model = ArticlePost
		#定义表单包含的字段
		fields = ('title', 'body', 'category')