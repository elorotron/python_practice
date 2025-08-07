letter_1 = "t"
letter_2 = "w"
print(letter_1 > letter_2)
print(ord(letter_1), ord(letter_2))
print(chr(116), chr(119))
print("a" > "A")  # True, потому что код “a” больше

# Если вы хотите сравнивать строки без учёта регистра, сначала приведите их к одному регистру:

text_1 = "Привет"
text_2 = "привет"
print(text_1.lower() == text_2.lower())  # True
