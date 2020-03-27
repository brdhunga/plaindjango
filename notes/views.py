import json
from typing import Dict
import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Note


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Maybe this will have all the notes")


@csrf_exempt
def render_single_note(request: HttpRequest, note_id: str) -> HttpResponse:

    if request.method == "POST":
        request_dict: Dict = json.loads(request.body)

        # passKey, content
        note_id = request_dict["noteId"]
        pass_key = request_dict["passKey"]

        if not note_id or not pass_key:
            return HttpResponse("Note id or passkey cannot be empty", status=500)

        if not os.environ["PASSKEY"] == pass_key:
            return HttpResponse("passkey does not match", status=500)
        
        # Note object and boolean object
        note, created = Note.objects.get_or_create(note_id=note_id)
        note.content = request_dict["content"]
        note.save()

        return HttpResponse(note.content)

    note, created = Note.objects.get_or_create(note_id=note_id)
    if created:
        content = ""
    else:
        content = note.content

    return render(request, 'single_note.html', {'noteId': note_id, 'content': content})

