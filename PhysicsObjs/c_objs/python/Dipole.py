from .Vector import Vector
from cpy_objs import cpy_objs

class Dipole(cpy_objs.Structure):
	_fields_ = [
	("pos", Vector),
	("charge", cpy_objs.float32),
	]
	def __init__(self, pos={}, charge=0):
		self.pos = Vector(**pos)
		self.charge = cpy_objs.float32(charge)
		pass
