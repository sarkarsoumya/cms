from .settings import FILE_UPLOAD_FOLDER
import os


def handle_uploaded_file(f):
    with open(os.path.join(FILE_UPLOAD_FOLDER, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
