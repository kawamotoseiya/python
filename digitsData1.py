import sys
sys.path.append("/Users/kawamotoseiya/Library/Python/3.7/lib/python/site-packages")

import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[0],cmap="Greys")
plt.show()
