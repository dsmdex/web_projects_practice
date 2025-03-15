from django.shortcuts import render

def home(request):
  # The context is all of the variables we want passed into the template.
  context = {"attractions" : attractions}
  return render(request, 'state_attractions/home.html', context)

def details(request, statename):
  # We replace the dash with a space for later ease of use. The dash is there because of the slugify filter.
  context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
  return render(request, 'state_attractions/details.html', context)

# This is the dictionary for all the attractions
attractions = [
  { 'attraction_name': 'Niagara Falls', 'state': 'New York' },
  { 'attraction_name': 'Grand Canyon National Park', 'state': 'Arizona' },
  { 'attraction_name': 'Mall of America', 'state': 'Minnesota' },
  { 'attraction_name': 'Mount Rushmore', 'state': 'South Dakota' },
  { 'attraction_name': 'Times Square', 'state': 'New York' },
  { 'attraction_name': 'Walt Disney World', 'state': 'Florida' },
  { 'attraction_name': 'Yellowstone National Park', 'state': 'Wyoming' },
  { 'attraction_name': 'Statue of Liberty', 'state': 'New York' },
  { 'attraction_name': 'Golden Gate Bridge', 'state': 'California' },
  { 'attraction_name': 'The Alamo', 'state': 'Texas' },
  { 'attraction_name': 'Hollywood Walk of Fame', 'state': 'California' },
  { 'attraction_name': 'Las Vegas Strip', 'state': 'Nevada' },
  { 'attraction_name': 'Great Smoky Mountains National Park', 'state': 'Tennessee' },
  { 'attraction_name': 'The White House', 'state': 'Washington, D.C.' },
  { 'attraction_name': 'Rock and Roll Hall of Fame', 'state': 'Ohio' },
  { 'attraction_name': 'French Quarter', 'state': 'Louisiana' },
  { 'attraction_name': 'Mount St. Helens', 'state': 'Washington' },
  { 'attraction_name': 'Liberty Bell', 'state': 'Pennsylvania' },
  { 'attraction_name': 'Empire State Building', 'state': 'New York' },
  { 'attraction_name': 'Denali National Park', 'state': 'Alaska' },
  { 'attraction_name': 'Space Needle', 'state': 'Washington' },
  { 'attraction_name': 'Gateway Arch', 'state': 'Missouri' },
  { 'attraction_name': 'Yosemite National Park', 'state': 'California' },
  { 'attraction_name': 'Mount Vernon', 'state': 'Virginia' },
  { 'attraction_name': 'Pike Place Market', 'state': 'Washington' },
  { 'attraction_name': 'Hersheypark', 'state': 'Pennsylvania' },
  { 'attraction_name': 'Bourbon Street', 'state': 'Louisiana' },
  { 'attraction_name': 'The Bean (Cloud Gate)', 'state': 'Illinois' },
  { 'attraction_name': 'Central Park', 'state': 'New York' }
]