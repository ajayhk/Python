import numpy as np
from numpy import linalg as la
from scipy.spatial import distance
from sklearn.metrics.pairwise import cosine_similarity

A = np.random.normal(0, 1, size=(300, 300))
B = np.random.normal(0, 1, size=(300, 300))
C = A.dot(B)
A_norm = la.norm(A)
B_norm = la.norm(B)
cos_sim = cosine_similarity(A, B)
print (cos_sim)
