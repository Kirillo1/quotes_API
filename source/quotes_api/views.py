from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class IndexView(TemplateView):
    template_name = "index.html"


