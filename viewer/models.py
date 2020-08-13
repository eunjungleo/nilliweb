from django.db import models

class Content(models.Model):
    title = models.TextField()
    url = models.URLField()
    

    korean = models.TextField(null=True)
    chinese = models.TextField(null=True)
    turkmen = models.TextField(null=True)


    q1 = models.IntegerField(null=True)
    q2 = models.IntegerField(null=True)
    q3 = models.IntegerField(null=True)
    q4 = models.IntegerField(null=True)
    q5 = models.IntegerField(null=True)


    def __str__(self):
        return str(self.pk) + "/ " + self.title
        

    

