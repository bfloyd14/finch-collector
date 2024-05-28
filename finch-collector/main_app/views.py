from django.shortcuts import render

# Add the Cat class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lola', 'Shitzu', 'Kinda sassy and is down for a good treat.', 7),
  Dog('Sasha', 'Border Collie', 'great nose and cuddler.', 10),
  Dog('Moe', 'Pitt-Bull Mix', 'short legs but nice teeth.', 9),
  Dog('Joy', 'Shepard Mix', 'Alpha, she just wants to play frisbee.', 11),
  Dog('George', 'Dobermann Pincher', 'loves to lay in bed', 12)
]

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  return render(request, 'dogs/index.html', {'dogs': dogs})