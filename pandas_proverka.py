import pandas as pd

print(pd.Series(['первый', 'второй', 'третий', 'четвертый', 'пятый'])) # создание таблицы из объектов и индексов
print(pd.Series({'aboba1': 'первый', 'aboba2': 'второй', 'aboba3': 'третий'})) #создание таблицы с произвольными индексами
print(pd.DataFrame({'aboba1':[1,2], 'aboba2':[3,4], 'aboba3':[5,6]})) #cоздание двумерной или большей таблицы
