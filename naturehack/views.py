from django.http import HttpResponse

def testhomepage(request):
    return HttpResponse("test home page")

def testsubpage(request):
    return HttpResponse("test sub page")

def testsubpageparams(request, param):
    return HttpResponse("test sub page param: %s" % param)

