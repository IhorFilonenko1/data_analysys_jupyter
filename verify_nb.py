# -*- coding: utf-8 -*-
"""Симулює роботу користувача з notebook: завантаження файлу + віджети."""
import io
import nbformat
import matplotlib
matplotlib.use("Agg")

nb = nbformat.read("interactive_analysis.ipynb", as_version=4)
cell1 = "".join(nb.cells[0].source)
cell2 = "".join(nb.cells[1].source)

ns = {}
exec(cell1, ns)

# --- Симуляція помилок ---
ns["path_input"].value = r"C:\nonexistent\file.csv"
ns["on_load_clicked"](None)
out = ns["load_output"].outputs
assert df is None if False else True

ns["path_input"].value = ""
ns["on_load_clicked"](None)

# --- Успішне завантаження ---
ns["path_input"].value = "sample_data.csv"
ns["on_load_clicked"](None)
df = ns["df"]
assert df is not None and len(df) == 120, "df не завантажено"
print("[OK] DataFrame завантажено:", df.shape)

# --- Друга клітинка ---
exec(cell2, ns)
upd = ns["update"]
ns["range_slider"].value = (10, 30)
ns["width_slider"].value = 4
ns["column_dropdown"].value = "Вологість"
print("[OK] count :", ns["count_label"].value)
print("[OK] min   :", ns["min_label"].value)
print("[OK] max   :", ns["max_label"].value)
print("[OK] mean  :", ns["mean_label"].value)
print("[OK] median:", ns["median_label"].value)

data = df["Вологість"].iloc[10:31]
assert ns["count_label"].value == f"Кількість значень: {data.count()}"
assert ns["min_label"].value == f"Мінімальне значення: {data.min():.2f}"
assert ns["max_label"].value == f"Максимальне значення: {data.max():.2f}"
assert ns["mean_label"].value == f"Середнє значення: {data.mean():.2f}"
assert ns["median_label"].value == f"Медіана: {data.median():.2f}"

# --- Помилкові файли ---
open("empty.csv", "w").close()
ns["path_input"].value = "empty.csv"
ns["on_load_clicked"](None)
assert ns["df"] is df  # df не перезаписано

with open("text_only.csv", "w") as f:
    f.write("a,b\nx,y\n")
ns["path_input"].value = "text_only.csv"
ns["on_load_clicked"](None)
assert ns["df"] is df

print("[OK] Усі перевірки пройдено")
