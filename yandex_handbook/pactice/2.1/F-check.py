# Для этого напишите программу, которая рассчитывает стоимость покупки и печатает чек в заданном формате.
# Итоговая стоимость вычисляется как произведение цены за килограмм и веса товара. Гарантируется, что у покупателя достаточно денег для покупки.


product_name = input()
product_price = int(input())
product_weight = int(input())
customer_money = int(input())

product_final_price = product_price * product_weight

sdacha = customer_money - product_final_price

print(f"""Чек
{product_name} - {product_weight}кг - {product_price}руб/кг
Итого: {product_final_price}руб
Внесено: {customer_money}руб
Сдача: {sdacha}руб""")