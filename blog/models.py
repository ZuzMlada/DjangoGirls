from django.db import models
from django.utils import timezone


class Post(models.Model): #class Post ma tieto vlastnosti, objekt je Model
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) #foreign key - odkazujeme na tabulku pouzivatelov
    title = models.CharField(max_length=200)
    text = models.TextField() #velky text v DB
    created_date = models.DateTimeField(   #cas, kedy sme ho vytvorili
            default=timezone.now)
    published_date = models.DateTimeField(  #datum publikovania
            blank=True, null=True)

    def publish(self): #metoda published - ulozi nam datum publikovania
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title #ked zavolame self, vrati text (title)
