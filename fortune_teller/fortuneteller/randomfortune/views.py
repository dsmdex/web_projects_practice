from django.shortcuts import render
import random

# Create your views here.
def get_greeting():
    greet = random.choice(greetingList)
    return greet

def get_fortune():
    fortune = random.choice(fortuneList)
    return fortune

def fortune_view(request):
    context = {
        'greet': get_greeting(),
        'fortune': get_fortune()
    }
    return render(request, 'randomfortune/fortune.html', context)

fortuneList = [
    "Do not be afraid of competition.",
    "An exciting opportunity lies ahead of you.",
    "You love peace.",
    "Get your mind set…confidence will lead you on.",
    "You will always be surrounded by true friends.",
    "Sell your ideas-they have exceptional merit.",
    "You should be able to undertake and complete anything."
]

greetingList = [
    "Hello!", 
    "Hi there!", 
    "Good morning!", 
    "Good afternoon!", 
    "Good evening!", 
    "Hey!", 
    "Howdy!", 
    "Greetings!", 
    "What's up?", 
    "Yo!", 
    "Welcome!", 
    "Nice to see you!", 
    "Hey there!", 
    "Hiya!", 
    "Salutations!"
]

def test_view(request):
    return render(request, 'randomfortune/test.html')

def test_two_view(request):
    return render(request, 'randomfortune/test_two.html')