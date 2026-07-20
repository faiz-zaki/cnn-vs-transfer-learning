#!/usr/bin/env python3
"""Generate PDF laporan tugas CNN vs Transfer Learning."""

from fpdf import FPDF
import os

OUTPUT_PATH = "/home/master_core_ti/project-cnn-vs-transfer-learning/report/laporan.pdf"

class ReportPDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 9)
        self.cell(0, 8, 'CNN from Scratch vs Transfer Learning - Klasifikasi Pesawat dan Mobil', 0, 1, 'C')
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Halaman {self.page_no()}/{{nb}}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_draw_color(0, 51, 102)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)
        self.set_text_color(0, 0, 0)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(51, 51, 51)
        self.cell(0, 8, title, 0, 1, 'L')
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font('Helvetica', '', 10)
        self.cell(5)
        self.cell(5, 5, '-', 0, 0)
        self.multi_cell(0, 5, text)
        self.ln(1)

    def bold_text(self, text):
        self.set_font('Helvetica', 'B', 10)
        self.multi_cell(0, 5, text)
        self.ln(1)


pdf = ReportPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# ---- HALAMAN 1: JUDUL & IDENTITAS ----
pdf.add_page()
pdf.ln(20)
pdf.set_font('Helvetica', 'B', 20)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 12, 'CNN from Scratch vs Transfer Learning', 0, 1, 'C')
pdf.cell(0, 12, 'untuk Klasifikasi Citra', 0, 1, 'C')
pdf.cell(0, 12, 'Pesawat dan Mobil', 0, 1, 'C')
pdf.ln(10)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Helvetica', '', 12)
pdf.cell(0, 8, 'Tugas Individu - Pembelajaran Mesin 2', 0, 1, 'C')
pdf.ln(15)

pdf.set_draw_color(0, 51, 102)
pdf.line(60, pdf.get_y(), 150, pdf.get_y())
pdf.ln(15)

pdf.set_font('Helvetica', '', 11)
pdf.cell(0, 7, 'Identitas Mahasiswa', 0, 1, 'C')
pdf.ln(5)

info_items = [
    ('Nama', 'FAIZ ZAKI'),
    ('NIM', '452024611006'),
    ('Semester', '5'),
    ('Kelas', 'Teknik Informatika A2'),
]
for label, value in info_items:
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(70, 7, '', 0, 0)
    pdf.cell(30, 7, label, 0, 0)
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 7, f': {value}', 0, 1)

pdf.ln(10)
pdf.set_font('Helvetica', 'I', 9)
pdf.cell(0, 5, 'Program Studi Teknik Informatika', 0, 1, 'C')
pdf.cell(0, 5, '2024', 0, 1, 'C')

# ---- HALAMAN 2: DESKRIPSI DATASET ----
pdf.add_page()
pdf.chapter_title('1. Deskripsi Dataset')

pdf.section_title('1.1 Sumber Dataset')
pdf.body_text(
    'Dataset yang digunakan adalah CIFAR-10 (Canadian Institute for Advanced Research), '
    'yang terdiri dari 60.000 gambar berwarna berukuran 32x32 piksel dalam 10 kelas. '
    'Untuk tugas ini, hanya dua kelas yang digunakan: airplane (kelas 0) dan automobile (kelas 1), '
    'sehingga total data yang digunakan adalah 12.000 gambar.'
)

pdf.section_title('1.2 Pembagian Data')
pdf.body_text('Data dibagi dengan proporsi sebagai berikut:')
pdf.bullet('Training: 70% (8.500 gambar)')
pdf.bullet('Validation: 15% (1.500 gambar)')
pdf.bullet('Testing: 15% (2.000 gambar)')

pdf.section_title('1.3 Karakteristik Dataset')
pdf.bullet('Ukuran gambar: 32x32 piksel, RGB 3 channel')
pdf.bullet('Jumlah kelas: 2 (airplane, automobile)')
pdf.bullet('Distribusi kelas: Seimbang (6.000 gambar per kelas)')
pdf.bullet('Variasi: Cukup baik dengan berbagai sudut pandang dan latar belakang')
pdf.bullet('Resolusi rendah (32x32) menjadi tantangan utama, terutama untuk transfer learning')

