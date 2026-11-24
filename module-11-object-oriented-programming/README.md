# Modul 11 — Object-Oriented Programming (OOP)

Modul ini mengajarkan class, instance, atribut, method, pewarisan, komposisi, serta protokol objek Python. Tujuannya adalah memahami bagaimana perilaku dan data terkait dalam objek, termasuk fitur lanjutan yang dipakai hanya saat diperlukan. Semua contoh memakai Python 3.10+ dan standard library. Jalankan setiap perintah dari folder modul ini. Screenshot jendela log eksekusi ditautkan di setiap submodul.

## Daftar materi

1. [Class dan object](144_class_basic.py)
2. [Instance attributes](145_instance_attributes.py)
3. [Class attributes](146_class_attributes.py)
4. [Instance methods](147_instance_methods.py)
5. [Class methods](148_class_methods.py)
6. [Static methods](149_static_methods.py)
7. [Constructor](150_constructor_init.py)
8. [String representation](151_string_representation.py)
9. [Encapsulation](152_encapsulation.py)
10. [Property dan setter](153_properties.py)
11. [Inheritance](154_inheritance.py)
12. [Multiple inheritance](155_multiple_inheritance.py)
13. [Method overriding](156_method_overriding.py)
14. [Polymorphism](157_polymorphism.py)
15. [Abstract classes](158_abstract_classes.py)
16. [Composition](159_composition.py)
17. [Operator overloading](160_operator_overloading.py)
18. [Dunder methods](161_dunder_methods.py)
19. [Dataclass](162_dataclass_basic.py)
20. [Enum](163_enum_class.py)
21. [Slots](164_slots.py)
22. [Descriptor protocol](165_descriptors.py)
23. [Metaclass](166_metaclasses.py)
24. [Method Resolution Order](167_mro_method_resolution.py)

### 144. Class dan object
**Tujuan:** Membuat instance dari class. **Konsep dan cara kerja:** class Kucing menyediakan metode `mengeong`, lalu instance memanggilnya. **Jalankan:** `python 144_class_basic.py`. **Hasil:** `Meong!`. **Source code:** [144_class_basic.py](144_class_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/144_class_basic.png).

### 145. Instance attributes
**Tujuan:** Memisahkan data per objek. **Konsep dan cara kerja:** `self.nama` pada tiap Murid diisi oleh constructor secara independen. **Jalankan:** `python 145_instance_attributes.py`. **Hasil:** Ayu dan Budi. **Source code:** [145_instance_attributes.py](145_instance_attributes.py). **Screenshot:** [Lihat hasil eksekusi](output/145_instance_attributes.png).

### 146. Class attributes
**Tujuan:** Memahami nilai bersama pada class. **Konsep dan cara kerja:** `pi` tersedia pada Lingkaran; radius disimpan terpisah pada instance. **Jalankan:** `python 146_class_attributes.py`. **Hasil:** luas lingkaran radius 2. **Source code:** [146_class_attributes.py](146_class_attributes.py). **Screenshot:** [Lihat hasil eksekusi](output/146_class_attributes.png).

### 147. Instance methods
**Tujuan:** Mengubah state objek lewat metode. **Konsep dan cara kerja:** `setor` menggunakan `self` untuk menambah saldo instance rekening. **Jalankan:** `python 147_instance_methods.py`. **Hasil:** saldo 150. **Source code:** [147_instance_methods.py](147_instance_methods.py). **Screenshot:** [Lihat hasil eksekusi](output/147_instance_methods.png).

### 148. Class methods
**Tujuan:** Menyediakan pembuat instance alternatif. **Konsep dan cara kerja:** `@classmethod` menerima `cls`, mengonversi teks harga, lalu membuat Produk. **Jalankan:** `python 148_class_methods.py`. **Hasil:** harga 100. **Source code:** [148_class_methods.py](148_class_methods.py). **Screenshot:** [Lihat hasil eksekusi](output/148_class_methods.png).

### 149. Static methods
**Tujuan:** Mengelompokkan fungsi yang tidak butuh `self` atau `cls`. **Konsep dan cara kerja:** `genap` menguji sisa bagi tanpa membaca state Matematika. **Jalankan:** `python 149_static_methods.py`. **Hasil:** `True` untuk 8. **Source code:** [149_static_methods.py](149_static_methods.py). **Screenshot:** [Lihat hasil eksekusi](output/149_static_methods.png).

