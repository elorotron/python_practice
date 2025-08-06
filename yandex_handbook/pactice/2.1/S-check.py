product_name = input()
product_price = int(input())
product_weight = int(input())
customer_money = int(input())

product_final_price = product_price * product_weight

sdacha = customer_money - product_final_price

print(f"{"Чек":=^35}")
print(f"Товар:{product_name:>29}")
example = f"{product_weight}кг * {product_price}руб/кг"
print(f"Цена:{example:>30}")
print(f"Итого:{product_final_price:>26}руб")
print(f"Внесено:{customer_money:>24}руб")
print(f"Сдача:{sdacha:>26}руб")
print(f"{"":=^35}")
