# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.conf import settings


def credits(request: HttpRequest):
    content = "<html><body><p>Nicky/Paco.</p></body></html>"
    return HttpResponse(content=content, content_type="text/html")


def about(request: HttpRequest):
    content = "<html><body><p>Example website built following Django In Action chapters by Paco.</p></body></html>"
    return HttpResponse(content=content, content_type="text/html")


def version(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"version": settings.APP_VERSION})
