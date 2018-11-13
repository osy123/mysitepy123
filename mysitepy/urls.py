"""mysitepy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import main.views as main_views
import user.views as user_views
import guestbook.views as guestbook_views
import board.views as board_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_views.index),

    path('user/joinform', user_views.joinform),
    path('user/join', user_views.join),
    path('user/joinsuccess', user_views.joinsuccess),
    path('user/loginform', user_views.loginform),
    path('user/login', user_views.login),
    path('user/logout', user_views.logout),
    path('user/modifyform', user_views.modifyform),
    path('user/checkemail', user_views.checkemail),
    path('user/modify',user_views.modify),

    path('guestbook/', guestbook_views.list),
    path('guestbook/add', guestbook_views.add),
    path('guestbook/deleteform', guestbook_views.deleteform),
    path('guestbook/delete', guestbook_views.delete),
    path('guestbook/list', guestbook_views.list),

    path('board/',board_views.list), # 게시판
    path('board/modify',board_views.modify), # 글수정
    path('board/modifyform',board_views.modifyform), # 글수정폼

    path('board/view',board_views.view),  # 글보기
    path('board/writeform',board_views.writeform),# 글쓰기폼
    path('board/write', board_views.write),  # 글쓰기
    path('board/delete',board_views.delete), # 글삭제

    path('guestbook/ajax',guestbook_views.ajax),
    path('guestbook/api/list',guestbook_views.api_list),
    path('guestbook/api/add',guestbook_views.api_add),

]
