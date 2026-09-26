import multiprocessing as mp
import os
import time

def tampilkan_pid(nama):
    # Mencetak Process ID (PID) untuk membuktikan setiap worker adalah proses OS terpisah
    print(f"[{nama}] berjalan di PID: {os.getpid()}")

print(f"[Main] berjalan di PID: {os.getpid()}")

proses = [mp.Process(target=tampilkan_pid, args=(f"Worker-{i}",)) for i in range(3)]
for p in proses:
    p.start()
for p in proses:
    p.join()