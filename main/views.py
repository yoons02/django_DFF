from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def showmentors(request):
    return render(request, 'main/mentor_list.html')

def showcontact(request):
    return render(request, 'main/contact.html')

def showrecruit(request):
    return render(request, 'main/recruit.html')

def showdff(request):
    return render(request, 'main/dff.html')

def showannounce(request):
    return render(request, 'main/announce.html')

def showmessage(request):
    blogs = Blog.objects.all()

    p = Paginator(Blog.objects.order_by('-id'),10)
    page = request.GET.get('page')
    venues = p.get_page(page)
    return render(request, 'main/message.html',{'blogs':blogs, 'venues':venues})

def showdreamer(request):
    return render(request, 'main/dreamer.html')

def showthanks(request):
    return render(request, 'main/thanks.html')

def showNew(request):
    if request.method == "GET":
        return render(request, 'main/new.html')

def showcomplete(request):
    return render(request, 'main/complete.html')
        
def showPwd(request):
    return render(request, 'main/pwd.html') 

def showPwd_2(request):
    return render(request, 'main/pwd_2.html') 

def showPwd_3(request):
    return render(request, 'main/pwd_3.html') 

def showdetail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'main/detail.html', {'blog':blog})

def create(request):
    new_blog = Blog()
    new_blog.writer = request.POST['writer']
    new_blog.phone = request.POST['phone']
    new_blog.title = request.POST['title']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('main:showcomplete')

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('main:showmessage')

# def test(request):
#     blog_list = Blog.objects.all()
#     page = request.Get.get('page', '1')
#     paginator = Paginator(blog_list,'10')
#     page_obj = paginator.page(page)
#     return render(request, 'main:showmessage', {'page_obj':page_obj})

# def showmessage(request):
#     blog_list = Blog.objects.all() #models.py Board ???????????? ?????? ????????? board_list??? ??????
#     # board_list ????????? ??????
#     page = request.GET.get('page', '1') #GET ???????????? ????????? ???????????? ?????????
#     paginator = Paginator(blog_list, '10') #Paginator(????????? ??????, ????????? ??? ?????? ?????????)
#     page_obj = paginator.page(page) #????????? ????????? ?????? ?????? ???????????? ?????? get_page ??????
#     return render(request, 'main:message.html', {'page_obj':page_obj}) 


