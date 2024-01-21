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

#make le object
class Company:
    def __init__(self, name: str):
        self.name = name
        self.funds = random.randint(10000000, 20000000)
        self.growth_modifier = 1.0083
    def accountant(self):
        return self.funds * self.growth_modifier

# Setup phase
companies: List[Company] = []

#make le dictionary into le object
for name in COMPANY_NAMES:
    companies.append(Company(name))

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

#months
for a in range(user_input):
    for b in range(len(companies)):
        companies[b].funds = companies[b].funds * random.uniform(0.9, 1.2)
        results[companies[b].name].append(companies[b].funds)
        print('{}, {:,.2f}'.format(companies[b].name, companies[b].funds))
    print('--------------------------------')

winner = companies[0]
for c in range(len(companies)):
    if companies[c].funds > winner.funds:
        winner.name = companies[c].name
        winner.funds = companies[c].funds
    else:
        continue

df = pd.DataFrame(results)
fig = px.line(df, x = df['Month'], y = df.columns[1:])

print('The company {} has amassed a fortune of {:,.2f} and triumphed over all other companies'.format(winner.name, winner.funds))
fig.show()