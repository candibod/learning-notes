import os

from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    docs_folder = os.path.realpath(os.getcwd() + "/notes/templates/docs")
    docs_urls = {}

    for path, subdirs, files in os.walk(docs_folder):
        for name in files:
            file_name = os.path.join(path, name).replace(docs_folder, "").removesuffix(".html")
            docs_urls = serialize_file_path(docs_urls, file_name)

    return render(request, 'index.html', {"data": docs_urls})


def serialize_file_path(data, file_path):
    file_path_split = file_path.split(os.sep)

    if len(file_path_split) > 1:
        if file_path_split[0] in data:
            data[file_path_split[0]] = serialize_file_path(data[file_path_split[0]], os.sep.join(file_path_split[1:]))
        else:
            data[file_path_split[0]] = serialize_file_path({}, os.sep.join(file_path_split[1:]))
    else:
        data[file_path_split[0]] = file_path

    return data


def render_docs_file(request, doc_path):
    if len(doc_path) > 40:
        return HttpResponseNotFound("Whoops! Looks like this page went on vacation.")

    print("docpath", doc_path)

    doc_folder = os.path.realpath(os.getcwd() + "/notes/templates/docs/")
    doc_folder = doc_folder + os.sep + doc_path.replace("_", os.sep) + ".html"

    print("folder", doc_folder)

    if not os.path.isfile(doc_folder):
        return HttpResponseNotFound("Whoops! Looks like this page went on vacation.")

    return render(request, "docs/" + str(doc_path).replace("_", os.sep) + ".html")
