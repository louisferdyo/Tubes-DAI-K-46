# Tugas Besar 1 IF3070 Dasar Inteligensi Artifisial : Pencarian Solusi Diagonal Magic Cube dengan Local Search

## Deskripsi Singkat
Diagonal magic cube merupakan kubus yang tersusun dari angka 1 hingga n3 tanpa pengulangan dengan n adalah panjang sisi pada kubus tersebut. Angka-angka pada tersusun sedemikian rupa sehingga properti-properti berikut terpenuhi:
- Terdapat satu angka yang merupakan magic number dari kubus tersebut (Magic number tidak harus termasuk dalam rentang 1 hingga n3, magic number juga bukan termasuk ke dalam angka yang harus dimasukkan ke dalam kubus)
- Jumlah angka-angka untuk setiap baris sama dengan magic number
- Jumlah angka-angka untuk setiap kolom sama dengan magic number
- Jumlah angka-angka untuk setiap tiang sama dengan magic number
- Jumlah angka-angka untuk seluruh diagonal ruang pada kubus sama dengan magic number
- Jumlah angka-angka untuk seluruh diagonal pada suatu potongan bidang dari kubus sama dengan magic number

Algoritma local search yang kami gunakan untuk mencari solusi diagonal magic cube:  
1. Steepest Ascent
2. Stochastic
3. Random Restart
4. Sideways Move
5. Genetic Algorithm
6. Simulated Annealing

- Bahasa pemograman yang digunakan untuk pembuatan algoritma local search kami adalah python, 
- visualisasi plot menggunakan matplotlib, 
- visualisasi kubus menggunakan plotly, 
- library math & numpy untuk kalkulasi perhitungan

## Cara menjalankan
1. Clone repo ini dengan mengetikkan command " git clone https://github.com/louisferdyo/Tubes-DAI-K-46"
2. pindah ke folder 'src'
3. Jalankan program main.py dengan cara "python main.py"
4. pilih algoritma yang ingin dicoba untuk menyelesaikan pencarian solusi diagonal magic cube

## Dokumentasi
Di dalam folder 'doc', terdapat sebuah file .pdf yang menjelaskan deskripsi, persoalan, hasil eksperimen, analisis, pembahasan, juga kesimpulan berupa algoritma terbaik menurut kami.

## Pembagian Tugas
| NAMA                  | NIM            | TUGAS                           |
|-----------------------|----------------|---------------------------------|
| Louis Ferdyo Gunawan  | 18222022       |  Membuat steepest, visualisasi 2d, bagian eksperimen, analisis, kesimpulan pada laporan, |
| Erwan Poltak Halomoan | 18222028       |  visualisasi 3d, Membuat Stochastic, Melakukan debug code, testing dan laporan bagian Genetic Algorithm |
| Hartanto Luwis        | 18222064       |  Membuat fungsi-fungsi dasar (makeCube, random, ..), Simulated Annealing, Genetic Algorithm, detail fungsi pada laporan, kesimpulan dan saran pada laporan	|
| Ammar Naufal          | 18222066       | Membuat Sideways Move, Membuat Random Restart, Membuat laporan bagian hasil eksperimen, merapikan laporan, melakukan debug dan revisi typography kode |
