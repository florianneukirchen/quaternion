# Quaternions 

This project provides a simple python class for calculations with Quaternions.
They are often used to calculate 3D rotations (avoiding gimbal locks, interpolation errors and other problems). 

Quaternions are kind of 4-dimensional complex numbers. See [Visualizing quaternions](https://eater.net/quaternions) for an animated introduction.

For production code you'll probably prefer [Scipy.spatial.transform.Rotation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html).

See the [Jupyter Notebook](test_quaternion_class.ipynb) for more examples. 


Example: 

```python
import numpy as np
from quaternion import Quaternion

q1 = Quaternion.from_axis(30,[0,0.8,0.6]) 
q2 = Quaternion.from_axis(45,[0,0,1])

point = [1,2,3]

p = Quaternion.from_point(point)

q3 = q1 * p2 * q1.conjugate()

print(q3)
rotated_point = q3.vector
```

