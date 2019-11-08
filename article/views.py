from django.shortcuts import render


# View to create an article
def create_article(request):
    print("TEST_PRINT")
    return render(request, 'scriky/index.html')


# View to delete an article
def delete_article(request):
    return render(request, 'scriky/index.html')


# View to edit an article
def edit_article(request):
    return render(request, 'scriky/index.html')


# View to view an article
def view_article(request):
    return render(request, 'scriky/index.html')


# View to search for an article
def search_article(request):
    return render(request, 'scriky/index.html')