### 150. Constructor melalui `__init__`
**Tujuan:** Menginisialisasi data sebelum dipakai. **Konsep dan cara kerja:** constructor menyimpan sisi sehingga `luas` dapat menghitung kuadratnya. **Jalankan:** `python 150_constructor_init.py`. **Hasil:** luas 16. **Source code:** [150_constructor_init.py](150_constructor_init.py). **Screenshot:** [Lihat hasil eksekusi](output/150_constructor_init.png).

### 151. `__str__` dan `__repr__`
**Tujuan:** Membedakan tampilan untuk pembaca dan debugging. **Konsep dan cara kerja:** kedua metode mengembalikan teks representasi Buku yang berbeda. **Jalankan:** `python 151_string_representation.py`. **Hasil:** `Buku: Python` serta `Buku('Python')`. **Source code:** [151_string_representation.py](151_string_representation.py). **Screenshot:** [Lihat hasil eksekusi](output/151_string_representation.png).

### 152. Encapsulation
**Tujuan:** Mengendalikan perubahan saldo melalui metode. **Konsep dan cara kerja:** `__saldo` memakai name mangling; `tarik` hanya memproses jumlah positif yang mencukupi. **Jalankan:** `python 152_encapsulation.py`. **Hasil:** saldo 70. **Source code:** [152_encapsulation.py](152_encapsulation.py). **Screenshot:** [Lihat hasil eksekusi](output/152_encapsulation.png).

### 153. Property dan setter
**Tujuan:** Memvalidasi assignment atribut. **Konsep dan cara kerja:** property membaca `_harga`, setter menolak nilai negatif baik saat dibuat maupun diubah. **Jalankan:** `python 153_properties.py`. **Hasil:** harga 75. **Source code:** [153_properties.py](153_properties.py). **Screenshot:** [Lihat hasil eksekusi](output/153_properties.png).

### 154. Inheritance
**Tujuan:** Menggunakan perilaku parent. **Konsep dan cara kerja:** Anjing mewarisi `bersuara` dari Hewan tanpa menulis metode baru. **Jalankan:** `python 154_inheritance.py`. **Hasil:** `Suara hewan`. **Source code:** [154_inheritance.py](154_inheritance.py). **Screenshot:** [Lihat hasil eksekusi](output/154_inheritance.png).

### 155. Multiple inheritance
**Tujuan:** Menggabungkan dua perilaku parent. **Konsep dan cara kerja:** Bebek mewarisi `berenang` dan `terbang` dari dua class berbeda. **Jalankan:** `python 155_multiple_inheritance.py`. **Hasil:** `Berenang Terbang`. **Source code:** [155_multiple_inheritance.py](155_multiple_inheritance.py). **Screenshot:** [Lihat hasil eksekusi](output/155_multiple_inheritance.png).

### 156. Method overriding
**Tujuan:** Mengubah perilaku parent di subclass. **Konsep dan cara kerja:** Kucing mendefinisikan kembali `bersuara`, sedangkan Hewan mempertahankan perilaku asal. **Jalankan:** `python 156_method_overriding.py`. **Hasil:** `Suara hewan Meong`. **Source code:** [156_method_overriding.py](156_method_overriding.py). **Screenshot:** [Lihat hasil eksekusi](output/156_method_overriding.png).

### 157. Polymorphism
**Tujuan:** Memanggil antarmuka sama pada tipe berbeda. **Konsep dan cara kerja:** loop memanggil `bersuara` tanpa memeriksa apakah objek Kucing atau Anjing. **Jalankan:** `python 157_polymorphism.py`. **Hasil:** Meong lalu Guk. **Source code:** [157_polymorphism.py](157_polymorphism.py). **Screenshot:** [Lihat hasil eksekusi](output/157_polymorphism.png).

### 158. Abstract classes
**Tujuan:** Mensyaratkan implementasi metode pada class konkret. **Konsep dan cara kerja:** Bentuk mendeklarasikan `luas` abstrak; Persegi mengimplementasikannya. **Jalankan:** `python 158_abstract_classes.py`. **Hasil:** luas 9. **Source code:** [158_abstract_classes.py](158_abstract_classes.py). **Screenshot:** [Lihat hasil eksekusi](output/158_abstract_classes.png).

