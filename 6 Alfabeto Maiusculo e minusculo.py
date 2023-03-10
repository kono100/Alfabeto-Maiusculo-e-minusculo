import string as st
letras = st.ascii_uppercase

print("\nMAIÚSCULAS")
print(70*'-')
print(f"{letras}\n")

temp_string2 = letras
space_string2 = ' '.join(temp_string2) + ' '
print(space_string2)
print(70*'-')

#Letras minusculas
print("minúsculas")
print(70*'-')
print(letras.lower())
print()

temp_string2 = letras.lower()
space_string2 = ' '.join(temp_string2) + ' '
print(space_string2)
print()