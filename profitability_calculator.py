import webbrowser

fixed_costs=input  ("What are the company's fixed costs? ")
costs_of_production=input  ("What is the cost of producing one product? ")
price=input  ("What's the price of the product? ")
profit_on_productse=(int(price)-int(costs_of_production))
print("The profit on one product is: ", profit_on_productse)
how_much_to_earn=int(fixed_costs)//int(profit_on_productse)
print("You have to sell a product so many times not to lose: " ,how_much_to_earn)

print("profitability_calculator made by lytezo on GitHub")
webbrowser.open("https://github.com/lytezo")