### 159. Composition
**Tujuan:** Membedakan relasi memiliki dari mewarisi. **Konsep dan cara kerja:** Mobil menyimpan instance Mesin dan memakai metode objek tersebut. **Jalankan:** `python 159_composition.py`. **Hasil:** `Mesin hidup`. **Source code:** [159_composition.py](159_composition.py). **Screenshot:** [Lihat hasil eksekusi](output/159_composition.png).

### 160. Operator overloading
**Tujuan:** Mendefinisikan makna `+` untuk objek sendiri. **Konsep dan cara kerja:** `__add__` menjumlahkan tiap komponen Vektor dan mengembalikan `NotImplemented` untuk tipe lain. **Jalankan:** `python 160_operator_overloading.py`. **Hasil:** vektor 4, 6. **Source code:** [160_operator_overloading.py](160_operator_overloading.py). **Screenshot:** [Lihat hasil eksekusi](output/160_operator_overloading.png).

### 161. Dunder methods
**Tujuan:** Memanfaatkan operasi bawaan untuk instance. **Konsep dan cara kerja:** `__len__` melayani `len`; `__contains__` melayani operator `in`. **Jalankan:** `python 161_dunder_methods.py`. **Hasil:** jumlah 2, buku ada. **Source code:** [161_dunder_methods.py](161_dunder_methods.py). **Screenshot:** [Lihat hasil eksekusi](output/161_dunder_methods.png).

### 162. `dataclass`
**Tujuan:** Membuat class data tanpa constructor manual. **Konsep dan cara kerja:** dekorator menghasilkan representasi dan pembandingan nilai otomatis. **Jalankan:** `python 162_dataclass_basic.py`. **Hasil:** Titik(2, 3) dan kesetaraan `True`. **Source code:** [162_dataclass_basic.py](162_dataclass_basic.py). **Screenshot:** [Lihat hasil eksekusi](output/162_dataclass_basic.png).

### 163. `Enum`
**Tujuan:** Membatasi status pada anggota bernama. **Konsep dan cara kerja:** anggota `Status.BARU` menyediakan `.name` dan `.value`. **Jalankan:** `python 163_enum_class.py`. **Hasil:** nama BARU dan nilai `baru`. **Source code:** [163_enum_class.py](163_enum_class.py). **Screenshot:** [Lihat hasil eksekusi](output/163_enum_class.png).

### 164. `__slots__`
**Tujuan:** Membatasi nama atribut instance. **Konsep dan cara kerja:** Titik hanya mendefinisikan `x` dan `y`; instance biasa tidak memiliki `__dict__` pada contoh ini. **Jalankan:** `python 164_slots.py`. **Hasil:** koordinat 2, 3; `Punya __dict__: False`. **Source code:** [164_slots.py](164_slots.py). **Screenshot:** [Lihat hasil eksekusi](output/164_slots.png).

### 165. Descriptor protocol
**Tujuan:** Mengatur pembacaan dan assignment satu atribut lintas instance. **Konsep dan cara kerja:** Positif memakai `__set_name__`, `__get__`, dan `__set__` untuk memvalidasi sisi Persegi. **Jalankan:** `python 165_descriptors.py`. **Hasil:** sisi 4. **Source code:** [165_descriptors.py](165_descriptors.py). **Screenshot:** [Lihat hasil eksekusi](output/165_descriptors.png).

### 166. Metaclass
**Tujuan:** Mengetahui bahwa class juga dibuat oleh objek bertipe metaclass. **Konsep dan cara kerja:** `CatatNama.__new__` menambahkan nama class saat Produk didefinisikan. **Jalankan:** `python 166_metaclasses.py`. **Hasil:** nama class Produk. **Source code:** [166_metaclasses.py](166_metaclasses.py). **Screenshot:** [Lihat hasil eksekusi](output/166_metaclasses.png).

### 167. Method Resolution Order
**Tujuan:** Memahami urutan pencarian metode pada pewarisan ganda. **Konsep dan cara kerja:** Gabungan mengutamakan Kiri, lalu Kanan, sebelum Dasar; `__mro__` memperlihatkan urutannya. **Jalankan:** `python 167_mro_method_resolution.py`. **Hasil:** metode Kiri dan daftar urutan class. **Source code:** [167_mro_method_resolution.py](167_mro_method_resolution.py). **Screenshot:** [Lihat hasil eksekusi](output/167_mro_method_resolution.png).

## Ringkasan

Class mengelompokkan data dan metode, sedangkan pewarisan dan komposisi menghubungkan perilaku. Metode khusus memberi objek integrasi dengan operator serta protokol bawaan Python.