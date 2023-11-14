from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def review(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="reviews/review.html")
