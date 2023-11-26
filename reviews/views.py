from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review


def review(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = ReviewForm()

    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
            review.save()
            return HttpResponseRedirect('/thank-you')

    return render(request, 'reviews/review.html', {'form': form})


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request, 'reviews/thank_you.html')
