from django.urls import path

from tricky import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('<n>', views.index, name='index'),
    path('', views.index, {'n': 20}, name='index'),

]
