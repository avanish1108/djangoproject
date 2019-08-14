from django.urls import path
from . views import survey,SuccessSurvey
app_name = 'survey'

urlpatterns = [
    path('', survey, name="survey"),
    path('/success', SuccessSurvey, name="SuccessSurvey"),

]