# NGL Spammer 🚀 [BETA]

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Sebuah script Python sederhana dan cepat untuk mengirimkan pesan anonim dalam jumlah banyak ke akun NGL.link target. Didesain untuk kemudahan penggunaan di terminal, baik di PC maupun Termux.

> [!WARNING]
> **Peringatan Penting:** Tool ini dibuat hanya untuk tujuan edukasi dan eksperimen. Penggunaan yang tidak bertanggung jawab dapat melanggar kebijakan layanan NGL.link dan berpotensi menyebabkan pemblokiran akun. Penulis tidak bertanggung jawab atas penyalahgunaan atau konsekuensi yang timbul dari penggunaan script ini. Gunakan dengan bijak dan risiko ditanggung sendiri.

---

## ✨ Fitur Utama

* 🚀 **Spam Cepat:** Mengirimkan pesan dalam jumlah yang ditentukan dengan efisien.
* 📜 **Dukungan File Pesan:** Mengambil daftar pesan dari `questions.txt` atau bisa langsung dari input.
* 💻 **Cross-Platform:** Kompatibel dengan lingkungan Linux, Windows, dan Termux.
* ⚙️ **Pengaturan Mudah:** Cukup masukkan username NGL dan jumlah pesan.

---

## 📸 Screenshots

Berikut adalah tampilan saat script dijalankan di terminal:

http://googleusercontent.com/image_generation_content/0

 

---

## 🛠️ Instalasi

Pastikan kamu sudah menginstall **Git** dan **Python 3.x** di sistem kamu.

### Untuk Windows (CMD/PowerShell)

1.  **Install Python:**
    Jika belum punya, unduh dan install Python dari [situs resminya](https://www.python.org/downloads/). Pastikan untuk mencentang "Add Python to PATH" saat instalasi.

2.  **Clone Repository:**
    Buka Command Prompt atau PowerShell, lalu jalankan perintah berikut:
    ```bash
    git clone [https://github.com/freefirerizky12345-afk/ngl-spammer.git](https://github.com/freefirerizky12345-afk/ngl-spammer.git)
    ```

3.  **Masuk ke Direktori:**
    ```bash
    cd ngl-spammer
    ```

4.  **Install Modul Python:**
    ```bash
    pip install requests
    ```

### Untuk Termux (Android)

1.  **Update dan Install Dependencies:**
    Buka Termux, lalu jalankan perintah ini untuk menginstal `git` dan `python`:
    ```bash
    pkg update && pkg upgrade -y
    pkg install git python -y
    ```

2.  **Clone Repository:**
    ```bash
    git clone [https://github.com/freefirerizky12345-afk/ngl-spammer.git](https://github.com/freefirerizky12345-afk/ngl-spammer.git)
    ```

3.  **Masuk ke Direktori:**
    ```bash
    cd ngl-spammer
    ```

4.  **Install Modul Python:**
    ```bash
    pip install requests
    ```

---

## ⚙️ Cara Menggunakan

1.  **(Opsional) Sesuaikan Pesan:**
    Buka file `questions.txt` dengan editor teks (misal: Notepad di Windows, `nano` di Termux). Setiap baris di file ini akan dianggap sebagai satu pesan yang akan dikirim. Kamu bisa menambahkan atau mengubah pesan sesuai keinginanmu.

2.  **Jalankan Script:**
    Di dalam direktori `ngl-spammer`, jalankan script menggunakan perintah:
    ```bash
    python ngl_spam.py
    ```

3.  **Ikuti Petunjuk:**
    Script akan meminta kamu untuk memasukkan:
    * **Username NGL:** Masukkan username target NGL.link (misal: `nama_teman`).
    * **Jumlah Pesan:** Masukkan berapa banyak pesan yang ingin kamu kirim (misal: `100`).

4.  **Selesai!** Script akan mulai mengirimkan pesan dan menampilkan statusnya di konsol.

---

## 💡 Tips

* Untuk menghentikan script, tekan `Ctrl + C` di terminal.
* Jika kamu sering menggunakan tool ini, pastikan untuk `git pull` secara berkala untuk mendapatkan update terbaru.

---

## 🤝 Kontribusi

Saran, perbaikan *bug*, atau penambahan fitur baru sangat diterima!
1.  Fork repository ini.
2.  Buat branch baru (`git checkout -b feature/AmazingFeature`).
3.  Commit perubahanmu (`git commit -m 'Add some AmazingFeature'`).
4.  Push ke branch (`git push origin feature/AmazingFeature`).
5.  Buka Pull Request.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
```

---

### 2. Penjelasan Tambahan & Cara Mengunggah Screenshot

* **Badge:** `[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)](https://www.python.org/)` ini adalah contoh *badge* yang menunjukkan versi Python dan bisa mengarah ke link Python. Kamu bisa mencari *badge* lain di situs seperti [shields.io](https://shields.io/).
* **Screenshot:**
    * `![NGL Spammer Screenshot](URL_GAMBAR_ANDA_DI_SINI)` adalah format untuk menampilkan gambar.
    * **Untuk mengupload gambar kamu agar bisa tampil di GitHub:**
        1.  Kamu bisa upload gambar kamu ke repositori GitHub kamu. Buat folder baru bernama `images` (atau `screenshots`).
        2.  Upload file gambar `.png` atau `.jpg` kamu ke folder tersebut.
        3.  Setelah diupload, klik pada gambar tersebut di GitHub.
        4.  Kemudian, klik kanan pada gambar yang muncul dan pilih **"Copy image address"** atau **"Salin alamat gambar"**.
        5.  `URL_GAMBAR_ANDA_DI_SINI` ini ganti dengan alamat gambar yang kamu salin tadi.
        6.  **Alternatif praktis:** Gunakan *screenshot* yang saya *generate* untuk kamu di atas. Tinggal *copy* URL-nya dan ganti di `![NGL Spammer Screenshot](URL_GAMBAR_ANDA_DI_SINI)`.

### 3. Langkah-langkah Penerapan

1.  **Salin Teks:** Salin semua kode Markdown yang saya berikan di atas.
2.  **Edit `README.md`:** Buka repositori kamu di GitHub. Klik pada file `README.md`, lalu klik ikon pensil (edit).
3.  **Paste:** Hapus semua konten lama dan paste teks yang baru.
4.  **Upload Screenshot:** Jika kamu ingin menggunakan *screenshot* buatanmu sendiri, upload ke GitHub seperti dijelaskan di atas, lalu ganti URL gambar di `![NGL Spammer Screenshot](URL_GAMBAR_ANDA_DI_SINI)` dengan URL gambarmu. Jika kamu puas dengan yang saya berikan, tidak perlu upload lagi, cukup copy URL gambar saya dan masukkan.
5.  **Commit Changes:** Scroll ke bawah dan klik tombol hijau "Commit changes".
6.  **Perbarui "About" Section:** (Jika belum) Klik ikon gerigi di bagian "About" di sidebar kanan. Isi "Description" dan "Topics" untuk memudahkan orang menemukan proyekmu.

Dengan *README* ini, repositori kamu akan terlihat jauh lebih profesional dan mudah dipahami!
