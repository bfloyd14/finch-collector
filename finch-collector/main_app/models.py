from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
  ('B', 'Breakfast'),
  ('D', 'Dinner'),
  ('T', 'Treat')
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)


  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("toy-detail", kwargs={"pk": self.id})


class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  gender = models.CharField(max_length=6)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("dog-detail", kwargs={"dog_id": self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
  
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices = MEALS,
    default = MEALS[0][0]
  ) 
  
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_meal_display()} on {self.date}'
  
  class Meta:
    ordering = ['date']


  
  