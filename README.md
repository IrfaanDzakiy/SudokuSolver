# Sudoku Solver


## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.


## Spesifikasi

#### Spesifikasi untuk program yang dibuat :
| No | Spesifikasi Program | Jenis |
| ---- | ---- | ---- |
| 1 | Program dibuat dalam bahasa Python | Wajib |
| 2 | Program menerima input berupa file eksternal yang berisi matriks area permainan (disediakan pada repository) dengan lambang '#' yang menandai area belum diketahui nomornya | Wajib |
| 3 | Program melengkapi area-area yang nomornya belum diketahui, strategi dan heuristik yang digunakan dibebaskan dan menjadi salah satu komponen penilaian. **Pencarian solusi harus dibuat sendiri algoritmanya**. | Wajib |
| 4 | Tuliskan hasil dari sepesifikasi (3) pada command prompt/terminal dan simpan dalam file eksternal. Buatlah agar mudah dibaca | Wajib |
| 5 | Tuliskan semua koordinat dari area bernomor 5, tuliskan pada command prompt/terminal dan simpan pada file eksternal yang sama dengan spesifikasi nomor (4). Koordinat dituliskan setelah area permainan | Wajib |
| 6 | Program dapat membaca inputan dari gambar. **Program hanya perlu dapat membaca gambar spesifik yang ada pada repository**. Library yang digunakan dibebaskan dan tidak ada batasan. | Bonus |
| 7 | Program diletakkan pada directory src, kemudian file pengujian diletakkan pada directory test, dan hasil pengujian berupa screenshot diletakkan pada directory result | Wajib |
| 8 | Program dikejakan secara individu, Anda boleh mencari referensi dari manapun namun tidak diperkenankan bekerja sama | Wajib |

#### Edit file readme setelah fork repository ini sehingga mencakup :
| No | Spesifikasi |
| ---- | ---- |
| 1 | Cara penggunaan program, seperti cara untuk kompilasi serta command yang dapat diterima program |
| 2 | Strategi pencarian solusi yang digunakan dan alasan penggunaannya secara lengkap, termasuk kompleksitas algoritmanya | 
| 3 | Apabila mengerjakan bonus, tuliskan library yang digunakan serta alasan penggunaannya dan kelebihan serta kekurangnnya menurut Anda |
| 4 | Tuliskan referensi (berupa link atau judul buku beserta halamannya) yang membantu Anda dalam mengerjakan tugas ini |


## Komponen Penilaian 
| No | Komponen |
| ---- | ---- |
| 1 | Kebenaran program dan fungsionalitasnya |
| 2 | Algoritma yang digunakan beserta alasan penggunaannya | 
| 3 | AKerapihan kode dan struktur repository |
| 4 | Kejelasan dan kerapihan readme |


## Pengumpulan
Lakukan merge request hasil fork Anda ke repository ini, informasi selanjutnya mengenai demo akan diberitahukan oleh asisten.


pip install pytesseract

https://github.com/UB-Mannheim/tesseract/wiki


## Pembuat
Name : M. Irfaan Dzakiy
<br/>
NIM : 13518145

## Cara Penggunaan Program
0. Pastikan sudah menginstall library PIL, pytesseract dan pastikan tesseract terinstall pada komputer anda. Installer tesseract bisa diunduh disini https://github.com/UB-Mannheim/tesseract/wiki. Jangan lupa untuk menambahkan tesseract ke PATH komputer anda.

```
pip install PIL
pip install pytesseract
```

1. Pergi ke directory src, lalu run dengan command

```
py Main.py
```

## Strategi Pencarian Solusi
Setelah saya melakukan riset dengan bantuan mbah gugel, saya menemukan beberapa pendekatan untuk memecahkan problem sudoku, yaitu Backtracking, Stochastic Search, Constraint Programming, dan Exact Cover. Saya memutuskan untuk menggunakan pendekatan Backtracking karena algoritma tersebut sudah pernah diajarkan sebelumnya pada matakuliah Strategi Algoritma, sehingga saya merasa percaya diri untuk membuat implementasi program dengan menggunakan pendekatan tersebut. Untuk kompleksitas dari algoritma adalah O(n³).

## Bonus
Untuk mengerjakan bonus, yaitu bisa menerima input file sudoku berupa gambar, saya menggunakan library tesseract. Alasannya adalah library ini sangat memudahkan saya dalam memproses karakter-karakter yang ada pada suatu gambar, pada kasus ini adalah gambar sudoku, menjadi sebuah string yang lebih mudah untuk diproses lebih lanjut. Namun kekurangan dari library ini adalah diperlukannya pre-processing pada gambar agar bisa menghasilkan string yang merepresentasikan isi sudoku dengan benar. Salah satu kasus yang kerap saya temui adalah kotak yang menyimpan suatu angka pada sudoku kerap mengubah hasil yang diberikan oleh tesseract, walaupun garis tersebut hanya memiliki ketebalan 1 pixel. Proses trial n error yang harus dilakukan untuk mendapatkan hasil cropping yang sesuai sangatlah merepotkan.

## Referensi
https://en.wikipedia.org/wiki/Sudoku_solving_algorithms

https://github.com/UB-Mannheim/tesseract/wiki

https://www.geeksforgeeks.org/sudoku-backtracking-7/

