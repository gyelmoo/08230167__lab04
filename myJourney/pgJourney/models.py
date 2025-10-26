from django.db import models

class LearningJourney(models.Model):  # Changed from learningJourney to LearningJourney
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    interests = models.TextField()

    def __str__(self):
        return self.name