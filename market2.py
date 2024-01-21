"""
Create a market simulation using OOP(object-oriented programming) principles.

This market simulation has 10 companies, and will have one of them win at the end of 10 years. 
The winner out of these companies is the one that generates the highest revenue after 10 years of operations. 

The average yearly growth rate in sales for these companies is 10% annually given no bad/positive events occur.

Each company should start with a random revenue, ranging from $10,000,000 to $20,000,000

Every month tick (1 month = 1 iteration) there are certain odds for events occuring. (120 total iterations)


Some of the global events are as follows:

Supply chain disruption - 10% decrease in revenue for all companies for the year. (1% chance of happening monthly) (can occur 10 times total)
Currency depreciation - 5% decrease in revenue for all companies for half a year. (2% chance of happening monthly) (can occur 20 times total)
Economic growth - 10% increase in revenue for all companies for two years. (1% chance of happening monthly) (can occur 5 times total)
More capital circulating - 15% increase in revenue for all companies for the year. (0.5% chance of happening monthly) (can occur 10 times total)
Improved international relations - 10% increase in revenue for all companies for the year. (0.5% chance of happening monthly) (can occur 10 times total)
(in total 5% reserved for global events)


Some of the individual events are as follows:  

Great PR campaign - 70% increase in revenue growth for that year. (1% chance of happening monthly) 
Bad PR campaign - 30% decrease in revenue growth for that year. (1.5% chance of happening monthly) 
Great investment - $1,500,000 added to revenue. (0.5% chance of happening monthly)
Bad investment - $2,000,000 removed from revenue. (0.5% chance of happening monthly)
Production problems - 20% decrease in total revenue for two years. (1% chance of happening monthly) 
New competitor enters market - 15% decrease in total revenue for three years. (0.3% chance of happening monthly) 
Rapid growth in demand - 30% increase in total revenue for two years. (2% chance of happening monthly) 
Raised capital - $1,000,000 added to revenue. (0.5% chance of happening monthly)
Debt repayment called in - $500,000 removed from revenue. (0.5% chance of happening monthly)
(in total 7.8% reserved for individual events)

The global events can only occur once during its effect duration.
E.g. Supply chain disruptions can only occur once every year, currency depreciation once every half a year.

These events should show up in the console monthly, alongside each company's revenue.
P.S. remember that this will become a graph later
"""

from typing import List 
import random
import plotly.express as px
import pandas as pd


COMPANY_NAMES = ['Pear', 'Macrohard', 'Tony', 'Samsings', 'Sahara', 'McRonald', 'Hotdog Monarch', 'Thneed Inc', 'Moria Mining', 'Isengard Logging']

#event type 1 = direct
#event type 2 = modifier

#events
GLOBAL_EVENTS = {
    'Supply chain disruptions': {
        'effect': 0.90,
        'chance': 0.01,
        'type': 2,
        'cooldown': 12,
    },
    'Currency depreciation': {
        'effect': 0.95,
        'chance': 0.02,
        'type': 2,
        'cooldown': 6,
    },
    'Economic growth': {
        'effect': 1.10,
        'chance': 0.01,
        'type': 2,
        'cooldown': 24,
    },
    'More capital circulating': {
        'effect': 1.15,
        'chance': 0.005,
        'type': 2,
        'cooldown': 12,
    },
    'Improved international relations': {
        'effect': 1.10,
        'chance': 0.005,
        'type': 2,
        'cooldown': 12,
    },
}

INDIVIDUAL_EVENTS = {
    'Great PR campaign': {
        'effect': 1.70,
        'chance': 0.01,
        'type': 2,
        #'cooldown': ,
    },
    'Bad PR campaign': {
        'effect': 0.70,
        'chance': 0.015,
        'type': 2,
        #'cooldown': ,
    },
    'Great investment': {
        'effect': 1500000,
        'chance': 0.005,
        'type': 1,
        #'cooldown': ,
    },
    'Bad investment': {
        'effect': -2000000,
        'chance': 0.005,
        'type': 1,
        #'cooldown': ,
    },
    'Production problems': {
        'effect': 0.80,
        'chance': 0.01,
        'type': 2,
        #'cooldown': ,
    },
    'New competitor enters market': {
        'effect': 0.85,
        'chance': 0.003,
        'type': 2,
        #'cooldown': ,
    },
    'Rapid growth in demand': {
        'effect': 1.30,
        'chance': 0.02,
        'type': 2,
        #'cooldown': ,
    },
    'Raised capital': {
        'effect': 1000000,
        'chance': 0.005,
        'type': 1,
        #'cooldown': ,
    },
    'Debt repayment called in': {
        'effect': -500000,
        'chance': 0.005,
        'type': 1,
        #'cooldown': ,
    },
}

