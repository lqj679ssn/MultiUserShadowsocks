""" Adel Liu 180111

用户APi子路由
"""
from django.urls import path

from User.router import rt_user, rt_ss, rt_qt_user_app_id

urlpatterns = [
    path('', rt_user),
    path('ss', rt_ss),
    # path('@<str:qt_user_app_id>', rt_qt_user_app_id),
]
