import pandas as pd
import numpy as np


data = {
    'Продукт': ['Ноутбук', 'Смартфон', 'Планшет', 'Наушники', 'Смартфон', 'Ноутбук'],
    'Цена': [45000, 25000, 20000, 5000, 30000, 50000],
    'Количество': [10, 25, 15, 50, 20, 8],
    'Категория': ['Электроника', 'Электроника', 'Электроника', 
                  'Аксессуары', 'Электроника', 'Электроника']
}


df = pd.DataFrame(data)


print("Базовная информация о наборе данных:")
print(df.info())

print("\nОписательная статистика по числовым столбцам:")
print(df.describe())


print("\nСуммарная стоимость продаж по категориям:")
sales_by_category = df.groupby('Категория').apply(lambda x: (x['Цена'] * x['Количество']).sum())
print(sales_by_category)


df['Выручка'] = df['Цена'] * df['Количество']
top_products = df.groupby('Продукт')['Выручка'].sum().nlargest(3)
print("\nТоп-3 продукта по выручке:")
print(top_products)


output_file = 'sales_analysis.csv'
df.to_csv(output_file, index=False)
print(f"\nРезультаты сохранены в файл: {output_file}")