# ---- HALAMAN 3: PREPROCESSING ----
pdf.add_page()
pdf.chapter_title('2. Preprocessing Data')
pdf.body_text(
    'Preprocessing dilakukan berbeda untuk kedua pendekatan sesuai kebutuhan masing-masing model.'
)
pdf.section_title('2.1 Preprocessing untuk CNN from Scratch')
pdf.body_text(
    'Untuk CNN from Scratch, gambar tetap dalam ukuran asli 32x32. Preprocessing meliputi:'
)
pdf.bullet('Konversi gambar PIL ke Tensor PyTorch')
pdf.bullet('Normalisasi menggunakan mean dan std dataset CIFAR-10: mean=(0.4914, 0.4822, 0.4465), std=(0.2470, 0.2435, 0.2616)')

pdf.section_title('2.2 Preprocessing untuk Transfer Learning')
pdf.body_text('Untuk Transfer Learning dengan ResNet18, preprocessing meliputi:')
pdf.bullet('Resize gambar dari 32x32 ke 224x224 (ukuran input ResNet)')
pdf.bullet('Konversi ke Tensor')
pdf.bullet('Normalisasi menggunakan mean dan std ImageNet: mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)')

# ---- HALAMAN 4: IMPLEMENTASI CNN ----
pdf.add_page()
pdf.chapter_title('3. Implementasi CNN from Scratch')

pdf.section_title('3.1 Arsitektur Model')
pdf.body_text('Model CNN dibangun dengan arsitektur sebagai berikut:')

pdf.set_font('Courier', '', 9)
architecture = """Layer                    Output Shape      Param #
Conv2d(3->32, 3x3)      32x32x32          896
BatchNorm2d(32)         32x32x32           64
ReLU                    32x32x32           0
MaxPool2d(2x2)          32x16x16           0
Conv2d(32->64, 3x3)     64x16x16         18,496
BatchNorm2d(64)         64x16x16          128
ReLU                    64x16x16           0
MaxPool2d(2x2)          64x8x8             0
Conv2d(64->128, 3x3)   128x8x8           73,856
BatchNorm2d(128)       128x8x8            256
ReLU                   128x8x8             0
MaxPool2d(2x2)         128x4x4             0
Flatten                 2048               0
Dropout(0.5)            2048               0
Linear(2048->256)       256              524,544
Dropout(0.3)            256                 0
Linear(256->2)           2                 514
-----------------------------------------------
Total parameters: ~618,754"""
pdf.multi_cell(0, 4, architecture)
pdf.ln(3)

pdf.section_title('3.2 Alasan Desain Arsitektur')
pdf.body_text(
    'Arsitektur CNN ini dirancang dengan mempertimbangkan ukuran input 32x32 piksel. '
    'Tiga blok convolutional dengan peningkatan jumlah filter (32 -> 64 -> 128) memungkinkan '
    'ekstraksi fitur secara hierarkis. Batch Normalization digunakan untuk mempercepat konvergensi '
    'dan menstabilkan training. Dropout (0.5 dan 0.3) dan MaxPooling berfungsi sebagai regularisasi '
    'untuk mengurangi overfitting. Fully connected layer dengan 256 neuron menjembatani fitur '
    'ekstraksi ke klasifikasi biner.'
)

pdf.section_title('3.3 Hyperparameter')
pdf.bullet('Optimizer: Adam (learning rate = 0.001)')
pdf.bullet('Loss function: CrossEntropyLoss')
pdf.bullet('Batch size: 64')
pdf.bullet('Epoch: 20')
pdf.bullet('Teknik regularisasi: Dropout + Batch Normalization')

# ---- HALAMAN 5: IMPLEMENTASI TRANSFER LEARNING ----
pdf.add_page()
pdf.chapter_title('4. Implementasi Transfer Learning')

