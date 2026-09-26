import multiprocessing as mp
import time

def hitung_kuadrat(n, hasil_queue):
    time.sleep(0.1)  # simulasi kerja
    hasil_queue.put(n * n)

if __name__ == "__main__":
    q = mp.Queue()
    proses = [mp.Process(target=hitung_kuadrat, args=(i, q)) for i in range(5)]

    for p in proses:
        p.start()
    for p in proses:
        p.join()

    hasil = [q.get() for _ in range(5)]
    print("Hasil kuadrat (urutan bisa acak, tergantung proses mana selesai duluan):", sorted(hasil))