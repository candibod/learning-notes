from django.urls import path
from notes.views import index, render_docs_file

urlpatterns = [
    path('docs/<str:doc_path>', render_docs_file, name='docs-page'),
    path('', index, name='home-page'),
]
