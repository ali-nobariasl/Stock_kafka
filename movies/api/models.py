from django.db import models




class Dicrector(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    def __str__(self):
        return self.name + ' ' + self.surname
    

class Movie(models.Model):
    title = models.CharField(max_length=40)
    year = models.IntegerField(default=2000)
    director = models.ForeignKey(Dicrector, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.title
    




