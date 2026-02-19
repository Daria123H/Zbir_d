import pandas as pd

df = pd.read_csv(r"D:\Збір даних\Пр1\PR1.csv")

total_rows = len(df)

missing_share = df.isnull().sum().sum() / (df.shape[0] * df.shape[1])

price_numeric = pd.to_numeric(df["price"], errors="coerce")
non_numeric_price_share = price_numeric.isnull().sum() / total_rows

date_parsed = pd.to_datetime(df["date"], errors="coerce")
invalid_date_share = date_parsed.isnull().sum() / total_rows

duplicates_share = df.duplicated().sum() / total_rows

quality_index = 1 - (
    missing_share +
    non_numeric_price_share +
    invalid_date_share +
    duplicates_share
) / 4

print("Частка пропусків:", round(missing_share, 3))
print("Частка нечислових цін:", round(non_numeric_price_share, 3))
print("Частка некоректних дат:", round(invalid_date_share, 3))
print("Частка дублікатів:", round(duplicates_share, 3))
print("Індекс якості скрейпінгу:", round(quality_index, 3))