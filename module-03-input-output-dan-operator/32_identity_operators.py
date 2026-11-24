angka = [1, 2]
alias = angka
salinan = angka.copy()

# == membandingkan isi, sedangkan is membandingkan identitas objek.
print("Isi sama:", angka == salinan)
print("Objek sama (alias):", angka is alias)
print("Objek sama (salinan):", angka is salinan)