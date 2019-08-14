from django import forms
class sendmail(forms.Form):
    toemail = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)


# from django import forms
# from .models import sendmail
# from bootstrap_modal_forms.forms import BSModalForm
# class sendmailform(BSModalForm):
#     class Meta:
#         model =sendmail
#         fields =['toemail','subject','body']

