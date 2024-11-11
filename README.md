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
| Louis Ferdyo Gunawan  | 18222022       |  1. Membuat steepest |
                        |                |  2. Membuat visualisasi 2d |
                        |                |  3.Melakukan eksperimen & analisis pada hasil eksperimen |
                        |                |  4. Membuat kesimpulan |                        |
| Erwan Poltak Halomoan | 18222028       |              |
| Hartanto Luwis        | 18222064       |  1. Membuat fungsi-fungsi dasar spt makeCube, random, dst	|
                        |                |  2. Membuat Simulated Annealing |
                        |                |  3. Membuat Genetic Algorithm |
                        |                |  4. Membuat detail fungsi dan penjelasannya di laporan |
                        |                |  5. Membuat kesimpulan n saran |
| Ammar Naufal          | 18222066       |              |
