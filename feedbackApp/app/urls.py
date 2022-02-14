from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in/', views.signin, name="signin"),
    path('sign-up/', views.signup, name="signup"),
    path('forgot-password/', views.forgot_password, name="forgotpassword"),
    path('comment/', views.comment_page, name='comment'),
    path('comment-save/<int:pk>', views.comment_save, name='commentsave'),
    path('comment-filter/', views.comment_filter, name='filtering'),
    path('logout/', views.logout, name='logout'),
    path('404/', views.error_404, name='pagenotfound'),
    path('500/', views.error_500, name='servererror')
]
