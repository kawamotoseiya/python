import sys
sys.path.append("/Users/kawamotoseiya/Library/Python/3.7/lib/python/site-packages")

import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("kosuu", len(digits.images))
print("gazoudata",digits.images[0])
print("number",digits.target[0])
