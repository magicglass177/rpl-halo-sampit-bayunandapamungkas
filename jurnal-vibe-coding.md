# Jurnal Vibe Coding — Jobsheet 1

Nama: ... NIM: ... Kelas: ...

Proyek: Halo Sampit (Flask) | Asisten AI yang digunakan: Claude

> Petunjuk: bagian bertanda ✏️ **ISI** harus Anda lengkapi sendiri setelah menjalankan dan menguji kode. Hapus tanda ✏️ setelah terisi.

## Ringkasan Entri

| No | Tujuan | Prompt (ringkas) | Hasil AI | Keputusan | Alasan |
|----|--------|------------------|----------|-----------|--------|
| 1 | Beranda + formulir nama | Prompt Langkah 7 (konteks, tujuan, batasan, format keluaran) | `app.py` + `templates/index.html` + penjelasan 5 butir | Terima | Kriteria (a)–(d) terpenuhi; hanya memakai Flask dan pustaka standar; tidak ada rahasia di kode; `{{ nama }}` di-escape otomatis oleh Jinja2 |
| 2 | Salam sesuai jam | Prompt Langkah 12 (fungsi `salam_waktu(jam)`) | ✏️ **ISI** | ✏️ **ISI** (Terima/Ubah/Tolak) | ✏️ **ISI** |

---

## Entri 1 — Beranda + formulir nama

**Spesifikasi (kriteria penerimaan):**
- (a) Beranda menampilkan judul "Halo Sampit!"
- (b) Beranda menampilkan tanggal dan jam server
- (c) Formulir menerima nama dan menampilkan `Halo, <nama>!`
- (d) Masukan pengguna tampil aman (tidak dieksekusi sebagai HTML)

**Prompt lengkap:**

```text
Konteks: Saya mahasiswa D3 Teknologi Informasi yang baru belajar Flask. Proyek saya
bernama "Halo Sampit".
Tujuan: Buat aplikasi web Flask dengan satu halaman beranda yang menampilkan judul "Halo
Sampit!", tanggal dan jam server saat ini, serta formulir untuk mengisi nama. Setelah formulir
dikirim, tampilkan "Halo, <nama>!".
Batasan: Gunakan hanya Flask dan pustaka standar Python. Tanpa basis data dan tanpa
JavaScript. Masukan pengguna harus ditampilkan secara aman. Beri komentar singkat
berbahasa Indonesia. Aplikasi berjalan di localhost.
Format keluaran: Tampilkan isi app.py dan templates/index.html sebagai dua blok kode
terpisah, lalu jelaskan cara kerjanya dalam maksimal 5 butir.
```

**Hasil AI:**
- `app.py`: satu rute `/` untuk GET dan POST, nama diambil dengan `request.form.get("nama", "").strip()[:50]`, waktu dari `datetime.now()`, dijalankan di `127.0.0.1:5000` dengan `debug=True`.
- `templates/index.html`: formulir `method="post"`, input `maxlength="50"`, dan `{{ nama }}` di dalam blok `{% if nama %}`.
- Penjelasan 5 butir (rute, tanggal/jam, keluaran aman, tampilan salam, cara menjalankan).

**Hasil uji:**
- Nama biasa (mis. `Bayu`) menampilkan `Halo, Bayu!`: ✏️ **ISI** (berhasil/tidak)
- Uji `<b>tes</b>`: teks tampil apa adanya, tidak menjadi huruf tebal: ✏️ **ISI** (sesuai/tidak)
- Waktu server berubah setelah halaman dimuat ulang: ✏️ **ISI**

**Tinjauan kode:**
- Import hanya `datetime` (pustaka standar) dan `Flask`, `render_template`, `request` (Flask). Tidak ada paket tambahan.
- Tidak ada kata sandi, token, atau kunci rahasia di kode.
- `debug=True` mengaktifkan pemuat ulang otomatis dan halaman debugger saat error. Tidak boleh aktif saat rilis karena debugger dapat membocorkan kode dan memungkinkan eksekusi kode dari jarak jauh.
- Bagian yang tidak diminta namun ditambahkan AI: batas 50 karakter di server (`[:50]`), atribut `maxlength`, dan `host="127.0.0.1"` serta `port=5000` yang ditulis eksplisit. Semuanya wajar dan saya terima.
- Tiga baris yang awalnya belum saya pahami (tulis ulang dengan kata-kata sendiri):
  1. ✏️ **ISI** (baris + penjelasan Anda)
  2. ✏️ **ISI**
  3. ✏️ **ISI**

**Keputusan:** Terima

**Alasan:** Semua kriteria (a)–(d) terpenuhi, kode hanya memakai Flask dan pustaka standar, tidak ada rahasia tertanam, dan Jinja2 meng-escape masukan otomatis sehingga aman dari XSS. Tambahan dari AI (batas 50 karakter dan pengaturan host) sesuai tujuan aplikasi.

**Commit:** `Tambah aplikasi Halo Sampit dengan formulir sapaan`

---

## Entri 2 — Salam sesuai jam

**Spesifikasi:** Beranda menampilkan salam sesuai jam server sebelum waktu server: pagi (04.00–10.59), siang (11.00–14.59), sore (15.00–17.59), malam (18.00–03.59). Fitur lain tidak berubah dan tidak ada paket baru.

**Prompt lengkap:**

```text
Pada aplikasi Flask "Halo Sampit" berikut [isi app.py dan index.html saya], tambahkan fungsi
salam_waktu(jam) yang mengembalikan "Selamat pagi" (04.00–10.59), "Selamat siang"
(11.00–14.59), "Selamat sore" (15.00–17.59), dan "Selamat malam" (18.00–03.59). Tampilkan
salam itu di beranda sebelum waktu server. Jangan mengubah fitur lain dan jangan menambah
paket baru. Tampilkan hanya bagian kode yang berubah.
```

**Hasil AI:** ✏️ **ISI** (ringkas: fungsi apa yang dibuat, bagian mana di `app.py` dan `index.html` yang berubah)

**Uji batas jam:**

```text
python -c "from app import salam_waktu as s; print([(j, s(j)) for j in (3, 4, 10, 11, 14, 15, 17, 18)])"
```

Hasil yang seharusnya: 3 → malam; 4 → pagi; 10 → pagi; 11 → siang; 14 → siang; 15 → sore; 17 → sore; 18 → malam.

Hasil yang saya dapat: ✏️ **ISI** (tempel keluaran terminal; ada jam yang salah atau tidak)

**Tinjauan perubahan (Source Control VS Code):** ✏️ **ISI** (baris apa yang ditambah/dihapus, apakah ada perubahan di luar permintaan)

**Keputusan:** ✏️ **ISI** (Terima / Ubah / Tolak)

**Alasan:** ✏️ **ISI** (wajib terisi; jelaskan berdasarkan hasil uji batas jam)

**Commit:** `Tambah salam sesuai waktu dan perbarui jurnal`

---

## Catatan Penggunaan AI

- Semua kode awal dihasilkan oleh asisten AI (Claude) berdasarkan prompt di atas, lalu saya tinjau dan uji sendiri sebelum di-commit.
- Tidak ada kata sandi, token, atau data pribadi yang dimasukkan ke prompt maupun repositori.
- Pelajaran dari praktikum ini: ✏️ **ISI** (1–2 kalimat, mis. risiko vibe coding yang Anda temui dan cara mengendalikannya)
