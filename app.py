import streamlit as st

score_designer = 0
score_data_scientist = 0
score_programmer = 0

designer_qna ={
    "Apakah aplikasi web untuk desain interface": ["Excel", "Radeon", "Figma", "Phyton"],
    "Apakah aplikasi untuk membuat animasi": ["Adobe Photoshop", "Adobe Illustrator", "Adobe After Effects", "Adobe Premiere Pro"],
    "Apa itu UX design dalam konteks pengembangan web": ["Proses yang berfokus pada tampilan visual sebuah website", "Desain yang memprioritaskan kemudahan dan kenyamanan pengguna dalam berinteraksi dengan website", "Desain yang mengutamakan kecepatan loading website", "Desain yang fokus pada struktur hierarki kode HTML"],
    'Apa yang dimaksud dengan "responsive design" dalam pengembangan website': ["Desain yang hanya dapat dilihat di perangkat desktop", "Desain yang menyesuaikan tampilan website sesuai dengan ukuran layar perangkat", "Desain yang hanya menggunakan gambar sebagai elemen utama", "Desain yang tidak memerlukan CSS untuk tampilan"],
    "Apa fungsi dari CSS dalam pembuatan website": ["Mengatur struktur konten di dalam website", "Menyimpan data pengguna", "Mengubah tampilan dan gaya visual elemen HTML", "Menyediakan fungsionalitas interaktif pada website"],
}

data_scientist_qna ={
    'Apa yang dimaksud dengan "overfitting" dalam model machine learning?': [
        'Model yang sangat baik dalam memprediksi data baru', 
        'Model yang terlalu sederhana sehingga tidak dapat memodelkan data dengan baik', 
        'Model yang terlalu kompleks dan cocok dengan data latih, tetapi gagal pada data uji', 
        'Model yang hanya digunakan untuk mengolah data yang tidak terstruktur'
    ],
    'Apa fungsi utama dari "feature engineering" dalam machine learning?': [
        'Menambahkan lebih banyak data latih untuk meningkatkan akurasi model', 
        'Menggunakan data yang sudah ada untuk membuat fitur baru yang lebih informatif', 
        'Menghapus data yang tidak relevan dari dataset', 
        'Menggunakan model yang lebih kompleks untuk memperbaiki akurasi'
    ],
    'Apa yang dimaksud dengan "supervised learning" dalam machine learning?': [
        'Teknik pembelajaran di mana model belajar dari data yang tidak memiliki label', 
        'Teknik pembelajaran di mana model belajar dari data yang memiliki label atau hasil yang diketahui', 
        'Teknik pembelajaran di mana model tidak memerlukan data pelatihan', 
        'Teknik pembelajaran di mana model hanya menggunakan data unstructured'
    ],
    'Apa itu "random fores" dalam machine learning?': [
        'Model yang menggunakan satu pohon keputusan untuk memprediksi hasil', 
        'Algoritma pengklasifikasi yang menggabungkan beberapa pohon keputusan untuk meningkatkan akurasi', 
        'Algoritma yang hanya menggunakan satu jenis fitur dalam pengklasifikasian', 
        'Model yang digunakan untuk pemrosesan data teks'
    ],
    'Dalam analisis data, apa yang dimaksud dengan "outlier"?': [
        'Data yang terletak di tengah distribusi data', 
        'Data yang terpisah jauh dari pola umum data lainnya', 
        'Data yang merupakan rata-rata dari seluruh dataset', 
        'Data yang terletak di titik maksimum atau minimum dari dataset'
    ]
}

