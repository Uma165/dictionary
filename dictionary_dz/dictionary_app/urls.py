from django.urls import path

from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.WordListView.as_view(), name='word_list'),
    path('<int:pk>/', views.WordDetailView.as_view(), name='word_detail'),
    path('add/', views.WordCreateView.as_view(), name='word_create'),
    path('<int:pk>/update/', views.WordUpdateView.as_view(), name='word_update'),
    path('<int:pk>/delete/', views.WordDeleteView.as_view(), name='word_delete'),
    path('search/', views.WordSearchView.as_view(), name='word_search'),
]