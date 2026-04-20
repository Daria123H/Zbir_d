import pandas as pd
import matplotlib.pyplot as plt

notebook = pd.read_excel(r"d:\Збір даних\Пр6\notebook.xls")
microwave = pd.read_excel(r"d:\Збір даних\Пр6\microwave.xls")
fridge = pd.read_excel(r"d:\Збір даних\Пр6\fridge.xls")

mean_notebook = notebook["Absolute field (µT)"].mean()
mean_microwave = microwave["Absolute field (µT)"].mean()
mean_fridge = fridge["Absolute field (µT)"].mean()

print("Середні значення:")
print("Ноутбук:", mean_notebook)
print("Мікрохвильовка:", mean_microwave)
print("Холодильник:", mean_fridge)

plt.figure()

plt.plot(notebook["Time (s)"], notebook["Absolute field (µT)"], label="Ноутбук")
plt.plot(microwave["Time (s)"], microwave["Absolute field (µT)"], label="Мікрохвильовка")
plt.plot(fridge["Time (s)"], fridge["Absolute field (µT)"], label="Холодильник")

plt.xlabel("Час (с)")
plt.ylabel("Магнітне поле (µT)")
plt.title("Залежність магнітного поля від часу")
plt.legend()
plt.grid()

plt.show()

devices = ["Ноутбук", "Мікрохвильовка", "Холодильник"]
means = [mean_notebook, mean_microwave, mean_fridge]

plt.figure()
plt.bar(devices, means)

plt.title("Порівняння магнітного поля пристроїв")
plt.ylabel("Середнє значення (µT)")
plt.xlabel("Пристрої")

plt.show()