programmer_qna ={
    'Apa yang dimaksud dengan "version control" dalam pengembangan perangkat lunak?': [
        "Proses untuk mendokumentasikan kode yang ditulis oleh programmer", 
        "Sistem untuk mengelola perubahan kode sumber dan melacak versi kode", 
        "Proses untuk mengonversi kode menjadi bentuk mesin", 
        "Alat untuk menguji kinerja aplikasi"
    ],
    'Apa itu "refactoring" dalam pengembangan perangkat lunak?': [
        "Menulis ulang seluruh kode dari awal", 
        "Mengubah kode untuk meningkatkan kualitasnya tanpa mengubah perilaku eksternal", 
        "Menambahkan fitur baru dalam aplikasi", 
        "Menghapus kode yang tidak diperlukan"
    ],
    'Apa perbedaan utama antara "procedural programming" dan "object-oriented programming"?': [
        '"Procedural programming" lebih fokus pada penggunaan objek, sedangkan "object-oriented programming" lebih fokus pada prosedur', 
        '"Object-oriented programming" berfokus pada objek dan kelas, sedangkan "procedural programming" berfokus pada prosedur dan fungsi', 
        '"Procedural programming" lebih efisien daripada "object-oriented programming"', 
        'Tidak ada perbedaan antara keduanya'
    ],
    'Apa itu "API" dalam pengembangan perangkat lunak?': [
        "Protokol untuk menghubungkan perangkat keras dengan perangkat lunak", 
        "Sistem untuk memanage basis data secara efisien", 
        "Antarmuka yang memungkinkan aplikasi untuk berkomunikasi dengan sistem atau aplikasi lainnya", 
        "Teknik untuk mengamankan aplikasi web"
    ],
    'Dalam pemrograman, apa tujuan utama dari "unit testing"?': [
        "Untuk memastikan kode berjalan dengan baik di seluruh platform", 
        "Untuk menguji bagian terkecil dari aplikasi (misalnya fungsi atau metode) secara terpisah dari bagian lainnya", 
        "Untuk mengoptimalkan kinerja aplikasi", 
        "Untuk mendokumentasikan kode yang telah ditulis"
    ]
}


st.title(":blue[Mini Quiz App] - Menentukan Profesi yang Cocok Untuk Anda :thumbsup:")

st.logo(
    image ="https://torrentfreak.com/images/amelie2-600x374.jpg",
    size="large",
    link="https://torrentfreak.com/images/amelie2-600x374.jpg",
    
)

st.title("Quiz :red[Designer] :thumbsup:")

for q, options in designer_qna.items():
    user_answer = st.radio(q, options=options, key=q) 
    if user_answer:
        if user_answer == "Figma": 
            
            score_designer += 1
        if user_answer == "Adobe Premiere Pro": 
            
            score_designer += 1
        if user_answer == "Desain yang memprioritaskan kemudahan dan kenyamanan pengguna dalam berinteraksi dengan website": 
            
            score_designer += 1
        if user_answer == "Desain yang menyesuaikan tampilan website sesuai dengan ukuran layar perangkat": 
            
            score_designer += 1
        if user_answer == "Mengubah tampilan dan gaya visual elemen HTML": 
            
            score_designer += 1

st.title("Tech-nical Quiz :grey[Data Scientist] :thumbsup:")
        
for q, options in data_scientist_qna.items():
    user_answer = st.radio(q, options=options, key=q) 
    if user_answer:
        if user_answer == "Model yang terlalu kompleks dan cocok dengan data latih, tetapi gagal pada data uji": 
            
            score_data_scientist += 1
        if user_answer == "Menggunakan data yang sudah ada untuk membuat fitur baru yang lebih informatif": 
            
            score_data_scientist += 1
        if user_answer == "Teknik pembelajaran di mana model belajar dari data yang memiliki label atau hasil yang diketahui": 
            
            score_data_scientist += 1
        if user_answer == "Algoritma pengklasifikasi yang menggabungkan beberapa pohon keputusan untuk meningkatkan akurasi": 
            
            score_data_scientist += 1
        if user_answer == "Data yang terpisah jauh dari pola umum data lainnya": 
            
            score_data_scientist += 1

st.title("Quiz :green[Programmer] :thumbsup:")
        
