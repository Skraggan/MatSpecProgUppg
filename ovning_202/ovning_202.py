import numpy as np
import itertools
from operator import mul

def dot_product(vec_1, vec_2):
    '''
    Parametrar:
        vec_1: en vektor av typen ndarray
        vec_2: en vektor av typen ndarray
    Returvärde:
        Om vektorerna går att multiplicera skalärt:
            Skalärprodukten
        Om vektorerna inte går att multiplicera skalärt:
            None
    Övrigt: Denna funktion bygger inte på NumPy:s implementering
    av skalärprodukt.
    '''

    # Implementera koden nedan
    if (vec_1.shape != vec_2.shape): # TODO: kolla så de är 1-dimentionella
        return None
    result = sum(map(mul, vec_1, vec_2))
    return result

def is_orthogonal(koord_axlar):
    '''
    Parameter:
        koord_axlar: en matris av typen ndarray som
        definierar de båda koordinat-axlarnas riktning i kolonnerna
    Returvärde:
        Om ortogonala axlar: True
        Om ej ortogonala axlar: False
    '''
    result = False
    result = not dot_product(koord_axlar[:,0], koord_axlar[:,1])
    return result

def calc_proj(vektor, koord_axlar):
    '''
    Parametrar:
        vektor: en vektor med två komponenter av typen ndarray
        koord_axlar: en matris av typen ndarray som definierar
        de båda koordinat-axlarnas riktning i kolonnerna
    Returvärde:
        En matris av typen ndarray som innehåller projektionen
        på respektive koordinataxel i kolonnerna
    '''
    result = np.zeros([2, 2])
    
    y = vektor.flatten()
    u1, u2 = koord_axlar[0,:], koord_axlar[1,:]
    yu1 = dot_product(y, u1) * u1 / dot_product(u1, u1) 
    yu2 = dot_product(y, u2) * u2 / dot_product(u2, u2)

    result = np.c_[yu1, yu2]
    return result

# Test-exempel
y = np.array([[3], [2]])
u1 = np.array([4, 1])
u2 = np.array([-1, 4])
u = np.array([u1.T, u2.T])
# Kontrollera hur y och u skrivs ut
# INNAN du börjar skriva funktionerna

### Ändra inget under denna rad
if is_orthogonal(u):
    proj = calc_proj(y, u)
    print(proj.round(2))
    # För en fungerande funktion och givna
    # data enligt räkneexemplet så skrivs ut:
    # [[3.29, -0.29],
    # [0.82, 1.18]]

    print("Längden på ovanstående projektionsvektorer:")
    norm_u1 = round(np.linalg.norm(proj[:, 0]), 2)
    norm_u2 = round(np.linalg.norm(proj[:, 1]), 2)
    print(f"||u1|| = {norm_u1}")  # Blir 3.4
    print(f"||u2|| = {norm_u2}")  # Blir 1.21
else:
    print("Angivna koordinataxlar är inte ortogonala.")