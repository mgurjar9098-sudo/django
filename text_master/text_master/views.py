
from django.shortcuts import render
def index(request):
    param={"name":"rahul","age":23}
    return render(request,'index.html',param)

def analyze(request):
    text=request.GET.get('text1')
    # params={"name":text}

    upper=request.GET.get('upper','off')
    lower=request.GET.get('lower','off')
    capital=request.GET.get('capital','off')

    
    if upper=='on':
        params={'text1':text.upper()}

    elif lower=='on':
        params={"text1":text.lower()}

    elif capital=='on':
        params={"text1":text.capitalize()}

    
    else:
        params={"text1":text}


    
    
    return render(request,'analyze.html',params)