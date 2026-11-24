a, b = 0b1100, 0b1010

# Operator bitwise membandingkan setiap posisi bit pada bilangan bulat.
print("AND:", bin(a & b), "OR:", bin(a | b), "XOR:", bin(a ^ b))
print("Geser kiri:", bin(a << 1), "Geser kanan:", bin(a >> 1))