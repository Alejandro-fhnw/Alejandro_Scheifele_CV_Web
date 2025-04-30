from django.urls import path
from . import views

urlpatterns = [
    path('',            views.home,         name='home'),
    path('about/',      views.about,        name='about'),
    path('skills/',     views.skills,       name='skills'),
    path('work/',       views.work,         name='work'),
    path('projects/',   views.projects,     name='projects'),

    # Blog-Übersicht
    path('blog/',                   views.blog,         name='blog'),

    # Einzelner Blogpost – nimmt einen Slug entgegen
    path('blog/<slug:slug>/',       views.post_detail,  name='post_detail'),

    path('contact/',    views.contact,      name='contact'),
]
