from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse, QueryDict
from hello.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail, send_mass_mail
from django.core.mail import EmailMessage
import os
from rest_framework import viewsets, serializers
from .models import *
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.views.generic.base import View
from django.core import serializers as dj_serializers  # 避免和rest_framework里面的serializers冲突
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializersapi import UserPersonalInfoSerializer
from rest_framework.decorators import api_view





# Create your views here.


def index(request):

        return HttpResponse("jjjj")

def weather(request):
    return render(request, 'weather.html')


def page1(request):
    context = {'name': "尚柯"}
    return render(request, 'page1.html', context)


def sonpage(request):
    context = {'name': "尚柯", "ads": ["selenium", "Appium", "requests"]}
    return render(request, 'sonpage.html', context)


# 测试你的qq号码
def test_qq(request):
    """请求页面"""
    return render(request, 'get_demo.html')


# 提交后返回页面
def result_qq(request):
    """返回结果"""
    if request.method == 'GET':
        # r = request.GET["q"]
        r = request.GET.get('qq', None)  # key_name不存在时,不会报错
        res = ""

        try:
            if int(r) % 2:
                res = "大吉大利!"
            else:
                res = "恭喜发财!"

        except:

            res = "请输入正确的QQ号!"
        return HttpResponse("测试结果：%s" % res)
    else:
        render(request, 'get_demo.html')

    # return HttpResponse("提交成功！")
# 查询数据
def user(request):

    res = ""
    if request.method == 'GET':
        # 获取提交的数据
        # r = request.GET["q"] # key就是前面输入框里的name属性对应值name="q"
        n = request.GET.get('name', None)
        res = User.objects.filter(user_name="%s" % n)
        try:
            res = res[0].mail

        except:

            res = "未查询到数据"

        return render(request,'name.html', {'email': res})
    else:
        return render(request, 'name.html', {'email': res})

# 注册
def register(request):
    """注册页面"""
    error_name = ''
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        mail = request.POST.get('mail')
        # 先查询数据库是否有此用户名
        user_list = User.objects.filter(user_name=username)
        if user_list:
            # 如果已经注册过，就给个提示
            error_name = "%s用户已被注册" % username
            return render(request, 'register.html', {'error_name': error_name})
        else:
            # 如果没被注册，插入数据库
            user1 = User()
            user1.user_name = username
            user1.pwd = make_password(pwd)
            user1.mail = mail
            user1.save()
            # 第二种写法
            # user = User(user_name=username,
            #            psw = psw,
            #            mail = mail,
            #            )
            # user.save()
            return HttpResponseRedirect('/login/')
            # return render(request, 'login.html', {'rename': res})
    return render(request, 'register.html')

# 登录
def login1(request):
    """登录页面"""
    error_msg = ''
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    if request.method == 'POST':
        # error_msg = ''
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        # pwd1 = make_password(pwd)

        # user_obj = User.objects.filter(user_name=username, pwd=pwd).first()
        #
        # if user_obj:
        #     return HttpResponse("登陆成功")
        # else:
        #     return HttpResponse('用户名或密码错误')
        # 查询用户名对应的密码
        ret = User.objects.filter(user_name=username).first()
        # ret = User.objects.filter(user_name=username, pwd=pwd1)
        # 校验密码
        is_pwd_true = check_password(pwd, ret.pwd)
        if is_pwd_true:
            return HttpResponse('登陆成功')
            # return render(request, 'login.html', {'password': '用户密码错误'})
            # return redirect('https://www.cnblogs.com/qican/')
        else:
            error_msg = '用户名或密码错误，请重新输入'
            return render(request, 'login.html', {'error_msg': error_msg})
            # return HttpResponse('用户名或密码错误')
            # return render(request, 'login.html', {'username': '用户不存在'})
    return render(request, 'login.html')

