# ======================================================================
#                     PROGRAM CLUSTERING AI MAHASISWA
#                     Metode K-Means Clustering
# ======================================================================

from math import sqrt

JUDUL = "PROGRAM CLUSTERING AI MAHASISWA"

KETERANGAN_CLUSTER = {
    1: "Pengguna AI Intensif",
    2: "AI sebagai Pendukung Belajar",
    3: "Minim Penggunaan AI / Mandiri"
}

# --------------------------- DATA STATIS -------------------------------
# Data kuesioner mahasiswa; nama dan NIM diganti dengan identitas anonim untuk publikasi.
# Jawaban kuesioner dan nilai numerik tidak diubah.
# Identitas anonim bukan nama/NIM asli responden.
DATA_MAHASISWA = [{'no': 1,
  'nama': 'Mahasiswa_01',
  'nim': 'M001',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 4,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Persiapan ujian atau merangkum materi, mencari referensi dan '
               'ide penulisan, menerjemahkan atau menjelaskan teks'},
 {'no': 2,
  'nama': 'Mahasiswa_02',
  'nim': 'M002',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 3,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Membuat atau men-debug kode program, Persiapan ujian atau '
               'merangkum materi'},
 {'no': 3,
  'nama': 'Mahasiswa_03',
  'nim': 'M003',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 3,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, Persiapan ujian atau merangkum materi'},
 {'no': 4,
  'nama': 'Mahasiswa_04',
  'nim': 'M004',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 4,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Membuat atau men-debug kode program, Persiapan ujian atau '
               'merangkum materi, menerjemahkan atau menjelaskan teks'},
 {'no': 5,
  'nama': 'Mahasiswa_05',
  'nim': 'M005',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Membuat atau men-debug kode program, Persiapan ujian atau '
               'merangkum materi, mencari referensi dan ide penulisan'},
 {'no': 6,
  'nama': 'Mahasiswa_06',
  'nim': 'M006',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 3,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, Persiapan ujian atau merangkum materi, mencari referensi dan ide penulisan, '
               'menerjemahkan atau menjelaskan teks'},
 {'no': 7,
  'nama': 'Mahasiswa_07',
  'nim': 'M007',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, mencari referensi dan ide penulisan, menerjemahkan atau menjelaskan teks'},
 {'no': 8,
  'nama': 'Mahasiswa_08',
  'nim': 'M008',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Di beberapa tahap penting (Awal,tengah,akhir)',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 4,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Membuat atau men-debug kode program, Persiapan ujian atau '
               'merangkum materi'},
 {'no': 9,
  'nama': 'Mahasiswa_09',
  'nim': 'M009',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Sangat yakin, saya terbiasa belajar mandiri',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 4,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah'},
 {'no': 10,
  'nama': 'Mahasiswa_10',
  'nim': 'M010',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Membuat atau men-debug kode program'},
 {'no': 11,
  'nama': 'Mahasiswa_11',
  'nim': 'M011',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, Persiapan ujian atau merangkum materi, mencari referensi dan ide penulisan, '
               'menerjemahkan atau menjelaskan teks'},
 {'no': 12,
  'nama': 'Mahasiswa_12',
  'nim': 'M012',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 4,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Persiapan ujian atau merangkum materi, mencari referensi dan '
               'ide penulisan'},
 {'no': 13,
  'nama': 'Mahasiswa_13',
  'nim': 'M013',
  'frekuensi_ai': 'Jarang,1-2x setiap bulannya',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 1,
  'kesulitan': 'Tidak sulit, bisa mandiri',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Persiapan ujian atau merangkum materi, mencari referensi dan '
               'ide penulisan, menerjemahkan atau menjelaskan teks'},
 {'no': 14,
  'nama': 'Mahasiswa_14',
  'nim': 'M014',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 2,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Persiapan ujian atau merangkum materi, mencari referensi dan '
               'ide penulisan, menerjemahkan atau menjelaskan teks'},
 {'no': 15,
  'nama': 'Mahasiswa_15',
  'nim': 'M015',
  'frekuensi_ai': 'Jarang,1-2x setiap bulannya',
  'keyakinan': 'Sangat yakin, saya terbiasa belajar mandiri',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 1,
  'kesulitan': 'Tidak sulit, bisa mandiri',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah'},
 {'no': 16,
  'nama': 'Mahasiswa_16',
  'nim': 'M016',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Setiap hari',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program'},
 {'no': 17,
  'nama': 'Mahasiswa_17',
  'nim': 'M017',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, mencari referensi dan ide penulisan'},
 {'no': 18,
  'nama': 'Mahasiswa_18',
  'nim': 'M018',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Persiapan ujian atau '
               'merangkum materi, mencari referensi dan ide penulisan'},
 {'no': 19,
  'nama': 'Mahasiswa_19',
  'nim': 'M019',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Di beberapa tahap penting (Awal,tengah,akhir)',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 4,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, Persiapan ujian atau merangkum materi, mencari referensi dan ide penulisan'},
 {'no': 20,
  'nama': 'Mahasiswa_20',
  'nim': 'M020',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'Sangat yakin, saya terbiasa belajar mandiri',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 3,
  'kesulitan': 'Tidak sulit, bisa mandiri',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, mencari referensi dan ide penulisan, menerjemahkan atau '
               'menjelaskan teks'},
 {'no': 21,
  'nama': 'Mahasiswa_21',
  'nim': 'M021',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Sangat yakin, saya terbiasa belajar mandiri',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Membuat atau men-debug kode program, menerjemahkan atau '
               'menjelaskan teks'},
 {'no': 22,
  'nama': 'Mahasiswa_22',
  'nim': 'M022',
  'frekuensi_ai': 'Jarang,1-2x setiap bulannya',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 4,
  'kesulitan': 'Sangat kesulitan',
  'tujuan_ai': 'Membuat atau men-debug kode program'},
 {'no': 23,
  'nama': 'Mahasiswa_23',
  'nim': 'M023',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 3,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Membuat atau men-debug kode program, mencari referensi dan ide penulisan'},
 {'no': 24,
  'nama': 'Mahasiswa_24',
  'nim': 'M024',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Persiapan ujian atau merangkum materi, mencari referensi dan '
               'ide penulisan, menerjemahkan atau menjelaskan teks'},
 {'no': 25,
  'nama': 'Mahasiswa_25',
  'nim': 'M025',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 4,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, Persiapan ujian atau merangkum materi'},
 {'no': 26,
  'nama': 'Mahasiswa_26',
  'nim': 'M026',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah'},
 {'no': 27,
  'nama': 'Mahasiswa_27',
  'nim': 'M027',
  'frekuensi_ai': 'Jarang,1-2x setiap bulannya',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '1-2 kali per minggu',
  'ketergantungan': 2,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, mencari referensi dan ide penulisan'},
 {'no': 28,
  'nama': 'Mahasiswa_28',
  'nim': 'M028',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 4,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Membuat atau men-debug kode program, menerjemahkan atau '
               'menjelaskan teks'},
 {'no': 29,
  'nama': 'Mahasiswa_29',
  'nim': 'M029',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 4,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Mengerjakan tugas atau laporan, Persiapan ujian atau merangkum materi, mencari referensi dan ide '
               'penulisan'},
 {'no': 30,
  'nama': 'Mahasiswa_30',
  'nim': 'M030',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': 'Setiap hari',
  'ketergantungan': 5,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Persiapan ujian atau '
               'merangkum materi, menerjemahkan atau menjelaskan teks'},
 {'no': 31,
  'nama': 'Mahasiswa_31',
  'nim': 'M031',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Sangat yakin, saya terbiasa belajar mandiri',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Persiapan ujian atau merangkum materi, mencari referensi dan '
               'ide penulisan'},
 {'no': 32,
  'nama': 'Mahasiswa_32',
  'nim': 'M032',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'Ragu-Ragu, proses belajar menjadi lebih lambat',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 3,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Membuat atau men-debug kode program, menerjemahkan atau '
               'menjelaskan teks'},
 {'no': 33,
  'nama': 'Mahasiswa_33',
  'nim': 'M033',
  'frekuensi_ai': 'kadang-Kadang (1-2x setiap minggu)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Hanya saat mentok / tidak tahu cara lanjut',
  'frekuensi_minggu': '3-4 kali perminggu',
  'ketergantungan': 4,
  'kesulitan': 'Sedikit lebih lambat',
  'tujuan_ai': 'Persiapan ujian atau merangkum materi'},
 {'no': 34,
  'nama': 'Mahasiswa_34',
  'nim': 'M034',
  'frekuensi_ai': 'Sering (hampir setiap hari)',
  'keyakinan': 'cukup yakin, hanya sedikit terganggu',
  'tahap_ai': 'Untuk mengecek atau memperbaiki hasil saya',
  'frekuensi_minggu': 'Hampir setiap Hari',
  'ketergantungan': 4,
  'kesulitan': 'Cukup kesulitan',
  'tujuan_ai': 'Memahami konsep atau materi Kuliah, Mengerjakan tugas atau laporan, Membuat atau men-debug kode '
               'program, Persiapan ujian atau merangkum materi, mencari referensi dan ide penulisan, '
               'menerjemahkan atau menjelaskan teks'}]

# ----------------------- KONVERSI DATA AWAL ----------------------------
# Semakin besar nilai, semakin tinggi kecenderungan penggunaan/kebutuhan AI.
KONVERSI_FREKUENSI_AI = {
    "Jarang,1-2x setiap bulannya": 1,
    "kadang-Kadang (1-2x setiap minggu)": 2,
    "Sering (hampir setiap hari)": 3
}

KONVERSI_KEYAKINAN = {
    "Sangat yakin, saya terbiasa belajar mandiri": 1,
    "cukup yakin, hanya sedikit terganggu": 2,
    "Ragu-Ragu, proses belajar menjadi lebih lambat": 3
}

KONVERSI_TAHAP_AI = {
    "Hanya saat mentok / tidak tahu cara lanjut": 1,
    "Untuk mengecek atau memperbaiki hasil saya": 2,
    "Di beberapa tahap penting (Awal,tengah,akhir)": 3
}

KONVERSI_FREKUENSI_MINGGU = {
    "1-2 kali per minggu": 1,
    "3-4 kali perminggu": 2,
    "Hampir setiap Hari": 3,
    "Setiap hari": 4
}

KONVERSI_KESULITAN = {
    "Tidak sulit, bisa mandiri": 1,
    "Sedikit lebih lambat": 2,
    "Cukup kesulitan": 3,
    "Sangat kesulitan": 4
}

URUTAN_FITUR = [
    "Frekuensi AI",
    "Keyakinan tanpa AI",
    "Tahap AI",
    "Frekuensi/Minggu",
    "Ketergantungan",
    "Kesulitan tanpa AI",
    "Jumlah Tujuan AI"
]


def garis(karakter="=", panjang=128):
    print(karakter * panjang)


def header():
    garis()
    print(JUDUL.center(128))
    garis()
    print("Cluster 1 = Pengguna AI Intensif")
    print("Cluster 2 = AI sebagai Pendukung Belajar")
    print("Cluster 3 = Minim Penggunaan AI / Mandiri")
    garis("-")


def pendekkan(teks, panjang):
    return teks if len(teks) <= panjang else teks[:panjang - 3] + "..."


def jumlah_tujuan(teks):
    # Pada data kuesioner, tujuan yang dipilih dipisahkan dengan tanda koma.
    return len([pilihan for pilihan in teks.split(",") if pilihan.strip()])


def ubah_ke_angka(mahasiswa):
    return [
        KONVERSI_FREKUENSI_AI[mahasiswa["frekuensi_ai"]],
        KONVERSI_KEYAKINAN[mahasiswa["keyakinan"]],
        KONVERSI_TAHAP_AI[mahasiswa["tahap_ai"]],
        KONVERSI_FREKUENSI_MINGGU[mahasiswa["frekuensi_minggu"]],
        mahasiswa["ketergantungan"],
        KONVERSI_KESULITAN[mahasiswa["kesulitan"]],
        jumlah_tujuan(mahasiswa["tujuan_ai"])
    ]


def siapkan_data_awal():
    data_angka = []
    for mahasiswa in DATA_MAHASISWA:
        data_angka.append({
            "no": mahasiswa["no"],
            "nama": mahasiswa["nama"],
            "nim": mahasiswa["nim"],
            "nilai": ubah_ke_angka(mahasiswa)
        })
    return data_angka


def tampilkan_konversi():
    print("\nKETERANGAN PERUBAHAN DATA AWAL MENJADI ANGKA")
    garis("-")
    print("1. Frekuensi AI       : Jarang = 1, Kadang-kadang = 2, Sering = 3")
    print("2. Keyakinan tanpa AI : Sangat yakin/mandiri = 1, Cukup yakin = 2, Ragu-ragu = 3")
    print("3. Tahap memakai AI   : Saat mentok = 1, Mengecek hasil = 2, Beberapa tahap = 3")
    print("4. Frekuensi/minggu   : 1-2 kali = 1, 3-4 kali = 2, Hampir setiap hari = 3, Setiap hari = 4")
    print("5. Ketergantungan     : Menggunakan nilai asli pada data, yaitu skala 1 sampai 5")
    print("6. Kesulitan tanpa AI : Tidak sulit = 1, Sedikit lambat = 2, Cukup sulit = 3, Sangat sulit = 4")
    print("7. Tujuan AI          : Banyaknya tujuan yang dipilih mahasiswa")
    garis("-")


def tampilkan_data_awal_yang_sudah_diubah(data_angka):
    print("\nDATA AWAL SETELAH DIUBAH MENJADI ANGKA")
    print("Urutan nilai fitur:")
    print("[Frekuensi AI, Keyakinan tanpa AI, Tahap AI, Frekuensi/Minggu, Ketergantungan, Kesulitan tanpa AI, Jumlah Tujuan AI]")
    garis("-")
    print(f"{'No':<4}{'Nama Mahasiswa':<38}{'NIM':<13}{'Data Awal Setelah Dikonversi':<40}")
    garis("-")
    for mhs in data_angka:
        print(f"{mhs['no']:<4}{pendekkan(mhs['nama'], 36):<38}{mhs['nim']:<13}{str(mhs['nilai']):<40}")
    garis("-")
    print(f"Jumlah data yang akan dikelompokkan = {len(data_angka)} mahasiswa")


def jarak_euclidean(data, centroid):
    return sqrt(sum((data[i] - centroid[i]) ** 2 for i in range(len(data))))


def centroid_baru(anggota, centroid_lama):
    if len(anggota) == 0:
        return centroid_lama[:]
    return [
        sum(mhs["nilai"][fitur] for mhs in anggota) / len(anggota)
        for fitur in range(len(anggota[0]["nilai"]))
    ]


def rata_rata_centroid(centroid):
    return sum(centroid) / len(centroid)


def format_centroid(centroid):
    return "[" + ", ".join(f"{nilai:.2f}" for nilai in centroid) + "]"


def urutkan_label_cluster(cluster, centroid):
    """
    K-Means sebenarnya menghasilkan kelompok tanpa nama.
    Supaya nomor cluster sesuai judul projek, cluster diurutkan berdasarkan
    rata-rata centroid:
    tertinggi = Cluster 1 (intensif), tengah = Cluster 2, terendah = Cluster 3.
    """
    pasangan = list(zip(cluster, centroid))
    pasangan.sort(key=lambda item: rata_rata_centroid(item[1]), reverse=True)
    return [item[0] for item in pasangan], [item[1] for item in pasangan]


def tampilkan_centroid_awal(centroid, pemilik):
    print("\nCENTROID AWAL")
    garis("-")
    print("Centroid awal dipilih dari tiga mahasiswa yang mewakili pola penggunaan AI berbeda.")
    print("Urutan fitur centroid =", URUTAN_FITUR)
    for nomor in range(1, 4):
        print(f"\nCluster {nomor} = {KETERANGAN_CLUSTER[nomor]}")
        print(f"Data wakil : {pemilik[nomor - 1]['nama']} ({pemilik[nomor - 1]['nim']})")
        print(f"Centroid   : {format_centroid(centroid[nomor - 1])}")
    garis("-")


def tampilkan_satu_iterasi(iterasi, cluster, centroid):
    print(f"\nPROSES CLUSTERING - ITERASI KE-{iterasi}")
    garis("-")
    for nomor in range(1, 4):
        anggota = cluster[nomor - 1]
        print(f"\nCluster {nomor} = {KETERANGAN_CLUSTER[nomor]}")
        print(f"Centroid hasil iterasi = {format_centroid(centroid[nomor - 1])}")
        print(f"Jumlah anggota         = {len(anggota)} mahasiswa")
        for mhs in anggota:
            print(f"  - {mhs['nama']} ({mhs['nim']}) -> {mhs['nilai']}")
    garis("-")


def susunan_anggota(cluster):
    return tuple(tuple(mhs["nim"] for mhs in kelompok) for kelompok in cluster)


def proses_clustering(data_angka):
    # Tiga data wakil untuk centroid awal (indeks 3, 1, 14),
    # mewakili penggunaan AI intensif, pendukung, dan minim/mandiri.
    wakil_centroid = [
        data_angka[3],
        data_angka[1],
        data_angka[14]
    ]
    centroid = [mhs["nilai"][:] for mhs in wakil_centroid]

    input("\nTekan Enter untuk menampilkan centroid awal...")
    tampilkan_centroid_awal(centroid, wakil_centroid)

    input("\nTekan Enter untuk memulai iterasi ke-1...")

    anggota_sebelumnya = None
    iterasi = 0

    while True:
        iterasi += 1
        cluster = [[], [], []]

        # Menentukan cluster terdekat untuk setiap mahasiswa.
        for mahasiswa in data_angka:
            jarak = [jarak_euclidean(mahasiswa["nilai"], titik) for titik in centroid]
            posisi_terdekat = jarak.index(min(jarak))
            cluster[posisi_terdekat].append(mahasiswa)

        # Menghitung centroid hasil iterasi.
        centroid_hasil = [
            centroid_baru(cluster[i], centroid[i])
            for i in range(3)
        ]

        # Menetapkan nama cluster berdasarkan intensitas centroid.
        cluster, centroid_hasil = urutkan_label_cluster(cluster, centroid_hasil)

        tampilkan_satu_iterasi(iterasi, cluster, centroid_hasil)

        anggota_sekarang = susunan_anggota(cluster)
        if anggota_sekarang == anggota_sebelumnya:
            print(f"\nCluster telah stabil pada iterasi ke-{iterasi}.")
            print("Anggota cluster tidak berubah dari iterasi sebelumnya.")
            return cluster, centroid_hasil, iterasi

        anggota_sebelumnya = anggota_sekarang
        centroid = centroid_hasil
        input(f"\nTekan Enter untuk melanjutkan ke iterasi ke-{iterasi + 1}...")


def tampilkan_kesimpulan(cluster, centroid, iterasi):
    print("\nKESIMPULAN HASIL CLUSTERING")
    garis("=")
    total = len(DATA_MAHASISWA)
    for nomor in range(1, 4):
        jumlah = len(cluster[nomor - 1])
        persen = jumlah / total * 100
        print(
            f"Cluster {nomor} = {KETERANGAN_CLUSTER[nomor]}: "
            f"{jumlah} mahasiswa ({persen:.1f}%), "
            f"rata-rata centroid {rata_rata_centroid(centroid[nomor - 1]):.2f}."
        )

    print(
        f"\nProses K-Means pada {total} data mahasiswa berhenti setelah {iterasi} iterasi, "
        "karena anggota pada setiap cluster sudah tidak berubah. "
        "Cluster 1 merupakan kelompok yang paling intensif memanfaatkan AI, "
        "Cluster 2 memanfaatkan AI sebagai pendukung belajar, sedangkan "
        "Cluster 3 merupakan kelompok yang penggunaan AI-nya paling minim dan lebih mandiri."
    )
    garis("=")


def main():
    header()
    tampilkan_konversi()

    # Data awal diubah menjadi angka sebelum memasuki proses K-Means.
    data_angka = siapkan_data_awal()
    tampilkan_data_awal_yang_sudah_diubah(data_angka)

    cluster_akhir, centroid_akhir, jumlah_iterasi = proses_clustering(data_angka)
    tampilkan_kesimpulan(cluster_akhir, centroid_akhir, jumlah_iterasi)


if __name__ == "__main__":
    main()
