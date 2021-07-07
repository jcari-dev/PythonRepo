import random

capital_dic= {
        'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne' 
}



def game():

  w = 0

  l = 0

  count = 0

  norepeats = []

  while count != len(capital_dic):

    
    
    states = random.choice(list(capital_dic.items()))
    
    if states[0] not in norepeats:
      print('not found in norepeats')

      norepeats.append(states[0])
      question = input(f"What's the capital of {states[0]}? ").lower()

      if question == states[1].lower():
        count += 1;
        w += 1;
        print(f'correct! You currently have {w} wins')

        
      elif question != states[1].lower():
        count += 1;
        l += 1;
        print(f'wrong! the answer is {states[1]}, you currently have {l} losses')
      
    else:

      print('found in norepeats')

      states = random.choice(list(capital_dic.items()))
    
  if count == len(capital_dic):
    again = input('Do you want to play again? (Y/N)').lower()

    if again == "y":
      game()
    elif again == "n":
      print('Sounds good :)')

game()
