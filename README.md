# LayananWarga AI 🇮🇩

**Asisten Informasi Pelayanan Publik Indonesia**

LayananWarga AI adalah prototipe chatbot berbasis kecerdasan buatan yang membantu masyarakat memahami prosedur umum pelayanan publik di Indonesia. Pengguna dapat bertanya tentang KTP, Kartu Keluarga, SIM, pajak, dan dokumen administrasi lainnya.

## Fitur

- Antarmuka web berbasis Streamlit.
- Chat dengan bubble pengguna di kanan dan AI di kiri.
- Integrasi Google Gemini API.
- Riwayat percakapan selama sesi aplikasi berlangsung.
- Pilihan topik layanan publik untuk memulai pertanyaan.
- Penanganan error umum, seperti kuota API dan layanan AI yang sibuk.

## Teknologi

- Python
- Streamlit
- Google Gen AI SDK
- Google Gemini API
- pyngrok untuk demo melalui Google Colab

## Instalasi lokal

### 1. Clone repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

Ganti `USERNAME/REPOSITORY` sesuai repository milikmu.

### 2. Instal dependensi

```bash
pip install -r requirements.txt
```

### 3. Konfigurasi Gemini API

Buat API key di [Google AI Studio](https://aistudio.google.com/apikey).

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="API_KEY_MILIKMU"
```

Linux/macOS:

```bash
export GEMINI_API_KEY="API_KEY_MILIKMU"
```

Jangan pernah mengunggah API key ke GitHub.

### 4. Jalankan aplikasi

```bash
streamlit run app.py
```

Buka alamat lokal yang ditampilkan Streamlit, biasanya `http://localhost:8501`.

## Menjalankan melalui Google Colab

1. Instal dependensi dengan `pip install -r requirements.txt`, atau instal `google-genai`, `streamlit`, dan `pyngrok`.
2. Masukkan `GEMINI_API_KEY` menggunakan input tersembunyi.
3. Atur ngrok authtoken menggunakan input tersembunyi.
4. Jalankan Streamlit pada port 8501 dan buat tunnel ngrok.

Tautan ngrok bersifat sementara dan aktif selama runtime serta proses terkait berjalan.

## Tampilan Chatbot

<img width="1906" height="911" alt="Screenshot 2026-10-25 211355" src="https://github.com/user-attachments/assets/37c8c1eb-390e-43bb-aacd-91d970b64fcd" />

<img width="1902" height="907" alt="Screenshot 2026-10-25 212747" src="https://github.com/user-attachments/assets/9b54dd9a-c110-4170-adbe-80039dd9d4b1" />


## Batasan dan keamanan

- Proyek ini bukan layanan resmi pemerintah.
- Jawaban AI dapat tidak lengkap, keliru, atau kedaluwarsa.
- Aplikasi belum melakukan pencarian sumber resmi secara otomatis.
- Aplikasi belum terintegrasi dengan sistem pemerintah.
- Hindari memasukkan NIK, nomor KK, kata sandi, atau data pribadi sensitif.

Verifikasi persyaratan, biaya, dan jadwal melalui kanal resmi instansi terkait.

## Rencana pengembangan

- Menambahkan tautan dan referensi sumber resmi.
- Menambahkan pencarian informasi dari situs instansi pemerintah.
- Menyesuaikan jawaban berdasarkan kabupaten/kota.
- Menambahkan evaluasi akurasi jawaban dan feedback pengguna.

## Lisensi

Milik Pribadi.
