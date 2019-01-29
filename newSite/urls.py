from django.conf.urls import url, include
from django.contrib import admin
import MovieReview
from django.urls import path


urlpatterns = [
    url('admin/',admin.site.urls),
    url(r'^$', include('MovieReview.urls')),
    url(r'add_movie/', MovieReview.views.addMovie, name="add_movie"),
    url(r'all_movie/', MovieReview.views.allMovie, name="all_movie"),
    path('edit_movie/<id>', MovieReview.views.editMovie, name="edit_movie"),
    path('update_movie/<id>', MovieReview.views.updateMovie, name="update_movie"),
    path('delete_movie/<id>', MovieReview.views.deleteMovie, name="delete_movie"),
]
