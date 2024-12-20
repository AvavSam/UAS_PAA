import random
import time
import matplotlib.pyplot as plt

# Fungsi untuk mengecek apakah elemen dalam array unik atau tidak
def is_unique(arr):
    return len(arr) == len(set(arr))

# Fungsi untuk menghitung waktu eksekusi (worst case dan average case)
def measure_execution_time(arr):
    start_time = time.perf_counter()
    is_unique(arr)  # Average case
    average_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    # Worst case: Array dengan semua elemen sama
    is_unique([arr[0]] * len(arr))
    worst_time = time.perf_counter() - start_time

    return average_time, worst_time

# Konfigurasi
n_values = [100, 150, 200, 250, 300, 350, 400, 500]
max_value = 230
seed = 42

# Menyimpan hasil
average_times = []
worst_times = []

# Generate array dan hitung waktu eksekusi
random.seed(seed)
for n in n_values:
    arr = [random.randint(0, max_value) for _ in range(n)]
    avg_time, worst_time = measure_execution_time(arr)
    average_times.append(avg_time)
    worst_times.append(worst_time)

# Plot hasil
plt.figure(figsize=(10, 6))
plt.plot(n_values, average_times, marker='o', label='Average Case')
plt.plot(n_values, worst_times, marker='o', label='Worst Case')

plt.title('Comparison of Execution Times for Unique Element Check')
plt.xlabel('Array Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid()
plt.show()
