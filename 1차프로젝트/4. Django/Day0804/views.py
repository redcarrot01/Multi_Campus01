from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # name = 'Django'
    # return HttpResponse('''<h2>Post List</h2>
    # <p>웰컴{name}!!!</p><p>{content}</p>'''.format(name=name, content=request.content_type))


    # querySet 사용하여 db에서 Post 목록 가져오기
    posts = Post.objects.filter(published_date__lte=timezone.now())\
        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
                                                    # 키 ,  값
#1. post_list 함수 만들어 요청 받아서 직접 문자열로 html 로 응답
    #return render(request, 'blog/post_list.html')