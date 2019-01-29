from django.shortcuts import render,HttpResponse
from .models import MovieInfo

def index(request):
    return render(request, "MovieReview/index.html")

def addMovie(request):
    if request.method == 'POST':

        movie_name=request.POST['movie_name']
        movie_review=request.POST['movie_review']
        movie_release_date=request.POST['movie_release_date']
        movie_genre=request.POST['movie_genre']
        movie_desc=request.POST['movie_desc']

        MovieInfo.objects.create(movie_name=movie_name,movie_review=movie_review,movie_release_date=movie_release_date,movie_genre=movie_genre,movie_desc=movie_desc)

    return render(request, "MovieReview/index.html")

def allMovie(request):
    allMovies= MovieInfo.objects.all()
    return render(request, "MovieReview/allMovies.html", {'movies': allMovies})

def editMovie(request,id):
    editMovies= MovieInfo.objects.get(id = id)
    return render(request, "MovieReview/editMovies.html", {'movies': editMovies})

def updateMovie(request, id):
    if request.method == 'POST':

        id=id
        movie_name=request.POST['movie_name']
        movie_review=request.POST['movie_review']
        movie_release_date=request.POST['movie_release_date']
        movie_genre=request.POST['movie_genre']
        movie_desc=request.POST['movie_desc']

        MovieInfo.objects.filter(id=id).update(movie_name=movie_name,movie_review=movie_review,movie_release_date=movie_release_date,movie_genre=movie_genre,movie_desc=movie_desc)

    return render(request, "MovieReview/index.html")

def deleteMovie(request,id):
    editMovies= MovieInfo.objects.get(id = id).delete()
    return render(request, "MovieReview/index.html", {'movies': editMovies})