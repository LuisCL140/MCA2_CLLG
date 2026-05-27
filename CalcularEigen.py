"""
    Obtencion de eigenvalores y eigenvectores de la tarea 6 
    @author Luis Gustavo Cortes Leon
    @version 22-04-2026
    
    a) x + 1/2y + 1/3z = 1
        1/2x + 1/3y + 1/4z = 0
        1/3x + 1/4y + 1/5z = 0
        
    Escribimos su matriz asociada 
     ((1, 1/2, 1/3)  ,
       (1/2, 1/3, 1/4)  ,
        (1/3, 1/4, 1/5))
        
        
    b) x1 + x2 + x3 + x4 = 10
        1.01x1 + 1.02x2 + 1.03x3 + 1.04x4 = 20 
            1.01^2x1 + 1.02^2x2 + 1.03^2x3 + 1.04^2x4 = 30
            1.01^3x1 + 1.02^3x2 + 1.02^3x3 + 1.04^3x4 = 40
        
    Escribimos su matriz asociada 
     ((1, 1, 1 ,1) ,
       (1.01, 1.02, 1.03, 1.04)  ,
            (1.01^2, 1.02^2, 1.03^2, 1.04^2),
                 1.01^3x1, 1.02^3, 1.02^3 1.04^3))
    
    c) x + 2y = 3
        2x + 4.0001y = 6.0001  
        
    Escribimos su matriz asociada 
     ((1, 2), 
        (2, 4.0001))
        
        Como es de la forma Ax = b
         
"""

import numpy as np

# Matriz A del inciso a)
A = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
], dtype=float)

# Eigenvalores y eigenvectores
eigenvalores, eigenvectores = np.linalg.eig(A)

print("Eigenvalores a):")
print(eigenvalores)

print("\nEigenvectores a):")
print(eigenvectores)

# Valores base
x = np.array([1.01, 1.02, 1.03, 1.04])

# Construcción de la matriz A inciso b)
A = np.vander(x, increasing=True)

# Eigenvalores y eigenvectores
eigenvalores, eigenvectores = np.linalg.eig(A)

print("Eigenvalores b):")
print(eigenvalores)

print("\nEigenvectores b):")
print(eigenvectores)

# Matriz A del inciso c)
C = np.array([
    [1, 2],
    [2, 4.0001],
], dtype=float)

# Eigenvalores y eigenvectores
eigenvalores, eigenvectores = np.linalg.eig(C)

print("Eigenvalores c):")
print(eigenvalores)

print("\nEigenvectores c):")
print(eigenvectores)