for q, options in programmer_qna.items():
    user_answer = st.radio(q, options=options, key=q) 
    if user_answer:
        if user_answer == 'Sistem untuk mengelola perubahan kode sumber dan melacak versi kode': 
            
            score_programmer += 1
        if user_answer == 'Mengubah kode untuk meningkatkan kualitasnya tanpa mengubah perilaku eksternal': 
            
            score_programmer += 1
        if user_answer == '"Object-oriented programming" berfokus pada objek dan kelas, sedangkan "procedural programming" berfokus pada prosedur dan fungsi': 
            
            score_programmer += 1
        if user_answer == 'Antarmuka yang memungkinkan aplikasi untuk berkomunikasi dengan sistem atau aplikasi lainnya': 
            
            score_programmer += 1
        if user_answer == 'Untuk menguji bagian terkecil dari aplikasi (misalnya fungsi atau metode) secara terpisah dari bagian lainnya': 
            
            score_programmer += 1
            

if st.button("Lihat Skor"):
    st.write("Score Designer:", score_designer)
    st.write("Score Data Scientist:", score_data_scientist)
    st.write("Score Programmer:", score_programmer)
    
    if score_programmer >= 3 and score_data_scientist >= 3 and score_designer >= 3:
        st.success("Luar Biasa! Kamu memiliki potensi menjadi seorang Designer, Data Scientist dan Programmer!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTgyYTE0OTNiYzlsZWk1MHlnanNybWNwNzN2dm93Nmx4NzFkZmNqNTJsNnhvaGNxbCZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/tHIRLHtNwxpjIFqPdV/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    elif score_programmer >= 3 and score_data_scientist >= 3 and score_designer < 3:
        st.success("Hebat! Kamu memiliki potensi menjadi seorang Data Scientist dan Programmer!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXRqamJrbXNxNXp5b25zdHN6NGVsanR0dml0ZHNraXVqa2U1NXBkayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jQPocZMaXEer4VLr5j/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    elif score_programmer >= 3 and score_data_scientist < 3 and score_designer >= 3:
        st.success("Hebat! Kamu memiliki potensi menjadi seorang Designer dan Programmer!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXRqamJrbXNxNXp5b25zdHN6NGVsanR0dml0ZHNraXVqa2U1NXBkayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jQPocZMaXEer4VLr5j/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    elif score_programmer < 3 and score_data_scientist >= 3 and score_designer >= 3:
        st.success("Hebat! Kamu memiliki potensi menjadi seorang Designer dan Data Scientist!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXRqamJrbXNxNXp5b25zdHN6NGVsanR0dml0ZHNraXVqa2U1NXBkayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jQPocZMaXEer4VLr5j/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    elif score_programmer < 3 and score_data_scientist < 3 and score_designer >= 3:
        st.success("Selamat! Kamu memiliki potensi menjadi seorang Designer!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpzN2wydHhvN24wcGxzNWd4eGFzdXd4YnZzcjgwY2s4NWIyOWs2bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vnADEzbST1i9Judtoq/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    elif score_programmer >= 3 and score_data_scientist < 3 and score_designer < 3:
        st.success("Selamat! Kamu memiliki potensi menjadi seorang Programmer!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpzN2wydHhvN24wcGxzNWd4eGFzdXd4YnZzcjgwY2s4NWIyOWs2bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vnADEzbST1i9Judtoq/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    elif score_programmer < 3 and score_data_scientist >= 3 and score_designer < 3:
        st.success("Selamat! Kamu memiliki potensi menjadi seorang Data Scientist!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpzN2wydHhvN24wcGxzNWd4eGFzdXd4YnZzcjgwY2s4NWIyOWs2bSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/vnADEzbST1i9Judtoq/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    else:
        st.error("Maaf silahkan coba lagi!")
        st.image(image="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3M0bzNha2R4bzdrcDlpZXExNnc3bHlwMXl5dmFkNzIzOGpxdnF5OCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/wZxmFSn2CMS2MTev4Y/giphy.gif", caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

        