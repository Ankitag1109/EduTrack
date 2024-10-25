from django.shortcuts import redirect, render
from . import views
def index_redirect(request):
    return redirect('/web/')
def attendence(request):
    return render(request, 'web/attendence.html')
def about(request):
    return render(request, 'web/about_us.html')
def examination(request):
    return render(request, 'web/examination.html')
def timeTable(request):
    return render(request, 'web/timeTable.html')
def dashboard(request):
    return render(request, 'web/dashboard.html')
def explore(request):
    return render(request, 'web/explore.html')
def firstpage(request):
    return render(request, 'web/firstpage.html')
def pysoprofile(request):
    return render(request, 'web/pysoprofile.html')
def roadmap(request):
    return render(request, 'web/roadmap.html')
def contact(request):
    return render(request, 'web/contact.html')