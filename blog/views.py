from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	categories = Category.objects.all()

	context = {
		'posts':posts,
		'categories':categories,
	}

	return render(request, 'blog/post_list.html', context=context)

def post_detail(request, pk):
	post =	get_object_or_404(Post, pk=pk)
	categories = Category.objects.all()

	context = {
		'post':post,
		'categories':categories,
	}
	return render(request, 'blog/post_detail.html', context=context)

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'blog/category_list.html', {'categories':categories})

def category_detail(request, pk):
	category = get_object_or_404(Category, pk=pk)
	categories = Category.objects.all()

	context = {
		'category':category,
		'categories':categories,
	}

	return render(request, 'blog/category_detail.html', context=context)

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_edit(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_data')
	return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required	
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)
	
def publish(self):
	self.published_date = timezone.now()
	self.save()

@login_required	
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')
	
