from .Vector import Vector
from cpy_objs import cpy_objs

class Dipole(cpy_objs.Structure):
	_fields_ = [
	("dir", Vector),
	("charge", cpy_objs.float32),
	]
	def __init__(self, dir={}, charge=0):
		self.dir = Vector(**dir)
		self.charge = cpy_objs.float32(charge)
		pass
