import pandas as pd
import matplotlib.pyplot as plt
#---------------Кривая диограмма---------------------
week = pd.Series({'Понедельник': 90, 'Вторник': 76, 'Среда': 51, 'Четверг': 39, 'Пятница': 23, 'Суббота': 66, 'Воскреснье': 100})
plt.title('график энергии в течении недели')
plt.plot(week)
plt.show()
#-------------Круговая диограмма-----------------------
name = pd.Series({'Freddy': 33, 'Bonny': 27, 'Foxy': 50})
plt.pie(name, labels=name.index)
plt.show()