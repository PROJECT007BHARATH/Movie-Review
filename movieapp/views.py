from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm, ReviewForm
from .models import Review


# Create your views here.

def home(request):
    items = movie.objects.all()
    context = {
        'items': items
    }
    return render(request, "home.html", context)


def demo(request):
    query = request.GET.get("search-field")
    if query:
        Movie = movie.objects.filter(category=query)

    else:
        Movie = movie.objects.all()
    context = {
        'movie_list': Movie
    }
    return render(request, 'base.html', context)


def detail(request, movie_id):
    Movie = movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': Movie})


def add_movie(request):
    if request.method == "POST":
        category = request.POST.get('category')
        Movie_Name = request.POST.get('Movie_Name')
        Release_date = request.POST.get('Release_date')
        Trailer = request.POST.get('Trailer')
        Description = request.POST.get('Description')
        Actors = request.POST.get('Actors')
        Picture = request.FILES['Poster']
        Movie = movie(category=category, Movie_Name=Movie_Name, Release_date=Release_date, Trailer=Trailer,
                      Description=Description, Actors=Actors, Poster=Picture)
        Movie.save()
        print(Picture)
        return redirect('/')
    return render(request, 'add.html')


def delete(request, id):
    if request.method == 'POST':
        Movie = movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    Movie = movie.objects.get(id=id)

    if request.method == 'POST':
        Form = MovieForm(request.POST, request.FILES, instance=Movie)
        if Form.is_valid():
            Form.save()
            return redirect('/')
    else:
        Form = MovieForm(instance=Movie)
    return render(request, 'edit.html', {'Form': Form, 'Movie': Movie})


def rate(request, id):
    post = movie.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars=stars, comment=comment, movie=post)
        review.save()
        return redirect('success')

    forms = ReviewForm()
    context = {
        "forms": forms

    }
    return render(request, 'rate.html', context)


def success(request):
    return render(request, "success.html")
