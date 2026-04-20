import pandas as pd
import numpy as np
import time
import sqlite3
import matplotlib.pyplot as plt


np.random.seed(42)
size = 1_000_000  

df = pd.DataFrame({
    "timestamp": pd.date_range("2024-01-01", periods=size, freq="min"),
    "consumption_kwh": np.random.rand(size) * 10,
    "voltage": np.random.rand(size) * 240,
    "current": np.random.rand(size) * 20
})

def measure_write(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    return time.time() - start


def measure_read(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    return time.time() - start
results = {
    "format": [],
    "write_time": [],
    "read_time": []
}

csv_file = "data.csv"

t_write = measure_write(df.to_csv, csv_file, index=False)
t_read = measure_read(pd.read_csv, csv_file)

results["format"].append("CSV")
results["write_time"].append(t_write)
results["read_time"].append(t_read)


parquet_file = "data.parquet"

t_write = measure_write(df.to_parquet, parquet_file, index=False)
t_read = measure_read(pd.read_parquet, parquet_file)

results["format"].append("Parquet")
results["write_time"].append(t_write)
results["read_time"].append(t_read)


hdf_file = "data.h5"

t_write = measure_write(df.to_hdf, hdf_file, key="data", mode="w")
t_read = measure_read(pd.read_hdf, hdf_file, "data")

results["format"].append("HDF5")
results["write_time"].append(t_write)
results["read_time"].append(t_read)


db_file = "data.db"

def write_sql():
    conn = sqlite3.connect(db_file)
    df.to_sql("energy", conn, if_exists="replace", index=False)
    conn.close()

def read_sql():
    conn = sqlite3.connect(db_file)
    pd.read_sql("SELECT * FROM energy", conn)
    conn.close()

t_write = measure_write(write_sql)
t_read = measure_read(read_sql)

results["format"].append("SQL")
results["write_time"].append(t_write)
results["read_time"].append(t_read)


res_df = pd.DataFrame(results)
print(res_df)


plt.figure(figsize=(10,5))

x = np.arange(len(res_df["format"]))

plt.bar(x - 0.2, res_df["write_time"], width=0.4, label="Write time")
plt.bar(x + 0.2, res_df["read_time"], width=0.4, label="Read time")

plt.xticks(x, res_df["format"])
plt.ylabel("Time (seconds)")
plt.title("Comparison of data storage formats performance")
plt.legend()
plt.show()
