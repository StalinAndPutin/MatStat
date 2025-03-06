from matplotlib import pyplot as plt
from read_data import read_data


def emp_fn():
    import numpy as np
    import matplotlib.pyplot as plt

    import numpy as np
    import matplotlib.pyplot as plt

    # Полные данные из вашего первого сообщения (150 записей)
    data =read_data()

    # Разделение данных по столбцам
    sepal_length = np.array([x.Sepal.Length for x in data])
    sepal_width = np.array([x.Sepal.Width for x in data])
    petal_length = np.array([x.Petal.Length for x in data])
    petal_width = np.array([x.Petal.Width for x in data])
    species = np.array([x.Species for x in data])

    # Вычисление площади чашелистика
    sepal_area = sepal_length * sepal_width

    print(sepal_area)

    # Функция для построения ЭФР
    def ecdf(data):
        """Вычисляет эмпирическую функцию распределения."""
        x = np.sort(data)
        y = np.arange(1, len(data) + 1) / len(data)
        print(x)
        # print(y)
        return x, y

    # Разделение данных по видам
    setosa_area = sepal_area[species == "setosa"]
    versicolor_area = sepal_area[species == "versicolor"]
    virginica_area = sepal_area[species == "virginica"]
    # all_species = sepal_area[species == "setosa" or species == "versicolor" or species == "virginica" ]
    # Вычисление ЭФР для каждого вида
    x_setosa, y_setosa = ecdf(setosa_area)
    x_versicolor, y_versicolor = ecdf(versicolor_area)
    x_virginica, y_virginica = ecdf(virginica_area)
    x_all_area_species, y_all_area_species = ecdf(sepal_area)

    # Построение графиков
    plt.figure(figsize=(10, 6))
    plt.step(x_setosa, y_setosa, label="Setosa", where="post")
    plt.step(x_versicolor, y_versicolor, label="Versicolor", where="post")
    plt.step(x_virginica, y_virginica, label="Virginica", where="post")
    plt.step(x_all_area_species, y_all_area_species, label="All", where="post")
    # Настройки графика
    plt.title("Эмпирическая функция распределения площади чашелистика")
    plt.xlabel("Площадь чашелистика (Sepal.Length × Sepal.Width)")
    plt.ylabel("F(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Построение графиков
    plt.hist(x_setosa, alpha=0.2, label="Setosa")
    plt.hist(x_versicolor, alpha=0.2, label="Versicolor")
    plt.hist(x_virginica, alpha=0.2, label="Virginica")
    plt.hist(x_all_area_species, alpha=0.2, label="All")
    plt.title("Гистограмма распределения площади чашелистика")
    plt.xlabel("Площадь чашелистика (Sepal.Length × Sepal.Width)")
    plt.legend()
    plt.grid(True)
    plt.show()


    data = [x_setosa, x_versicolor, x_virginica, x_all_area_species]
    plt.boxplot([x_setosa, x_versicolor, x_virginica, x_all_area_species], labels=["Setosa", "Versicolor", "Virginica", "All"])
    for i, d in enumerate(data):
        # Генерация координат X для точек данных
        x = np.random.normal(i + 1, 0.04, size=len(d))  # i + 1 — позиция box plot
        plt.scatter(x, d, color='black', alpha=0.5)
    plt.title("Box-plot распределения площади чашелистика")
    plt.xlabel("Площадь чашелистика (Sepal.Length × Sepal.Width)")
    plt.grid(True)
    plt.show()
