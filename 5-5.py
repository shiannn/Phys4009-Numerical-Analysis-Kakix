class Vector3D(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def inner(self, input):
        return (self.x*input.x+self.y*input.y+self.z*input.z)

#### END YOUR CLASS IMPLEMENTATION HERE ####

v1 = Vector3D(3.0,4.0,5.0)
v2 = Vector3D(5.2,7.4,-2.5)
v3 = Vector3D(2.1,4.2,0.0)

print('inner(v1,v2) = %.4f' % v1.inner(v2))
print('inner(v1,v3) = %.4f' % v1.inner(v3))
print('inner(v2,v3) = %.4f' % v2.inner(v3))
