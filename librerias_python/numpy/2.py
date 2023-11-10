import numpy as np
mi_array = np.array([1, 2, 3])
print(mi_array) #[1 2 3]
print(type(mi_array)) #<class 'numpy.ndarray'>

#dimension cero
mi_array = np.array(11)
print(mi_array) #11
print(type(mi_array)) #<class 'numpy.ndarray'>

#dimension uno
mi_array = np.array([1, 3, 5, 7]) 
print(mi_array) #[1 3 5 7]
print(type(mi_array)) #<class 'numpy.ndarray'>

#dimension dos
mi_array = np.array([[1, 3, 5, 7], [2, 4, 6, 8]]) 
print(mi_array) #[[1 3 5 7]
                 #[2 4 6 8]]
print(type(mi_array)) #<class 'numpy.ndarray'>

#dimension tres
mi_array = np.array([[[1, 2, 3],[4, 5, 6]], [[1, 2, 3],[4, 5, 6]]]) 
print(mi_array) #[[[1 2 3]
                  #[4 5 6]]
                 #[[1 2 3]
                  #[4 5 6]]]
print(type(mi_array)) #<class 'numpy.ndarray'>

#multiples dimensiones
mi_array = np.array([1, 2, 3])
print(mi_array) #
print(type(mi_array)) #<class 'numpy.ndarray'>