1. Ubah ukuran buffer menjadi 3
    mengubah empty = semaphore (5) menjadi empty = semaphore (3)
2. Amati perubahan blocking:
    produsen tidak bisa mengisi terus buffer jika konsumen lebih lambat dalam megambil barang, ini mencegah terjadinya overflow. sebaliknya jika buffer kosong, konsumen akan blocked di full.acquire(), untuk mencegah underflow.
3. Bandingkan mutex vs semaphore secara konseptual 
    MUTEX digunakan untuk proteksi, sedangkan SEMAPHORE digunakan untuk penjadwalan atau sinkronisasi.