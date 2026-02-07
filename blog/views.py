from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from blog.models import Post

# def home_view(request):
#   return HttpResponse('Главная страница')

def get_post_list(request):
  posts = Post.objects.all()

  return render(request, template_name='blog/post_list.html', context={'posts': posts}) 


def get_post_detail(request, post_id):
  Post.objects.get(id=post_id)

  # return render(request, 'blog/post_detail.html', {'post': Post.objects.get(id=post_id)})
  return render(request, 'blog/post_detail.html', {'post': get_object_or_404(Post, id=post_id)})


def create_post(request):  
  if request.method == "POST":
    title = request.POST.get('title').strip()
    text = request.POST.get('text').strip()

    errors ={}

    if not title:
      errors['title'] = 'Вы забыли заголовок?'
    if not text:
      errors['text'] = 'Вы забыли слова?'
    
    if not errors:
      post = Post.objects.create(title=title, text=text)


    # post = Post.objects.create(title=request.POST.get('title'), text=request.POST.get('text'))

      return redirect('post_detail', post_id=post.id)
    else:
      context = {
        'errors': errors,
        'title': title,
        'text': text
    }

    return render(request, 'blog/post_add.html', context)
  
  
  return render(request, 'blog/post_add.html')