from django.db import models


class Word(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return (self.title)


class Definition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='definitions')
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return (self.text)