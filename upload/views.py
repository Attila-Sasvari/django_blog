from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


def image_upload(request):
    if not request.COOKIES.get('django_photo_uploaded'):
        response = HttpResponse("Visiting for the first time.")
        response.set_cookie('django_photo_uploaded', True)
        return response
    else:
        if request.COOKIES.get('django_photo_uploaded'):
            return HttpResponse("You already uploaded photo.")

    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")