# 重置密码
def reset_pwd(request):
    res = ''
    if request.method == 'GET':
        return render(request, 'reset_psw.html', {'msg': res})
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        new_pwd = request.POST.get('new')

        if pwd == new_pwd:
            res = "新密码和旧密码不能重复"
            return render(request, 'reset_psw.html', {'msg': res})
        else:
            user_list = User.objects.filter(user_name=username)
            if not user_list:
                res = "用户未注册：%s" % username
                return render(request, 'reset_psw.html', {'msg': res})
            else:
                ret = User.objects.filter(user_name=username).first()
                is_pwd_true = check_password(pwd, ret.pwd)
                if is_pwd_true:
                    ret.pwd = make_password(new_pwd)
                    ret.save()
                    # ret.set_password(new_pwd)
                    # ret.save()
                    res = '密码修改成功'
                else:
                    res = '密码错误'
                return render(request, 'reset_psw.html', {'msg': res})

# 发送邮件
def mail(request):
    send_mail('我要努努力！',
              '我的第一个邮件测试',
              '417799035@qq.com',
              ['417799035@qq.com'],
              fail_silently=False)
    return HttpResponse('邮件发送成功，收不到就去垃圾箱找找吧！')

# 发送多个邮件
def mass_mail(request):
    message1 = ('我要努努力！',
              '我的第一个邮件测试',
              '417799035@qq.com',
              ['417799035@qq.com'],
              )
    message2 = ('找到女朋友！',
              '我的第二个邮件测试',
              '417799035@qq.com',
              ['417799035@qq.com'],
              )
    send_mass_mail((message1,message2),
                   fail_silently=False)
    return HttpResponse('邮件多个发送成功，收不到就去垃圾箱找找吧！')
# 发送邮件带HTML
def mail_html(request):
    """发送html格式邮件"""
    h = """
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>带图片的邮件</title>
    </head>
    <body>
    <a href="https://yuedu.baidu.com/ebook/902224ab27fff705cc1755270722192e4536582b" target="_blank">
        <p> pytest教程,点图片进入：<br>
        <img src="https://img2018.cnblogs.com/blog/1070438/201902/1070438-20190228112918941-704279799.png" height="160" width="270" />
        </p></a>
    <p>
    其它图片：<br>
    <img src="http://www.w3school.com.cn/i/eg_chinarose.jpg" height=150 width=300/></p>
    <p>请注意，插入动画图像的语法与插入普通图像的语法没有区别。</p>
    </body>
    </html>
    """
    send_mail('我要努努力！',
              '我的第一个邮件测试',
              '417799035@qq.com',
              ['417799035@qq.com'],
              html_message=h,
              fail_silently=False)
    return HttpResponse('邮件HTML发送成功，收不到就去垃圾箱找找吧！')


# 发送邮件带附件
def mail_file(request):
    """发送附件"""
    email = EmailMessage(
        '争取32岁结婚',
        '那个你在哪里',
        '417799035@qq.com',  # 发件人
        ['417799035@qq.com', '417799035@qq.com'],  # 收件人
        ['417799035@qq.com'],  # cc抄送
        reply_to=['417799035@qq.com'],  # “回复”标题中使用的收件人地址列表或元组
        headers={'Message-ID': 'foo'},
    )
    cur = os.path.dirname(os.path.realpath(__file__))
    # templates目录下有个a.jpg的图片
    filepath = os.path.join(cur, "templates", "a.jpg")

    email.attach_file(filepath, mimetype=None)
    email.send()
    return HttpResponse('邮件附件发送成功，收不到就去垃圾箱找找吧！')

def loginView(request):
    """登录"""
    if request.method == "POST":
        username = request.POST.get('username', '')
        psw = request.POST.get('password', '')
        user = authenticate(username=username, password=psw)
        if user is not None:
            if user.is_active:
                login(request, user=user)
                request.session['user'] = username
                return HttpResponseRedirect('/success')
        else:
            return render(request, 'login.html', {'msg': '账号或者密码错误！'})
    else:
        return render(request, 'login.html', {'msg': ''})

@login_required
def successView(request):
    """登录页面"""
    return render(request, 'success.html', {'msg': ''})

