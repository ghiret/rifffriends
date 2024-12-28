# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.conf import settings
from django.shortcuts import render


def credits(request: HttpRequest) -> HttpResponse:
    content = "<html><body><p>Nicky/Paco.</p></body></html>"
    return HttpResponse(content=content, content_type="text/html")


def about(request: HttpRequest) -> HttpResponse:
    content = "<html><body><p>Example website built following Django In Action chapters by Paco.</p></body></html>"
    return HttpResponse(content=content, content_type="text/html")


def news(request: HttpRequest) -> HttpResponse:
    data = {
        "news": [
            "I have made it to section 3.6 of the book.",
            "RiffFriends has a news page.",
        ]
    }
    return render(request, "news.html", data)


def version(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"version": settings.APP_VERSION})
