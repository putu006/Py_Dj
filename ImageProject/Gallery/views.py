from django.shortcuts import render
from .models import ImageData
from .forms import ImageRegister
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    if request.method=='POST':
        fm1=ImageRegister(request.POST,request.FILES)
        if fm1.is_valid():
            fm1.save()
            return HttpResponseRedirect('/')
    else:
        fm1=ImageRegister()
    fm = ImageRegister()
    im = ImageData.objects.all()
    cat = ImageData.objects.values('category').distinct()
    return render(request,'main.html',{'fm':fm,'img':im,'cat':cat})


def delete(request,id):
    data = ImageData.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/')

# def filter(request,cat):
#     fil = ImageData.objects.filter(category='cat')
#     return HttpResponseRedirect('/')