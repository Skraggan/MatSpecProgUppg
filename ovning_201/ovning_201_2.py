import numpy as np
from ovning_201_1 import get_element

def make_mat_product(mat_A: np.ndarray, mat_B: np.ndarray) -> np.ndarray:
    '''
    Parametrar:
        mat_A och mat_B: matriser av typen ndarray
    Returvärde:
        Givet att matriserna är multiplicerbara:
            matris av typen ndarray, som utgör
            matrisprodukten
        Givet att matriserna inte är multiplicerbara:
             None
    '''
    if mat_A.shape[1] != mat_B.shape[0]:  
            return None 

    mat_C = np.zeros((mat_A.shape[0], mat_B.shape[1]))
    
    # Implementation av Definition 2.2.1 från den blåa linjär algebra boken
    for r in range(mat_C.shape[0]):
        for c in range(mat_C.shape[1]):
            mat_C[r,c] = get_element(mat_A, mat_B, r+1, c+1)

    return mat_C

# Ingångsvärden, kan förändras
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3-matris
B = np.array([[2, 3], [4, 5], [6, 7]])  # 3x2-matris

# Ändra inget under denna rad,
C = make_mat_product(A, B)
if C is None:
    print("De angivna matriserna är inte multiplicerbara med varandra")
else:
    print(f"C =\n {C}")
    # Skriver ut
    # [[28. 34.]
    # [64. 79.]]
    # givet matriserna A och B som de var från början
print("Programmet avslutades normalt")

"""
Som du ser i kodskelettet ovan så ska du använda dig av den tidigare implementerade funktionen `get_element` när matrisen skapas (om den går att skapa, förstås). I exemplet skapas också en initial resultatmatris, med rätt antal rader och kolonner, som fylls med nollor. För att ändra en nolla till ett annat värde så kan följande utföras:


result[i, j] = nytt_tal

Dessa `i` (radindex) och `j` (kolonnindex) är matrisens index; dessa index startar på noll.
"""