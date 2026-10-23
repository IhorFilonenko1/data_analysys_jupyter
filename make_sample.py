# -*- coding: utf-8 -*-
"""Генерує sample_data.csv для перевірки notebook."""
import numpy as np
import pandas as pd

n = 120
x = np.arange(n)
rng = np.random.default_rng(42)

df = pd.DataFrame({
    "Температура": np.round(20 + 8 * np.sin(x / 12) + rng.normal(0, 0.5, n), 2),
    "Вологість": np.round(55 + 15 * np.cos(x / 15) + rng.normal(0, 1.0, n), 2),
    "Тиск": np.round(1013 + 5 * np.sin(x / 20) + rng.normal(0, 0.3, n), 2),
})
df.to_csv("sample_data.csv", index=False, encoding="utf-8-sig")
print(df.head())
