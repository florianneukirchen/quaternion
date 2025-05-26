# Quaternions 

Calculate 3D rotations with Quaternions using a `Quaternions` class.
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

