from django.urls import path, include

urlpatterns = [
    path('api/account/', include('account.urls')),
    path('api/', include('posts.urls')),
]
