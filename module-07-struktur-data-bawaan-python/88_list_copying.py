asli = [1, 2]
alias = asli
salinan = asli.copy()

# append lewat alias mengubah list asli; salinan dangkal tetap list yang terpisah.
alias.append(3)
print("Asli:", asli)
print("Salinan:", salinan)