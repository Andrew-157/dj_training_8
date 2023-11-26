from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm


class ReviewView(View):

    def get(self, request: HttpRequest):
        form = ReviewForm()
        return render('reviews/review.html', {'form': form})

    def post(self, request: HttpRequest):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render('reviews/review.html', {'form': form})


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request, 'reviews/thank_you.html')
