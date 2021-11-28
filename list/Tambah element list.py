print('Tambah element list')
print()

# ambil bagian list pertama
A = [12,14,16,18,20]
B = [21, 23, 25, 27,29]
B.append (A[0:2])
print(B)
print()

#tambah list b dengan string
B.append('23')
print(B)
print()

#tambah list b dengan 3 nilai
print(B + [32, 15, 12])
print()

#gabungkan list a dengan list b
print(A+B)