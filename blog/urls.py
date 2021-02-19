from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('logIn/', auth_views.LoginView.as_view(template_name='logIn.html'), name='logIn'),
    path('signup/', views.signup, name='signup'),
    path('post/<int:post_id>/', views.post_show, name='blog-post-show'),
    path('post/create/', views.PostCreate.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(),
         name='blog-post-Update'),
    path('category/<category_name>/',
         views.category_view, name='blog-category_view'),
    path('post/published', views.published, name='blog-post-published')
]
