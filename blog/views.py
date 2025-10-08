from django.http import HttpResponse

def home(request):
    return HttpResponse("Привіт, світ! Це мій перший сайт на Django 🚀")
