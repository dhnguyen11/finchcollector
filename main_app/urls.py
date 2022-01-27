from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('perches/', views.PerchList.as_view(), name='perches_index'),
    path('parches/<int:pk>/', views.PerchDetail.as_view(), name='perches_detail'),
    path('perches/create/', views.PerchCreate.as_view(), name='perches_create'),
    path('perches/<int:pk>/update/', views.PerchUpdate.as_view(), name='perches_update'),
    path('perches/<int:pk>/delete/', views.PerchDelete.as_view(), name='perches_delete'),
    path('finches/<int:finch_id>/assoc_perch/<int:perch_id>/', views.assoc_perch, name='assoc_perch')
]