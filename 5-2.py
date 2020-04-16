class Vector3D(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({},{},{})'.format(self.x,self.y,self.z)


v1 = Vector3D(3.0,4.0,5.0)
print('converting v1 to string:', v1)

v2 = Vector3D(5.2,7.4,-2.5)
print('converting v2 to string:', v2)
