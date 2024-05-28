from django.shortcuts import render

# Add the Cat class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

old_dogs = [
  Dog('Lola', 'tan with a hint of silver', 'Kinda sassy and is down for a good treat.', 7),
  Dog('Sasha', 'blue merl', 'great nose and cuddler.', 10),
  Dog('Moe', 'tan', 'short legs but nice teeth.', 9),
  Dog('Joy', 'black and tan merl', 'Alpha, she just wants to play frisbee.', 11),
  Dog('George', 'white', 'loves to lay in bed', 12)
]

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  return render(request, {'old dogs': old_dogs})