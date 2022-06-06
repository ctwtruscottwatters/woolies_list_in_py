# -*- coding: utf-8 -*-
"""
runfile('C:/Users/Charles_Truscott/Desktop/recipe.py', wdir='C:/Users/Charles_Truscott/Desktop')
Milk
			Cost: $14.0 AUD	Cost per unit: $3.5 AUD	Qty: 4.0

			Cost: $11.9 USD	Cost per unit: $2.98 USD	Qty: 4.0

Bread
			Cost: $3.8 AUD	Cost per unit: $3.8 AUD	Qty: 1.0

			Cost: $3.23 USD	Cost per unit: $3.23 USD	Qty: 1.0

Butter
			Cost: $16.5 AUD	Cost per unit: $5.5 AUD	Qty: 3.0

			Cost: $14.02 USD	Cost per unit: $4.68 USD	Qty: 3.0

Eggs
			Cost: $7.5 AUD	Cost per unit: $7.5 AUD	Qty: 1.0

			Cost: $6.38 USD	Cost per unit: $6.38 USD	Qty: 1.0

Cheese
			Cost: $12.5 AUD	Cost per unit: $6.25 AUD	Qty: 2.0

			Cost: $10.62 USD	Cost per unit: $5.31 USD	Qty: 2.0

Raw Sugar
			Cost: $2.5 AUD	Cost per unit: $2.5 AUD	Qty: 1.0

			Cost: $2.12 USD	Cost per unit: $2.12 USD	Qty: 1.0

T-Bone Steak
			Cost: $66.0 AUD	Cost per unit: $16.5 AUD	Qty: 4.0

			Cost: $56.1 USD	Cost per unit: $14.02 USD	Qty: 4.0

Diced Beef
			Cost: $26.0 AUD	Cost per unit: $13.0 AUD	Qty: 2.0

			Cost: $22.1 USD	Cost per unit: $11.05 USD	Qty: 2.0

Madura Tea
			Cost: $25.0 AUD	Cost per unit: $6.25 AUD	Qty: 4.0

			Cost: $21.25 USD	Cost per unit: $5.31 USD	Qty: 4.0

Moccona Coffee
			Cost: $26.0 AUD	Cost per unit: $26.0 AUD	Qty: 1.0

			Cost: $22.1 USD	Cost per unit: $22.1 USD	Qty: 1.0

Total cost in AUD: 199.8 		 Total cost in USD: 169.83



"""
"""
Actual measurements taken in PSI, grams, kilograms, items (objects) or litres
"""
import numpy
rough_AUD_to_USD_conversion_factor_market_value = 0.85
cost_in_AUD = 0
cost_in_USD = 0

shopping_list = {"Milk": [14.00, 4], "Bread": [3.80, 1], "Butter": [16.50, 3], "Eggs": [7.50, 1], "Cheese": [12.50, 2], "Raw Sugar": [2.50, 1],
                 "T-Bone Steak": [66.0, 4], "Diced Beef": [26.00, 2], "Madura Tea": [25.00, 4], "Moccona Coffee": [26.00, 1]
                 }

for key in shopping_list:
    cost_in_AUD += shopping_list[key][0]
    cost_in_USD += shopping_list[key][0] * rough_AUD_to_USD_conversion_factor_market_value
    print(key + "\n\t\t\t" + "Cost: $" + str(shopping_list[key][0] ) + " AUD\t" + "Cost per unit: $" + str(float(shopping_list[key][0] / shopping_list[key][1])) + " AUD\t" + "Qty: " + str(float(shopping_list[key][1])), end = "\n\n")
    print("\t\t\t" + "Cost: $" + str(numpy.round((shopping_list[key][0] * rough_AUD_to_USD_conversion_factor_market_value), 2)) + " USD\t" + "Cost per unit: $" + str(float(numpy.round((shopping_list[key][0] / shopping_list[key][1]) * rough_AUD_to_USD_conversion_factor_market_value, 2))) + " USD\t" + "Qty: " + str(float(shopping_list[key][1])), end = "\n\n")
print("Total cost in AUD: {} \t\t Total cost in USD: {}".format(cost_in_AUD, numpy.round(cost_in_USD, 2)))