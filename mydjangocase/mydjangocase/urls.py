
"""mydjangocase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from hello import views
from mydjangocase import testdb
from django.urls import path, include
from django.contrib import admin
import xadmin
from . import settings
from django.views.static import serve
from django.conf.urls import url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^demo$', views.demo),
    path('page1/', views.page1),
    path('sonpage/', views.sonpage),
    url(r'^testdb$', testdb.testdb),
    url(r'^register$', testdb.add_user),
    url(r'^update_data$', testdb.update_user),
    url(r'^mail$', testdb.select_user),
    url(r'^select_all$', testdb.select_all),
    url(r'^select_values$', testdb.select_valus),
    url(r'^select_f_l$', testdb.sele_first_last),
    url(r'^getjson$', testdb.get_json),
    # url(r'^admin/$', admin.site.urls),
    url(r'^qq/$', views.test_qq),
    url(r'^result/$', views.result_qq),
    url(r'^email/$', views.user),
    url(r'^register/', views.register),
    # url(r'^login/', views.login),
    url(r'^reset/', views.reset_pwd),
    url(r'^mail/', views.mail),
    url(r'^more_mail/', views.mass_mail),
    url(r'^mail_html/', views.mail_html),
    url(r'^mail_file/', views.mail_file),
    url(r'^xadmin/', xadmin.site.urls),  # xadmin
    url(r'^admin/', admin.site.urls),  # 原来的admin
    url(r'^login/', views.loginView),
    url(r'^logout/', views.logoutView),
    url(r'^success/', views.successView),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^weather_web', views.weather),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^', include(router.urls)),
    url(r'^api/v1/login/$', views.LoginViewSet.as_view()),
    url(r'^api/v1/cards/$', views.CardListView.as_view()),
    url(r'^api/v1/cardlist/$', views.CardListAPIView.as_view()),
    url(r'^userinfo', views.UserPersonalInfoView.as_view()),
    url(r'^card_list_view', views.card_list_view),
    url(r'^api/test/demo/$', views.StudentListAPIView.as_view()),


]
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
