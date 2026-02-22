from ctypes import CDLL, Structure, POINTER, byref
from cpy_objs import cpy_objs
from .Vector import Vector
from .Dipole import Dipole

Dipoles_c = CDLL(r"C:/Users/joses/OneDrive/Desktop/Code/PhysicsObjs/PhysicsObjs/c_objs/so/Dipoles_c.dll")

Dipoles_c.addVectors.restype = Vector
Dipoles_c.scaleVector.restype = Vector
Dipoles_c.magnitude.restype = cpy_objs.float64
Dipoles_c.subVectors.restype = Vector