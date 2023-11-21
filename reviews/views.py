from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def review(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/thank-you")

    return render(request=request, template_name="reviews/review.html")


def thank_you(request: HttpRequest) -> HttpResponse:
    return render(request, 'reviews/thank_you.html')
