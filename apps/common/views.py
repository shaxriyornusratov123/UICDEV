from django.http import HttpRequest, HttpResponse


def healthcheck(_: HttpRequest) -> HttpResponse:
    return HttpResponse("common ok")
