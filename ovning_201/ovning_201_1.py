import numpy as np

def get_element(mat_A: np.ndarray, mat_B: np.ndarray, i: int, j: int) -> float:
    """
    Parametrar:
        mat_A och mat_B: matriser av typen ndarray
        i och j: rad- och kolonnindex, 1-baserat
    Returvärde:
        Givet att matriserna är multiplicerbara:
            talet på den önskade positionen
        Givet att matriserna inte är multiplicerbara:
            None
    """
    if mat_A.shape[1] != mat_B.shape[0]:  
        return None 
    
    c_ij = sum(map(lambda a, b: a*b, mat_A[i-1,:], mat_B[:,j-1]))
    return c_ij

# Ingångsvärden, kan förändras
A = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3-matris
B = np.array([[2, 3], [4, 5], [6, 7]])  # 3x2-matris
i, j = 2, 1  # Sökt index, rad och kolonn

# Ändra inget under denna rad,
# men ta gärna inspiration till det som
# behöver skrivas i funktionen get_element.
number_of_rows_in_A = A.shape[0]
number_of_cols_in_B = B.shape[1]

if i <= number_of_rows_in_A and i > 0 and j <= number_of_cols_in_B and j > 0:
    c_ij = get_element(A, B, i, j)
    if c_ij != None:
        # Skriver ut talet 64 givet
        # ingångsvärdena som de var från början
        print(c_ij)
    else:
        print("De angivna matriserna är inte multiplicerbara med varandra")
else:
    print("Begärt index finns ej i resultatmatrisen")
print("Programmet avslutades normalt")





"""
De senare alternativet ger en "dellista" som innehåller raderna respektive kolonnerna, antalet element i dessa listor (`len`) blir då antalet rader respektive kolonner. Ibland kan själva innehållet i dellistan vara intressant, nu vet ni hur det erhålls!

En annan vanlig operation är att *transponera* matriser. Detta fungerar så här:
"""

# A = np.array([[a11, a12], [a21, a22]])
# A är nu
# [[a11, a12],
#  [a21, a22]]

# Transponera nu A:
A = A.T
# A är nu
# [[a11, a21],
#  [a12, a22]]
# dvs raderna blir kolonner och vice versa.
