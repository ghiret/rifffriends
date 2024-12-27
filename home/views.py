# Create your views here.
from django.http import HttpResponse, HttpRequest


def credits(request: HttpRequest):
    content = "<html><body><p>Example website built following Django In Action chapters by Paco.</p></body></html>"
    return HttpResponse(content=content, content_type="text/html")
