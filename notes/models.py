from django.db import models


class Note(models.Model):
    note_id = models.CharField(max_length=30, blank=True, default="", unique=True)
    content = models.TextField(default="")

    def __str__(self):
        return self.note_id
