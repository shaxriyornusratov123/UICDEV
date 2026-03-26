from django.http import HttpRequest, HttpResponse


def healthcheck(_: HttpRequest) -> HttpResponse:
    return HttpResponse("courses ok")
