# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:48:13 2022

@author: Charles_Truscott
runfile('C:/Users/Charles_Truscott/Desktop/recipe.py', wdir='C:/Users/Charles_Truscott/Desktop')
Milk		Cost: $14.0 AUD	Cost per unit: $3.5 AUD

Milk		Cost: $11.9 USD	Cost per unit: $2.98 USD

Bread		Cost: $3.8 AUD	Cost per unit: $3.8 AUD

Bread		Cost: $3.23 USD	Cost per unit: $3.23 USD

Butter		Cost: $16.5 AUD	Cost per unit: $5.5 AUD

Butter		Cost: $14.02 USD	Cost per unit: $4.68 USD

Eggs		Cost: $7.5 AUD	Cost per unit: $7.5 AUD

Eggs		Cost: $6.38 USD	Cost per unit: $6.38 USD

Cheese		Cost: $12.5 AUD	Cost per unit: $6.25 AUD

Cheese		Cost: $10.62 USD	Cost per unit: $5.31 USD

Raw Sugar		Cost: $2.5 AUD	Cost per unit: $2.5 AUD

Raw Sugar		Cost: $2.12 USD	Cost per unit: $2.12 USD

T-Bone Steak		Cost: $66.0 AUD	Cost per unit: $16.5 AUD

T-Bone Steak		Cost: $56.1 USD	Cost per unit: $14.02 USD

Diced Beef		Cost: $26.0 AUD	Cost per unit: $13.0 AUD

Diced Beef		Cost: $22.1 USD	Cost per unit: $11.05 USD

Tea		Cost: $25.0 AUD	Cost per unit: $6.25 AUD

Tea		Cost: $21.25 USD	Cost per unit: $5.31 USD

Coffee		Cost: $26.0 AUD	Cost per unit: $26.0 AUD

Coffee		Cost: $22.1 USD	Cost per unit: $22.1 USD


"""
import numpy
rough_AUD_to_USD_conversion_factor_market_value = 0.85
shopping_list = {"Milk": [14.00, 4], "Bread": [3.80, 1], "Butter": [16.50, 3], "Eggs": [7.50, 1], "Cheese": [12.50, 2], "Raw Sugar": [2.50, 1],
                 "T-Bone Steak": [66.0, 4], "Diced Beef": [26.00, 2], "Tea": [25.00, 4], "Coffee": [26.00, 1]
                 }

for key in shopping_list:
    print(key + "\t\t" + "Cost: $" + str(shopping_list[key][0] ) + " AUD\t" + "Cost per unit: $" + str(float(shopping_list[key][0] / shopping_list[key][1])) + " AUD\n")
    print(key + "\t\t" + "Cost: $" + str(numpy.round((shopping_list[key][0] * rough_AUD_to_USD_conversion_factor_market_value), 2)) + " USD\t" + "Cost per unit: $" + str(float(numpy.round((shopping_list[key][0] / shopping_list[key][1]) * rough_AUD_to_USD_conversion_factor_market_value, 2))) + " USD\n")
    