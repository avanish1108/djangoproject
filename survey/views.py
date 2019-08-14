from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from survey.models import surveyform
from survey.forms import surveyforms
from django.http import HttpResponse
from django.core.exceptions import AppRegistryNotReady
# class surveyform(CreateView):
#     model = surveyform
#     fields = ['name', 'email', 'age','gender','career','change','interest','Qualities','Hobbeies']
#     success_url = reverse_lazy('theme:index')
# Create your views here.
# class surveyform(CreateView):
#     def get(self, request, *args, **kwargs):
#         context = {'form': surveyform()}
#         return render(request, 'survey/survey.html', context)

#     def post(self, request, *args, **kwargs):
#         form = surveyform(request.POST)
#         if form.is_valid():
#             survey = form.save()
#             survey.save()
#             # return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
#             return HttpResponseRedirect(reverse_lazy('theme:index'))
#         return render(request, 'survey/survey.html', {'form': form})

def survey(request):
    if request.method == "POST":  
        form = surveyforms(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except AppRegistryNotReady:  
                return HttpResponse('Invalid.') 
    else:  
        form = surveyforms()
    return render(request,'survey/survey.html',{'form':form})
def SuccessSurvey(request):
    return HttpResponse('Success! Thank you for your feal a survey form.')
