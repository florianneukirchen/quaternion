import numpy as np

def skew(v):
    """Skew-symmetric matrix from a 3D vector"""
    if v.shape != (3,):
        raise ValueError("Input must be a 3D vector")
    return np.array([[0, -v[2], v[1]],
                     [v[2], 0, -v[0]],
                     [-v[1], v[0], 0]])


class Quaternion:

    def __init__(self, array):

        if array.shape != (4,):
            raise ValueError("Quaternion must be a 4D vector")
        self.array = array

    @classmethod
    def from_xyzw(cls, x, y, z, w):
        return cls(np.array([x, y, z, w]))

    @classmethod
    def from_axis(cls, angle, axis, degrees=True):
        if degrees:
            angle = np.deg2rad(angle)

        half_angle = angle / 2.0
        sin_half_angle = np.sin(half_angle)
        cos_half_angle = np.cos(half_angle)

        axis = axis / np.linalg.norm(axis)

        return cls(np.array([axis[0] * sin_half_angle, axis[1] * sin_half_angle, axis[2] * sin_half_angle, cos_half_angle]))

    @classmethod
    def from_point(cls, point):
        point = np.asarray(point) # Can also be a list
        if point.shape != (3,):
            raise ValueError("Point must be a 3D vector")
        return cls(np.array([point[0], point[1], point[2], 0.0]))

    @property 
    def vector(self):
        return self.array[:3]
    
    @property
    def scalar(self):
        return self.array[3]

    def conjugate(self):
        return Quaternion(np.array([-self.array[0], -self.array[1], -self.array[2], self.array[3]]))


    def norm(self):
        return np.sqrt(np.dot(self.array, self.array))
    
    def normalize(self):
        norm = self.norm()
        if norm == 0:
            raise ValueError("Cannot normalize 0,0,0,0 quaternion")
        return Quaternion(self.array / norm)
    
    def inv(self):
        return Quaternion(self.conjugate().array / self.norm()**2)
    
    def is_unit(self):
        return np.isclose(self.norm(), 1.0)
    
    def as_Q(self):
        Q = np.zeros((4, 4))
        Q[:3, :3] = self.scalar * np.eye(3) + skew(self.vector)
        Q[:, 3] = self.array
        Q[3, :3] = -self.vector
        return Q

    def as_W(self):
        W = np.zeros((4, 4))
        W[:3, :3] = self.scalar * np.eye(3) - skew(self.vector)
        W[:, 3] = self.array
        W[3, :3] = -self.vector
        return W


    def __str__(self):
        return f"{self.array[0]} i + {self.array[1]} j + {self.array[2]} k + {self.array[3]}"
 

    def __repr__(self):
        return f"Quaternion({self.array[0]} i + {self.array[1]} j + {self.array[2]} k + {self.array[3]})"
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Quaternion(self.array * other)
        elif isinstance(other, Quaternion):
            return Quaternion(self.as_Q() @ other.array) 
        else:
            raise ValueError("Can only multiply by a scalar or another Quaternion")
    
    def __add__(self, other):
        if not isinstance(other, Quaternion):
            raise ValueError("Can only add another Quaternion")
        return Quaternion(self.array + other.array)
    
    def __sub__(self, other):
        if not isinstance(other, Quaternion):
            raise ValueError("Can only subtract another Quaternion")
        return Quaternion(self.array - other.array)
    