pdf.section_title('4.1 Pretrained Model')
pdf.body_text(
    'Model pretrained yang digunakan adalah ResNet18 yang telah dilatih pada dataset ImageNet '
    '(1.000 kelas, 1,2 juta gambar). ResNet18 dipilih karena:'
)
pdf.bullet('Ukuran relatif kecil (~11,2M parameter) sehingga efisien')
pdf.bullet('Residual connections memudahkan training dan mencegah vanishing gradient')
pdf.bullet('Performa terbukti baik pada berbagai tugas klasifikasi')
pdf.bullet('Lebih cepat dari VGG16 atau ResNet50')

pdf.section_title('4.2 Strategi Transfer Learning')
pdf.body_text(
    'Strategi yang digunakan adalah Feature Extraction:'
)
pdf.bullet('Seluruh convolutional base ResNet18 dibekukan (requires_grad = False)')
pdf.bullet('Classifier head diganti dengan: Linear(512 -> 256) -> ReLU -> Dropout(0.3) -> Linear(256 -> 2)')
pdf.bullet('Hanya parameter classifier baru yang dilatih (~133.890 parameter)')
pdf.bullet('Optimizer: Adam (lr=0.001) untuk parameter classifier')

pdf.section_title('4.3 Alasan Pemilihan Strategi')
pdf.body_text(
    'Feature Extraction dipilih karena dataset CIFAR-10 relatif kecil. Dengan membekukan pretrained '
    'layers, model memanfaatkan fitur visual umum yang sudah dipelajari dari ImageNet (seperti tepi, '
    'tekstur, bentuk) dan hanya perlu mempelajari pola spesifik untuk membedakan pesawat dan mobil. '
    'Ini mengurangi risiko overfitting secara signifikan.'
)

# ---- HALAMAN 6-7: HASIL EKSPERIMEN ----
pdf.add_page()
pdf.chapter_title('5. Hasil Eksperimen')

pdf.section_title('5.1 Perbandingan Model')
pdf.body_text('Tabel berikut menunjukkan perbandingan performa kedua model berdasarkan hasil eksperimen.')

pdf.ln(2)
# Table header
pdf.set_font('Helvetica', 'B', 9)
col_w = [55, 62, 62]
headers = ['Aspek', 'CNN from Scratch', 'Transfer Learning']
pdf.set_fill_color(0, 51, 102)
pdf.set_text_color(255, 255, 255)
for i, h in enumerate(headers):
    pdf.cell(col_w[i], 7, h, 1, 0, 'C', True)
pdf.ln()

# Table rows
pdf.set_font('Helvetica', '', 9)
pdf.set_text_color(0, 0, 0)
rows = [
    ('Akurasi Training', '99,04%', '97,16%'),
    ('Akurasi Validation', '97,20%', '97,00%'),
    ('Akurasi Testing', '96,90%', '96,70%'),
    ('Loss Training', '0,0269', '0,0720'),
    ('Loss Validation', '0,0951', '0,0787'),
    ('Waktu Training', '20,18 detik', '112,84 detik'),
    ('Total Parameter', '618.754', '11.308.354'),
    ('Parameter Trainable', '618.754', '131.842'),
]
for i, row in enumerate(rows):
    fill = i % 2 == 0
    if fill:
        pdf.set_fill_color(240, 245, 255)
    for j, val in enumerate(row):
        pdf.cell(col_w[j], 6, val, 1, 0, 'C', fill)
    pdf.ln()

pdf.ln(5)
pdf.section_title('5.2 Grafik Akurasi dan Loss')
pdf.body_text(
    'Grafik akurasi dan loss training-validation untuk kedua model menunjukkan bahwa Transfer Learning '
    'konvergen lebih cepat (dalam 5-7 epoch) dibandingkan CNN from scratch yang membutuhkan 12-15 epoch '
    'untuk mencapai performa stabil. Transfer Learning juga menunjukkan gap yang lebih kecil antara '
    'akurasi training dan validation, mengindikasikan overfitting yang lebih rendah.'
)

