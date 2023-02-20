import pandas as pd
drinks = {
    "Latte": [2.15, 2.45],
    "Flavoured latte - Vanilla": [2.55, 2.85],
    "Flavoured latte - Caramel": [2.55, 2.85],
    "Flavoured latte - Hazelnut": [2.55, 2.85],
    "Flavoured latte - Gingerbread": [2.55, 2.85],
    "Cappuccino": [2.15, 2.45],
    "Americano": [1.95, 2.25],
    "Flat white": [2.15, 2.45],
    "Cortado": [2.05, 2.35],
    "Mocha": [2.30, 2.70],
    "Espresso": [1.50, 1.80],
    "Filter coffee": [1.50, 1.80],
    "Chai latte": [2.30, 2.60],
    "Hot chocolate": [2.20, 2.90],
    "Flavoured hot chocolate - Caramel": [2.60, 2.90],
    "Flavoured hot chocolate - Hazelnut": [2.60, 2.90],
    "Flavoured hot chocolate - Vanilla": [2.60, 2.90],
    "Luxury hot chocolate": [2.40, 2.70],
    "Red Label tea": [1.20, 1.80],
    "Speciality Tea - Earl Grey": [1.30, 1.60],
    "Speciality Tea - Green": [1.30, 1.60],
    "Speciality Tea - Camomile": [1.30, 1.60],
    "Speciality Tea - Peppermint": [1.30, 1.60],
    "Speciality Tea - Fruit": [1.30, 1.60],
    "Speciality Tea - Darjeeling": [1.30, 1.60],
    "Speciality Tea - English breakfast": [1.30, 1.60],
    "Iced latte": [2.35, 2.85],
    "Flavoured iced latte - Vanilla": [2.75, 3.25],
    "Flavoured iced latte - Caramel": [2.75, 3.25],
    "Flavoured iced latte - Hazelnut": [2.75, 3.25],
    "Iced americano": [2.15, 2.50],
    "Frappes - Chocolate Cookie": [2.75, 3.25],
    "Frappes - Strawberries & Cream": [2.75, 3.25],
    "Frappes - Coffee": [2.75, 3.25],
    "Smoothies - Carrot Kick": [2.00, 2.50],
    "Smoothies - Berry Beautiful": [2.00, 2.50],
    "Smoothies - Glowing Greens": [2.00, 2.50],
    "Hot Chocolate": [1.40, 1.70],
    "Glass of milk": [0.70, 1.10]
}
new_drinks = {}
for key, value in drinks.items():
    regular = value[0]
    large = value[1]
    new_drinks[f"Regular {key}"] = regular
    new_drinks[f"Large {key}"] = large



drinks_list = []
for keys, values in new_drinks.items():
    item = f"{keys} - {values:.2f}"
    drinks_list.append(item)


