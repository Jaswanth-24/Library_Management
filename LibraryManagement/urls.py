from django.contrib import admin
from django.urls import path
from Library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                  # selection page
    path('index/', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('return/', views.returnn, name='return'),
    path('contact/', views.contact, name='contact'),
    path('admin_custom/', views.admin_custom, name='admin_custom'),
    path('user_login/', views.user_login, name='user_login'),     # corrected
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),  # corrected
    path('admin_login/',views.admin_login,name='admin_login')
]
