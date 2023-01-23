import numpy as np


def get_angle(a,b,c):
    a = np.array([6,0])
    b = np.array([0,0])
    c = np.array([0,6])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)