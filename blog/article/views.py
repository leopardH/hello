from django.shortcuts import render, redirect
from article.models import ArticlePost
#引入ArticlePostForm类
from .forms import ArticlePostForm
# Create your views here.
from django.http import HttpResponse
#引入User模型
from django.contrib.auth.models import User

def hello(request, id):
	return HttpResponse("hello world, django.number %d" % id)

def test(request):
	return render(request, 'test.html', {'current_time':datetime.now()})

def article_index(request):
	post_list = ArticlePost.objects.all() #获取全部的实例
	return render(request, 'index.html', {'post_list': post_list})

def article_display(request, tag):
    try:
        post_list = ArticlePost.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'display.html', {'post_list' : post_list, 'tag' : tag})

# def article_display(request):
# 	post_list = ArticlePost.objects.all() #获取全部的实例
# 	return render(request, 'display.html', {'post_list': post_list})

def article_detail(request, id):
	#取出相应文章
	post = ArticlePost.objects.get(id=id)
	#需要传递给模板的对象
	context = {'post':post}
	#载入模板，返回context对象
	return render(request, 'detail.html', context)

def article_write(request):
	#判断用户是否提交数据
	if request.method == "POST":
		#将提交的数据赋值到表单实例中
		article_post_form = ArticlePostForm(data=request.POST)
		print(article_post_form)
		#判断提交的数据是否满足模型的要求
		if article_post_form.is_valid():
			#保存数据，但暂时不提交到数据库中
			new_article = article_post_form.save(commit=False)
			#制定数据库中id=1的用户为作者
			new_article.author = User.objects.get(id=1)
			#将新文章保存到数据库中
			new_article.save()
			#完成后返回到文章列表
			return redirect('article:article_home')
		#如果数据不合法，返回错误信息
		else:
			return HttpResponse('表单内容有误，请重新填写。')
	#如果用户请求获取数据
	else:
		#创建表单类实例
		article_post_form = ArticlePostForm()
		#赋值上下文
		context = { 'article_post_form':article_post_form }
		#返回模板
		return render(request, 'write.html', context)

	