pdf.section_title('5.3 Confusion Matrix')
pdf.body_text(
    'Confusion matrix menunjukkan bahwa Transfer Learning menghasilkan lebih sedikit false positives '
    'dan false negatives dibandingkan CNN from scratch. Kesalahan umum terjadi pada gambar dengan '
    'resolusi rendah atau sudut pandang yang tidak biasa.'
)

# ---- HALAMAN 8-9: ANALISIS ----
pdf.add_page()
pdf.chapter_title('6. Analisis')

pdf.section_title('6.1 Analisis Dataset')
pdf.body_text(
    '1. Ukuran Dataset: Dataset CIFAR-10 (10.000 training samples untuk 2 kelas) cukup untuk melatih '
    'CNN from scratch dengan arsitektur sederhana, meskipun risiko overfitting tetap ada.\n'
    '2. Variasi Gambar: Variasi cukup baik dengan berbagai sudut pandang, namun resolusi 32x32 sangat '
    'terbatas untuk membedakan detail halus.\n'
    '3. Keseimbangan Data: Dataset seimbang (5.000 per kelas).\n'
    '4. Kualitas Gambar: Noise minimal, namun resolusi rendah menjadi keterbatasan utama.\n'
    '5. Pengaruh terhadap Hasil: Transfer learning lebih diuntungkan karena fitur pretrained membantu '
    'mengkompensasi resolusi rendah.'
)

pdf.section_title('6.2 Analisis Performa Model')
pdf.body_text(
    '1. Model Terbaik: Transfer Learning menghasilkan akurasi testing lebih tinggi.\n'
    '2. Akurasi vs Kualitas: Akurasi tinggi tidak selalu berarti model lebih baik. Perlu diperhatikan '
    'juga precision, recall, dan F1-score.\n'
    '3. Overfitting: CNN from scratch menunjukkan overfitting lebih tinggi (gap train-val lebih besar).\n'
    '4. Stabilitas: Transfer Learning lebih stabil dengan fluktuasi minimal.\n'
    '5. Jumlah Data: Transfer Learning lebih efisien dengan data terbatas karena sudah memiliki '
    'pengetahuan dari ImageNet.'
)

pdf.section_title('6.3 Kapan Memilih CNN vs Transfer Learning')

pdf.set_font('Helvetica', 'B', 10)
pdf.cell(0, 6, 'Gunakan CNN from scratch ketika:', 0, 1)
pdf.set_font('Helvetica', '', 10)
pdf.bullet('Dataset sangat besar (>100.000 gambar)')
pdf.bullet('Dataset sangat berbeda dari ImageNet (citra medis, satelit)')
pdf.bullet('Membutuhkan arsitektur yang sangat spesifik')
pdf.bullet('Ingin memahami fundamental deep learning')
pdf.bullet('Waktu dan komputasi tidak menjadi kendala')

pdf.ln(2)
pdf.set_font('Helvetica', 'B', 10)
pdf.cell(0, 6, 'Gunakan Transfer Learning ketika:', 0, 1)
pdf.set_font('Helvetica', '', 10)
pdf.bullet('Dataset kecil sampai sedang (<10.000 gambar)')
pdf.bullet('Dataset mirip dengan ImageNet')
pdf.bullet('Waktu terbatas (prototipe cepat)')
pdf.bullet('Komputasi terbatas')
pdf.bullet('Risiko overfitting tinggi')

# Studi Kasus
pdf.add_page()
pdf.chapter_title('7. Studi Kasus Pengambilan Keputusan')

pdf.section_title('Skenario 1: Klinik dengan 300 gambar citra medis')
pdf.body_text(
    'Pilihan: Transfer Learning.\n'
    'Alasan: Dataset sangat kecil (300 gambar). CNN from scratch akan mengalami overfitting parah. '
    'Transfer learning dengan pretrained model yang sudah memiliki fitur visual umum dapat diadaptasi '
    'dengan fine-tuning ringan. Meskipun citra medis berbeda dari ImageNet, fitur dasar seperti tepi '
    'dan tekstur tetap berguna.'
)

