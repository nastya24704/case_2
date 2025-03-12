# Part of a case-study #2: Microeconomics
# Developers: Lagoda K., Pinoeva K., Zheravina N., Mozhitseva M.


import local as lcl


def demand(price, a, b):
    """Function describing the quantity of supply.

    :param price: price of the product
    :param a: demand cutoff price
    :param b: tangent of the angle of inclination
    :return: quantity_demand
    """
    quantity_demand = a - b * price
    return quantity_demand


def supply(price, c, d):
    """Function describing the quantity of supply.

    :param price: price of the product
    :param c: minimum supply
    :param d: tangent of the angle of inclination
    :return: quantity_supply
    """
    quantity_supply = c - d * price
    return quantity_supply


a = float(input(f"{lcl.TOTAL_ADDRESSABLE_MARKET}:"))
b = float(input(f"{lcl.SLOPE_OF_THE_DEMAND}:"))
c = float(input(f"{lcl.INTERSECTION_POINT_OF_THE_SUPPLY}:"))
d = float(input(f"{lcl.SLOPE_OF_THE_SUPPLY}:"))
t = float(input(f"{lcl.TAX_RATE}:"))
# We enter the values ​​of the function coefficients


equilibrium_price = (a - c) / (d + b)
equilibrium_quantity = demand(equilibrium_price, a, b)
# Finding the initial equilibrium in the market.


price_supply = (c - a + b * t) / (-b - d)
price_demand = price_supply + t
quantity_1 = demand(price_demand, a, b)
#We find the price of the consumer and producer after the tax.


changing_quantity = quantity_1 - equilibrium_quantity
changing_price = price_supply - equilibrium_price
# We find changing in quantity and price.


consumer_surplus_0 = 1 / 2 * (a - equilibrium_price) * equilibrium_quantity
consumer_surplus_1 = 1 / 2 * (a - price_demand) * quantity_1

if c < 0:
    producer_surplus_0 = 1 / 2 * (equilibrium_price +
                                  c / d) * equilibrium_quantity
    producer_surplus_1 = 1 / 2 * (price_demand + c / d) * quantity_1
else:
    producer_surplus_0 = (c + equilibrium_quantity) / 2 * equilibrium_price
    producer_surplus_1 = (c + quantity_1) / 2 * price_supply

changing_consumer_s = consumer_surplus_1 - consumer_surplus_0
changing_producer_s = producer_surplus_1 - producer_surplus_0
# We find the initial, new surpluses and their changing.


tax_burden_consumer = (price_demand - equilibrium_price) * quantity_1
tax_burden_producer = (equilibrium_price - price_supply) * quantity_1
tax_revenue = quantity_1 * t
deadweight_loss = -(price_demand - price_supply) * (equilibrium_quantity -
                                                    quantity_1) * 1 / 2
# We find tax revenues and deadweight loss.


def main():
    
    """Function that outputs all answers.
    :return: None
    """
    print(f"{lcl.ANSWER}:", )
    print(f"{lcl.INITIAL_EQUILIBRIUM_QUANTITY}: {equilibrium_quantity},")
    print(f"{lcl.INITIAL_EQUILIBRIUM_PRICE}: {equilibrium_price},")
    print(f"{lcl.NEW_EQUILIBRIUM_QUANTITY}: {quantity_1},")
    print(f"{lcl.NEW_PRODUCER_PRICE}: {price_supply},")
    print(f"{lcl.NEW_CONSUMER_PRICE}: {price_demand},")
    print(f"{lcl.CHANGING_OF_THE_QUANTITY}: {changing_quantity},")
    print(f"{lcl.CHANGING_OF_THE_PRICE}: {changing_price},")
    print(f"{lcl.CONSUMER_SURPLUS_BEFORE_TAX}: {consumer_surplus_0},")
    print(f"{lcl.CONSUMER_SURPLUS_AFTER_TAX}: {consumer_surplus_1},")
    print(f"{lcl.CHANGING_OF_THE_CONSUMER_SURPLUS}:{changing_consumer_s}")
    print(f"{lcl.PRODUCER_SURPLUS_BEFORE_TAX}: {producer_surplus_0},")
    print(f"{lcl.PRODUCER_SURPLUS_AFTER_TAX}: {producer_surplus_1},")
    print(f"{lcl.CHANGING_OF_THE_PRODUCER_SURPLUS}: {changing_producer_s},")
    print(f"{lcl.TAX_BURDEN_OF_CONSUMER}: {tax_burden_consumer},")
    print(f"{lcl.TAX_BURDEN_OF_PRODUCER}: {tax_burden_producer},")
    print(f"{lcl.TAX_REVENUE}: {tax_revenue},")
    print(f"{lcl.DEADWEIGHT_LOSS}: {deadweight_loss}.")


if __name__ == '__main__':
    main()
    
