
from django.contrib import admin
from django.urls import path,include
import wordcounts.urls
import blog.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.list, name = "list"),
    path('blog/',include(blog.urls)),
    path('wordcounts/',include(wordcounts.urls)),
   
]
