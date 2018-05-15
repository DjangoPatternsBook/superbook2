from django.urls import path, include
from . import views
from . import apiviews

app_name = 'viewschapter'

blog_patterns = [
    path('', views.BlogHomeView.as_view(), name='blog_home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('<slug:slug>/', views.ArticleView.as_view(), name='article'),
]

urlpatterns = [
    path('hello-fn/<str:name>/',
         views.hello_fn, name="hello_fn_name"),
    path('hello-fn/',
         views.hello_fn, name="hello_fn"),

    path('hello-cl/<str:name>/',
         views.HelloView.as_view(), name="hello_cl_name"),
    path('hello-cl/',
         views.HelloView.as_view(), name="hello_cl"),

    path('hello-su/<str:name>/',
         views.SuperVillainView.as_view(), name="hello_su_name"),
    path('hello-su/',
         views.SuperVillainView.as_view(), name="hello_su"),

    path('myfeed/', views.MyFeed.as_view(
        extra_context={'title': 'My Feed'}), name="myfeed"),
    path('public/',
         views.PublicPostJSONView.as_view(), name="public"),

    path('year/<int:year>/',
         views.YearView.as_view(), name="year_view"),

    path('blog/', include(blog_patterns)),

    path('api/public/',
         apiviews.PublicPostList.as_view(), name="api_public"),
]
