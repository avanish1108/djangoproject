from django.db import models

class sendmail(models.Model):
    fromemail = models.EmailField()
    toemail = models.EmailField()
    subject = models.CharField(max_length=20)
    body = models.CharField(max_length=400)
    def __str__(self):
        return self.toemail



