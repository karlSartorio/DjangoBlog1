from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('aboutus/',views.AboutUsView.as_view(), name='aboutus'),
    path('', views.PostListView.as_view(), name='homepage'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # when a user click on a blog it will get the pk for it then, it will send that pk with the post
    # then it will then find the Pk in the model and give the infromation back from the model.
    path('post/new-post>', views.PostCreateView.as_view(), name=('post_new'),
    path('post/<int:pk>/edit/'),views.PostUpateView.as_view(), name=('post_edit'),
    path('post/<int:pk>/remove>', views.PostDeleteView.as_view(), name='post_delete'),
    path('draft/', views.DraftListView.as_view(), name='post_draft_list')

]
