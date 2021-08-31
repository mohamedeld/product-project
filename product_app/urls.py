from django.urls import path
from . import views

app_name = 'product_app'
urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('<int:product_id>',views.detail,name='detail'),
    path('<int:product_id>/upvote',views.upvote,name='upvote'),
]
