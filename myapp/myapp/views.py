from django.http import HttpResponse
def index(request):
    return HttpResponse('''
    <a href="/about"> About us </a>
    <h1>Hello World</h1>
    
    ''')


def about(request):
    return HttpResponse('''
    <a href="/"> go back to home </a>
    <h1>Hello I am about</h1>
    
    ''')