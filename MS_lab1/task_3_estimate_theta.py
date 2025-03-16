import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("iris.csv", delimiter=",", quotechar='"')

df["Sepal.Area"] = df["Sepal.Length"] * df["Sepal.Width"]

theta_0 = df["Sepal.Area"].mean()
print(theta_0)
n_values = [5, 10, 50, 100, 150]
M = 1000

theta_hats = {}

# Генерация выборок на основе данных
for n in n_values:
    estimates = []
    for _ in range(M):
        sample = df["Sepal.Area"].sample(n, replace=True)
        theta_hat = sample.mean()
        estimates.append(theta_hat)
    theta_hats[n] = estimates

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for ax in axes:
    ax.axvline(theta_0, color='red', linestyle='dashed', label=r'$\theta_0$')

# Гистограммы оценок
for n, estimates in theta_hats.items():
    sns.histplot(estimates, kde=True, label=f"n={n}", ax=axes[0])
axes[0].legend()
axes[0].set_title("Гистограмма оценок θ")
axes[0].set_xlabel("Оценка θ")
axes[0].set_ylabel("Частота")

# Box-plot оценок
sns.boxplot(data=[theta_hats[n] for n in n_values], ax=axes[1])
axes[1].set_xticks(range(len(n_values)))
axes[1].set_xticklabels(n_values)
axes[1].set_title("Box-plot оценок θ")
axes[1].set_xlabel("Объем выборки n")
axes[1].set_ylabel("Оценка θ")

# Violin-plot оценок
sns.violinplot(data=[theta_hats[n] for n in n_values], ax=axes[2])
axes[2].set_xticks(range(len(n_values)))
axes[2].set_xticklabels(n_values)
axes[2].set_title("Violin-plot оценок θ")
axes[2].set_xlabel("Объем выборки n")
axes[2].set_ylabel("Оценка θ")

plt.show()