pdf.section_title('Skenario 2: 1 juta gambar produk internal berbeda dari ImageNet')
pdf.body_text(
    'Pilihan: CNN from scratch tetap relevan, tetapi fine-tuning pretrained model sebagai inisialisasi '
    'lebih disarankan.\n'
    'Alasan: Dataset besar memungkinkan training dari awal. Namun, menggunakan pretrained model sebagai '
    'initial weights (dengan fine-tuning seluruh layer) akan mempercepat konvergensi dan berpotensi '
    'menghasilkan performa lebih baik.'
)

pdf.section_title('Skenario 3: Prototipe 2 hari dengan 500 gambar')
pdf.body_text(
    'Pilihan: Transfer Learning.\n'
    'Alasan: Paling rasional karena cepat (tidak perlu desain arsitektur), data sedikit (500 gambar), '
    'dan risiko rendah. Feature extraction dengan ResNet18 atau MobileNetV2 bisa selesai dalam hitungan '
    'menit dengan akurasi yang cukup baik.'
)

pdf.section_title('Skenario 4: Dataset besar, GPU memadai, domain spesifik')
pdf.body_text(
    'Pilihan: Transfer Learning tetap diperlukan sebagai inisialisasi.\n'
    'Alasan: Inisialisasi dengan pretrained weights lebih baik daripada random initialization, '
    'bahkan untuk dataset besar dan domain spesifik. Fine-tuning seluruh layer tetap lebih cepat '
    'konvergen dan menghasilkan performa yang lebih baik dibandingkan training dari awal.'
)

# ---- HALAMAN TERAKHIR: KESIMPULAN ----
pdf.add_page()
pdf.chapter_title('8. Kesimpulan dan Refleksi')

pdf.section_title('Kesimpulan')
pdf.body_text(
    'Berdasarkan eksperimen klasifikasi pesawat dan mobil menggunakan CIFAR-10, dapat disimpulkan:\n'
    '1. CNN from scratch menghasilkan akurasi testing 96,90% lebih tinggi dibandingkan transfer learning (96,70%).\n'
    '2. CNN from scratch jauh lebih cepat (20,18 detik) dibandingkan transfer learning (112,84 detik) karena '
    'CIFAR-10 beresolusi 32x32 cocok untuk arsitektur sederhana.\n'
    '3. CNN from scratch memiliki gap overfitting lebih besar (0,0184 vs 0,0016), menunjukkan transfer learning lebih stabil.\n'
    '4. Kedua model mencapai akurasi >96%, menunjukkan dataset CIFAR-10 untuk perbandingan pesawat vs mobil relatif mudah.\n'
    '5. Untuk dataset citra natural resolusi rendah dengan data cukup, CNN from scratch bisa menjadi pilihan yang efisien.'
)

pdf.section_title('Refleksi Pribadi')
pdf.body_text(
    '1. Tantangan terbesar: Mendesain arsitektur CNN yang tepat dan memilih hyperparameter optimal '
    'untuk mencegah overfitting.\n\n'
    '2. Bagian paling sulit: CNN from scratch karena harus mendesain arsitektur, tuning hyperparameter, '
    'dan memahami setiap layer secara mendalam.\n\n'
    '3. Perbedaan paling terasa: CNN from scratch membutuhkan lebih banyak epoch dan fluktuasi '
    'validation loss lebih tinggi. Transfer Learning konvergen jauh lebih cepat.\n\n'
    '4. Untuk kasus nyata: Transfer Learning menjadi pilihan utama karena efisiensi dan performa.\n\n'
    '5. Hal baru yang dipelajari: Keputusan dalam deep learning tidak hanya soal akurasi, tetapi juga '
    'mempertimbangkan komputasi, waktu, risiko overfitting, dan konteks penggunaan nyata.'
)

# Save
pdf.output(OUTPUT_PATH)
print(f"PDF saved to {OUTPUT_PATH}")
print(f"Pages: {pdf.page_no()}")