#make le object
class Company:
    def __init__(self, name: str):
        self.name = name
        self.funds = random.randint(10000000, 20000000)
        self.growth_modifier = 1.0083
    def accountant(self):
        return self.funds * self.growth_modifier

class Event:
    def __init__(self, name: str, effect: float, chance: float, event_type: int, cooldown: int):
        self.name = name
        self.effect = effect
        self.chance = chance
        self.event_type = event_type
        self.cooldown = cooldown
        self.cooldown_flag = 0
    def direct_effect(self, c: Company):
        return c.funds + self.effect
    def modifier_effect(self, c: Company):
        return c.growth_modifier * self.effect
    def tick(self) -> bool:
        return random.random() <= self.chance
    def cooldown_check(self):
        return a >= self.cooldown_flag

# Setup phase
companies: List[Company] = []
global_events: List[Event] = []
individual_events: List[Event] = []

while True:
    try:
        user_input = int(input('Please provide the length of the simulation in months: '))
        break
    except ValueError:
        print('Provided length must be a whole number')
    


results = {
    'Month': [x + 1 for x in range(user_input)],
    **{d: [] for d in COMPANY_NAMES},
}

#make le dictionary into le object
for name in COMPANY_NAMES:
    companies.append(Company(name))

for global_event in GLOBAL_EVENTS:
    global_events.append(Event(global_event, GLOBAL_EVENTS[global_event]['effect'], GLOBAL_EVENTS[global_event]['chance'], GLOBAL_EVENTS[global_event]['type'], GLOBAL_EVENTS[global_event]['cooldown']))
    
for individual_event in INDIVIDUAL_EVENTS:
    individual_events.append(Event(individual_event, INDIVIDUAL_EVENTS[individual_event]['effect'], INDIVIDUAL_EVENTS[individual_event]['chance'], INDIVIDUAL_EVENTS[individual_event]['type'], 1))
    
#months
for a in range(user_input):
    for b in range(len(global_events)):
        global_tick = global_events[b].tick() #wanna save these values for printing later

        for c in companies: 
            for d in range(len(companies)):
                if global_tick == True and global_events[b].cooldown_check() == False: 
                    continue

                else:
                    if global_tick == True:
                        print(f'{global_events[b].name}, {global_events[b].effect}, {companies[d].name}, {companies[d].funds}')
                        if global_events[b].event_type == 1: 
                            companies[d].funds = global_events[b].direct_effect(c)
                        else:
                            companies[d].growth_modifier = global_events[b].modifier_effect(c)
                        global_events[b].cooldown_flag = a + global_events[b].cooldown
                    #print(f'{companies[d].funds}')
                    else:
                        continue

            for e in range(len(individual_events)):
                for f in range(len(companies)):
                    individual_tick = individual_events[e].tick() #wanna save these values for printing later

                    if individual_tick == True:
                        print(f'{individual_events[e].name}, {individual_events[e].effect}, {companies[f].name}, {companies[f].funds}')
                        if individual_events[e].event_type == 1:
                            companies[f].funds = individual_events[e].direct_effect(c) 
                        else:
                            companies[f].growth_modifier = individual_events[e].modifier_effect(c)
                        #print(f'{companies[f].funds}')
                    else:
                        continue

    for g in range(len(companies)):
        companies[g].funds = companies[g].accountant()
        results[companies[g].name].append(companies[g].funds)

        print('{}, {:,.2f}'.format(companies[g].name, companies[g].funds)) #print events names and effects + company funds at the end
    print('--------------------------------')

winner = companies[0]
for h in range(len(companies)):
    if companies[h].funds > winner.funds:
        winner.name = companies[h].name
        winner.funds = companies[h].funds
    else:
        continue

df = pd.DataFrame(results)
fig = px.line(df, x = df['Month'], y = df.columns[1:])

print('The company {} has amassed a fortune of {:,.2f} and triumphed over all other companies'.format(winner.name, winner.funds))
fig.show()