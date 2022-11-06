import pandas as pd
import matplotlib.pyplot as plt

DIR = "../AnalysisData/"

data = pd.read_csv(f"{DIR}tb_ana.csv", sep=';')

data_group = data.groupby(["iso2"]).new_sp.sum().reset_index()
print("Suma zakażeń występujących w danym kraju świata")
print(data_group)

data_group2 = data_group.loc[(data_group['iso2'] == 'PL') | (data_group['iso2'] == 'GE') | (data_group['iso2'] == 'CZ')
                             | (data_group['iso2'] == 'SK') | (data_group['iso2'] == 'UA') | (
                                         data_group['iso2'] == 'BY')
                             | (data_group['iso2'] == 'LT')]
print(data_group2)

plt.figure(figsize=(30, 30))
data_group2.plot.bar(x="iso2", y="new_sp")
plt.rcParams.update({'font.size': 12})
plt.grid()
plt.title("Liczba odnotowanych przypadków zakażenia\n gruźlicą w Polsce i krajach sąsiadujących ")
plt.show()

data_group3 = data.loc[(data['iso2'] == 'PL')]
print(data_group3)

plt.figure(figsize=(30, 30))
data_group3.plot.bar(x="year", y="new_sp")
plt.rcParams.update({'font.size': 12})
plt.grid()
plt.title("Liczba odnotowanych przypadków zakażenia\n gruźlicą w Polsce w danych latach")
plt.show()

fig, axs = plt.subplots(2)
data_group3.plot.bar(x="year", y="f_cases", color='red', ax=axs[0])
axs[0].grid()
axs[0].set_ylim(0, 5000)
axs[0].axes.get_xaxis().set_ticklabels([])
data_group3.plot.bar(x="year", y="m_cases", ax=axs[1])
plt.rcParams.update({'font.size': 12})
axs[1].grid()
fig.suptitle("Liczba odnotowanych przypadków zakażenia\n gruźlicą w Polsce w danych latach podzielone między płciami")
plt.show()


