from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from .form import sendmail
from django.conf import settings
from django.contrib.auth.decorators import login_required
@login_required
def mailsend(request):
    if request.method == "GET":
        form = sendmail()
    else:
        form = sendmail(request.POST)
        if form.is_valid(): 
            toemail = form.cleaned_data['toemail']
            
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            try:
                html_content = ' <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script> <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css"><link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"><link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.3/css/mdb.min.css" rel="stylesheet"><script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script><script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script><script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.3/js/mdb.min.js"></script><h1>For Carrer interest survey</h1></br><a href="http://127.0.0.1:8000/surveyform/" class="btn btn-outline-success">survey</a> </br>'
                a=html_content + body
                msg = EmailMultiAlternatives(subject, body, settings.EMAIL_HOST_USER, [toemail])
                msg.attach_alternative(a, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success/')
    return render(request, "sendmail.html", {'form': form})


def success(request):
    return HttpResponse('Success! Thank you for your message.')
def index(request):
    return render(request, "home.html")
    
    # Create your views here.



# class sendmail(BSModalCreateView):
#     def get(self, request, *args, **kwargs): 
#         context = {'form_class':sendmailform()}
#         # form_class = sendmailform(request.GET)
#         return render(request, 'home.html',context)
#     def post(self, request, *args, **kwargs):
#         template_name = 'home.html'
#         form_class = sendmailform(request.POST)
#         if form_class.is_valid(): 

#             toemail = form.cleaned_data['toemail']
#             subject = form.cleaned_data['subject']
#             body = form.cleaned_data['body']
#             try:
#                 html_content = '<p>For Survey</p></br><a href="http://127.0.0.1:8000/survey/">survey</a>'
#                 html_content.append(body)
#                 msg = EmailMultiAlternatives(subject, body, settings.EMAIL_HOST_USER, [toemail])
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()
#                 sendmail = form.save()
#                 sendmail.save()
#                 return HttpResponseRedirect(reverse_lazy('basic:detail_list'))
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#         return render(request, "home.html", {'form': form})



