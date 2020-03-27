from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("I am the home")


def render_single_note(request: HttpRequest, note_id: str) -> HttpResponse:
    return render(request, 'single_note.html')

