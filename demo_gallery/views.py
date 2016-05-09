from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from demo_gallery.models import Photo, Item

def home(request):
    photos = Photo.objects.all()[:5]
    items = Item.objects.all()
    return render(request, 'demo_gallery/home.html', {'items': items, 'photos': photos})

def contact(request):
    items = Item.objects.all()
    return render(request, 'demo_gallery/contact.html', {'items': items})

def show_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    items = Item.objects.all()
    photos = Photo.objects.all().filter(item=item_id)
    return render(request, 'demo_gallery/item.html', {'item': item, 'photos': photos, 'items': items})

def list(request):
    photo_count = Photo.objects.all().count()
    photos = Photo.objects.all()[photo_count-4:]
    return render_to_response('demo_gallery/list.html', {"photos": photos})
