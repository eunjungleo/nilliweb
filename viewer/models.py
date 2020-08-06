from django.db import models

class Content(models.Model):
    title = models.TextField()
    url = models.URLField()
    date = models.DateTimeField(auto_now=True)
    korean = models.TextField(null=True)
    chinese = models.TextField(null=True)
    turkmen = models.TextField(null=True)
    eng = models.TextField(null=True)

    def __str__(self):
        return str(self.pk) + "/ " + self.title
    

