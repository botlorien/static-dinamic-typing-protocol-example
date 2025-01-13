from typing import SupportsComplex
import numpy as np

c64 = np.complex64(3+4j)
print(isinstance(c64, complex))
print(isinstance(c64, SupportsComplex))
c = complex(c64)
print(isinstance(c, SupportsComplex))
print(complex(c))