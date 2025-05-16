# **📸 Crowd Detection Using YOLOv4**

Crowd Detection Using YOLO adalah proyek machine learning yang bertujuan untuk mendeteksi kerumunan secara otomatis menggunakan algoritma You Only Look Once (YOLO). Sistem ini dapat digunakan untuk memantau area publik dan memberikan peringatan jika terjadi kerumunan berlebih, sehingga berguna dalam penerapan protokol keamanan, pengawasan, dan manajemen keramaian.

## 🎥 Demo Proyek
Tonton video demo penggunaan sistem ini di sini:

https://github.com/user-attachments/assets/f0d34361-7634-40c6-9e16-b35d6620db64


## 🎯 Tujuan Proyek

- Mendeteksi dan menghitung jumlah orang dalam suatu area.
- Memberikan notifikasi jika kerumunan melebihi ambang batas tertentu.
- Menggunakan model YOLO untuk deteksi objek secara real-time.

## 📦 Fitur Utama

- 🔍 Deteksi Real-Time: Menggunakan YOLO untuk mendeteksi kerumunan dalam video atau kamera langsung.
- 📊 Perhitungan Jumlah Orang: Menghitung jumlah individu dalam frame.
- 🚨 Peringatan Kerumunan: Memberikan peringatan ketika jumlah melebihi batas yang ditentukan.

## 🧠 Teknologi yang Digunakan

- YOLO (You Only Look Once) – YOLOv4 mini
- OpenCV – Pengolahan gambar dan video
- Python – Bahasa pemrograman utama
- Darknet – Framework pelatihan dan inferensi model


## 📊 Dataset

Kamu dapat menemukan dataset untuk pelatihan dan pengujian model di: https://www.crowdhuman.org/

## 🚀 Cara Menjalankan

**Clone repo:**

```bash
git clone https://github.com/IsmaDDamara/iSense_Smart-Crowd-Detection-with-ML-Model.git
```

**Arahkan ke folder test**

```bash
cd test/opencv_dnn
```

**Jalankan deteksi:**

```bash
python opencv_video.py
```

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT License.
