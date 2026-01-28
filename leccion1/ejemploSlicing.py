
import copy
original = [[1,2,3],"A","B"]

deep_copia_slice = copy.deepcopy(original)
deep_copia_slice[1] = "Z"

copia_slice = original[:]
copia_slice[1] = "Z"

print(f"original: {original}")
copia_slice[0][0] = 99
print(f"original: {original}")
print(f"copia slice: {copia_slice}")
print(f"Deep copia slice: {deep_copia_slice}")
