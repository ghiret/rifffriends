# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse


def credits(request: HttpRequest):
    content = "<html><body><p>Nicky/Paco.</p></body></html>"
    return HttpResponse(content=content, content_type="text/html")


def about(request: HttpRequest):
    content = "<html><body><p>Example website built following Django In Action chapters by Paco.</p></body></html>"
    return HttpResponse(content=content, content_type="text/html")


def version(request: HttpRequest):
    content = {"version": "0.0.1"}
    return JsonResponse(content)
