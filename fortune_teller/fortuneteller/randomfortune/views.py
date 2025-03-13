from django.shortcuts import render
import random

# Create your views here.
def fortune(request):
    fortune = random.choice(fortuneList)
    context = {
        'fortune': fortune
    }
    return render(request, 'randomfortune/fortune.html', context)

fortuneList = [
    "Do not be afraid of competition.",
    "An exciting opportunity lies ahead of you.",
    "You love peace.",
    "Get your mind set…confidence will lead you on.",
    "You will always be surrounded by true friends.",
    "Sell your ideas-they have exceptional merit.",
    "You should be able to undertake and complete anything.",
    "You are kind and friendly.",
    "You are wise beyond your years.",
    "Your ability to juggle many tasks will take you far.",
    "A routine task will turn into an enchanting adventure.",
    "Beware of all enterprises that require new clothes.",
    "Be true to your work, your word, and your friend.",
    "Goodness is the only investment that never fails.",
    "Forget injuries; never forget kindnesses.",
    "Respect yourself and others will respect you.",
    "It is easier to stay out than to get out.",
    "Sing every day and chase the mean blues away.",
    "You will receive money from an unexpected source.",
    "Plan for many pleasures ahead.",
    "Experience is the best teacher.",
    "You will be happy with your spouse.",
    "Expect the unexpected.",
    "Stay healthy. Walk a mile.",
    "The family that plays together stays together.",
    "Eat chocolate to have a sweeter life.",
    "Make yourself necessary to someone.",
    "The only way to have a friend is to be one.",
    "Nothing great was ever achieved without enthusiasm.",
    "Dance as if no one is watching.",
    "Live this day as if it were your last.",
    "Your life will be happy and peaceful.",
    "Reach for joy and all else will follow.",
    "Move in the direction of your dreams.",
    "Bloom where you are planted.",
    "Appreciate. Appreciate. Appreciate.",
    "Happy news is on its way."
]
