from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm


class ReviewView(View):

    def get(self, request: HttpRequest):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {'form': form})

    def post(self, request: HttpRequest):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you')
        return render(request, 'reviews/review.html', {'form': form})


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'
