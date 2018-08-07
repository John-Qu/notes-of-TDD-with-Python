from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    # # return HttpResponse('<html><title>To-Do lists</title></html>')
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text', ''),
    # })
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

