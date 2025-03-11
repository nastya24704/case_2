#Фунция спроса и предложения товара заданны уравнениями Qd=300- P
# Qs= P/2 - 30. Государство установило налог в размере 15 д.ед за единицу товара
# Налог уплачивает покупатель. Определите параметры начального равновесия
# Равновесия после налога, изменение выигрышей покупателей и продавцов
# Налоговые поступления и чистые потери общества ( задача 1.26)
#Вводим значения коэффицентов


import local as lcl


def demand(price, a, b):
    '''
    Функция описывающая величину спроса
    :param Price: Цена товара
    :param a:
    :param b:
    :return: Quantity_demand
    '''
    Quantity_demand= a - b*price
    return Quantity_demand


def supply(price, c, d):
    '''
    Функция описывающая величину предложения
    :param Price: Цена товара
    :param c:
    :param d:
    :return: Quantity_supply
    '''
    Quantity_supply = c - d * price
    return Quantity_supply


a = float(input("total_addressable_market"))
b = float(input("slope_of_the_demand"))
c = float(input("intersection_point_of_the_supply"))
d = float(input("slope_of_the_supply"))
t = float(input("tax_rate"))


#Находим начальное равновесие на рынке
equilibrium_price = (a - c) / (d + b)
equilibrium_quantity = demand(equilibrium_price, a, b)


#Находим цену покупателя и продавца после введения налога
price_supply = (c - a + b * t) / (- b - d)
price_demand = price_supply + t
quantity_1 = demand(price_demand,a,b)


#Находим изменение объемов продаж и цен
changing_quantity = quantity_1 - equilibrium_quantity
changing_price = price_supply - equilibrium_price

#Находим начальные, изменённые выигрыши и их изменение
consumer_surplus_0= 1/2 * (a - equilibrium_price) * equilibrium_quantity
consumer_surplus_1= 1/2 * (a - price_demand) * quantity_1

if c<0:
   producer_surplus_0 = 1 / 2 * (equilibrium_price + c / d) * equilibrium_quantity
   producer_surplus_1 = 1 / 2 * (price_demand + c / d) * quantity_1
else:
    producer_surplus_0 = (c + equilibrium_quantity)/2 * equilibrium_price
    producer_surplus_1 = (c + quantity_1) / 2 * price_supply

changing_consumer_surplus= consumer_surplus_1 - consumer_surplus_0
changing_producer_surplus= producer_surplus_1 - producer_surplus_0


#Находим Налоговые поступления и чистые потери общества
tax_burden_consumer= (price_demand - equilibrium_price) * quantity_1
tax_burden_producer= (equilibrium_price - price_supply) * quantity_1
tax_revenue = quantity_1 * t
deadweight_loss= -(price_demand - price_supply) * (equilibrium_quantity - quantity_1) * 1/2

def main():
 print("answer")
 print("initial_equilibrium_quantity", equilibrium_quantity)
 print("initial_equilibrium_price", equilibrium_price)
 print("new_equilibrium_quantity", quantity_1)
 print("new_produser_price", price_supply)
 print("new_consumer_price", price_demand)
 print("changing_of_the_quantity", changing_quantity)
 print("changing_of_the_price", changing_price)
 print("consumer_surplus_before_tax", consumer_surplus_0)
 print("consumer_surplus_after_tax", consumer_surplus_1)
 print("changing_of_the_consumer_surplus", changing_consumer_surplus)
 print("producer_surplus_before_tax", producer_surplus_0)
 print("producer_surplus_after_tax", producer_surplus_1)
 print("changing_of_the_producer_surplus", changing_producer_surplus)
 print("tax_burden_of_consumer", tax_burden_consumer)
 print("tax_burden_of_producer", tax_burden_producer)
 print("tax_revenue", tax_revenue)
 print("deadweight_loss", deadweight_loss)


if __name__ == '__main__':
    main()
