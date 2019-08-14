from django import forms
from .models import surveyform
GENDER = [('male','male'),
('female','female'),
]
CHANGE = [('yes','yes'),
('no','no'),
]
INTEREST_CHOICES = [('business','business'),
('Education','Education'),
('Marketing','Marketing'),
('Journalism','Journalism'),
('Psychology','Psychology'),
('Mathematics','Mathematics'),
('IT Programming','IT Programming'),
]
QUALITIES_CHOICES = [('Creative','Creative'),
('Organized','Organized'),
('Methodical','Methodical'),
('Fast learner','Fast learner'),
('Competetive','Competetive'),('Self-educated','Self-educated'),
('Self-motivated','Self-motivated'),
('Decision Maker','Decision Maker'),
('Communicative','Communicative'),
]
HOBBEIES_CHOICES = [('Fishing','Fishing'),
('Cooking','Cooking'),
('Painting','Painting'),
('Gardening','Gardening'),
('Networking','Networking'),
('Programming','Programming'),
('Reading','Reading'),
]
class surveyforms(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect(),)
    career = forms.CharField(widget=forms.Textarea, required=True,)
    change = forms.ChoiceField(choices=CHANGE, widget=forms.RadioSelect(),)
    interest = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=INTEREST_CHOICES,)
    Qualities = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=QUALITIES_CHOICES,)
    Hobbies = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=HOBBEIES_CHOICES,)
    class Meta:
        model = surveyform
        fields = ['name', 'email', 'age','gender','career','change','interest','Qualities','Hobbies']