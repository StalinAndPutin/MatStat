from matplotlib import pyplot as plt
from read_data import read_data
import numpy as np

def emp_fn():
    # Чтение данных
    data = read_data()

    # Разделение данных по столбцам
    sepal_length = np.array([x.Sepal.Length for x in data])
    sepal_width = np.array([x.Sepal.Width for x in data])
    species = np.array([x.Species for x in data])

    # Вычисление площади чашелистика
    sepal_area = sepal_length * sepal_width

    # Функция для построения ЭФР
    def ecdf(data):
        """Вычисляет эмпирическую функцию распределения."""
        x = np.sort(data)
        y = np.arange(1, len(data) + 1) / len(data)
        return x, y

    # Разделение данных по видам
    setosa_area = sepal_area[species == "setosa"]
    versicolor_area = sepal_area[species == "versicolor"]
    virginica_area = sepal_area[species == "virginica"]

    # Вычисление ЭФР для каждого вида
    x_setosa, y_setosa = ecdf(setosa_area)
    x_versicolor, y_versicolor = ecdf(versicolor_area)
    x_virginica, y_virginica = ecdf(virginica_area)
    x_all_area_species, y_all_area_species = ecdf(sepal_area)

    # Создание сетки графиков
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # График 1: Эмпирическая функция распределения
    axes[0].step(x_setosa, y_setosa, label="Setosa", where="post")
    axes[0].step(x_versicolor, y_versicolor, label="Versicolor", where="post")
    axes[0].step(x_virginica, y_virginica, label="Virginica", where="post")
    axes[0].step(x_all_area_species, y_all_area_species, label="All", where="post")
    axes[0].set_title("Эмпирическая функция распределения площади чашелистика")
    axes[0].set_xlabel("Площадь чашелистика (Sepal.Length × Sepal.Width)")
    axes[0].set_ylabel("F(x)")
    axes[0].legend()
    axes[0].grid(True)

    # График 2: Гистограмма
    axes[1].hist(x_setosa, alpha=0.2, label="Setosa")
    axes[1].hist(x_versicolor, alpha=0.2, label="Versicolor")
    axes[1].hist(x_virginica, alpha=0.2, label="Virginica")
    axes[1].hist(x_all_area_species, alpha=0.2, label="All")
    axes[1].set_title("Гистограмма распределения площади чашелистика")
    axes[1].set_xlabel("Площадь чашелистика (Sepal.Length × Sepal.Width)")
    axes[1].legend()
    axes[1].grid(True)

    # График 3: Box-plot
    data = [x_setosa, x_versicolor, x_virginica, x_all_area_species]
    axes[2].boxplot(data, labels=["Setosa", "Versicolor", "Virginica", "All"])
    for i, d in enumerate(data):
        x = np.random.normal(i + 1, 0.04, size=len(d))
        axes[2].scatter(x, d, color='black', alpha=0.5)
    axes[2].set_title("Box-plot распределения площади чашелистика")
    axes[2].set_xlabel("Площадь чашелистика (Sepal.Length × Sepal.Width)")
    axes[2].grid(True)

    # Отображение всех графиков
    plt.tight_layout()
    plt.show()