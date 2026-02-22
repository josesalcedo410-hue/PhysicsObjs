from cpy_objs import cpy_objs

class Vector(cpy_objs.Structure):
	_fields_ = [
	("x", cpy_objs.float32),
	("y", cpy_objs.float32),
	("z", cpy_objs.float32),
	]
	def __init__(self, x=0, y=0, z=0):
		self.x = cpy_objs.float32(x)
		self.y = cpy_objs.float32(y)
		self.z = cpy_objs.float32(z)
		pass