def logoutView(request):
    """退出登录"""
    logout(request)   # 这个方法，会将存储在用户session的数据全部清空
    return render(request, 'login.html', {'msg': ''})


def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}
    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
class CardViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)   # token认证
    permission_classes = (IsAuthenticated,)  # # IsAuthenticated 仅通过认证的用
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)

    def post(self, request, *args, **kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)

    def put(self, request, *args, **kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)

class LoginViewSet(APIView):
    '''登录获取token方法'''
    permission_classes = (AllowAny,)  # AllowAny 允许所有用户

    """登录方法"""
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user:
            return JsonResponse({"code": 0,
                                 "msg": "用户名密码不对"})
        # 删除原有Token
        old_token = Token.objects.filter(user=user)
        old_token.delete()
        # 创建新的Token
        token = Token.objects.create(user=user)
        return JsonResponse({"code": 1,
                             "msg": "login success",
                             "token": token.key})





class CardListView(View):
    '''基于django的view实现获取card列表'''
    def get(self, request):
        data = {}
        cards = Card.objects.all()
        data['result'] = json.loads(dj_serializers.serialize("json", cards))
        return JsonResponse(data)


class CardAPISerializer(serializers.ModelSerializer):   # 继承自ModelSerializer类
    '''序列化数据的类，根据model表来获取字段'''
    class Meta:
        model = Card
        fields = '__all__'


class CardListAPIView(APIView):
    '''REST framework的APIView实现获取card列表 # shangke'''
    # authentication_classes = (TokenAuthentication,)  # token认证
    # permission_classes = (IsAuthenticated,)   # IsAuthenticated 仅通过认证的用户
    permission_classes = (AllowAny,)  # 允许所有用户

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        cards = Card.objects.all()
        serializer = CardAPISerializer(cards, many=True)
        return Response({"code": 0,
                         "data": serializer.data,
                         "msg": "success!"})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def card_list_view(request):
    '''基于函数式实现get和post请求'''
    cards = Card.objects.all()
    serializer = CardAPISerializer(cards, many=True)
    if request.method == 'GET':
        return Response(serializer.data)

    elif request.method == 'POST':
        verify_data = CardAPISerializer(data=request.data)
        if verify_data.is_valid():
            verify_data.save()
            return Response({"message": "create some data!", "data": request.data})
        else:
            return Response(verify_data.errors)
    else:
        return Response({"message": "request method mot valid!"})

class UserPersonalInfoView(APIView):
    '''REST framework的APIView实现获取UserPersonalInfo表 # 作者：上海悠悠，QQ交流群：750815713'''
    # authentication_classes = (TokenAuthentication,)  # token认证
    # permission_classes = (IsAuthenticated,)   # IsAuthenticated 仅通过认证的用户
    permission_classes = (AllowAny,)  # 允许所有用户

    def get(self, request, format=None):
        """
        Return a list of all UserPersonalInfo
        """
        info = UserPersonalInfo.objects.all()
        serializer = UserPersonalInfoSerializer(info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        '''
        create UserPersonalInfo
        '''
        verify_data = UserPersonalInfoSerializer(data=request.data)
        if verify_data.is_valid():
            verify_data.save()
            return Response({"message": "create some data!", "data": request.data})
        else:
            return Response(verify_data.errors)


class StudentAPISerializer(serializers.ModelSerializer):   # 继承自ModelSerializer类
    '''序列化数据的类，根据model表来获取字段'''
    class Meta:
        model = Student
        fields = '__all__'


class StudentListAPIView(APIView):
    '''REST framework的APIView实现获取card列表 # shangke'''
    # authentication_classes = (TokenAuthentication,)  # token认证
    # permission_classes = (IsAuthenticated,)   # IsAuthenticated 仅通过认证的用户
    permission_classes = (AllowAny,)  # 允许所有用户

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        student = Student.objects.all()
        serializer = StudentAPISerializer(student, many=True)
        return Response({"code": 0,
                         "data": serializer.data,
                         "msg": "success!"})