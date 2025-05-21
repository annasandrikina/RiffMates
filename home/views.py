from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def credits(request):
    content = "Nicky\n Anna"
    return HttpResponse (content, content_type="text/plain")

def news (request):
    data = {"news" : [
        "Riifmates now has new page!",
        "Riffmates has its first page "
    ]}
    return render (request, "news.html", data )
