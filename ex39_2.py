states = { 'Oregon' : 'OR' ,
          'Florida' : 'FL' ,
          'California' : 'CA'}
cities = { 'OR' : 'Portland' }
cities['CA'] = 'San Francisco'
cities['FL'] = 'Jacksonville'

print('-' *10)
print(f"Cali has {cities['CA']}")
print(f"OR has {cities['OR']}")

print('-' * 10)

print(f"Florida abbreviation is {states['Florida']}")

print('-' * 10)

print(f"OR has ", cities[states['Oregon']])
print(f"Florida has {cities[states['Florida']]}")

print('-' * 10)

#for state, abbrev in list(states.items()):
for state, abbrev in states.items():
    print(f'{state} is abbreviated {abbrev} ')
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')
    print(f"And has {cities[abbrev]}")

print('-' * 10)

state = states.get('Texas' )

print(state)

if not state:
    print('No Texas here bro')

state1 = states.get('Turtle', 'Huh? What was that again?')

print(state1)
