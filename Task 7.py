# Create a python module with list and import the module in another .py file and change the value in list
from mymodule import a
a[2]=5
print(a)
# Installed pandas package using pip install pandas in command prompt
print("pandas package installed")
# Import random number
import random
y=int(input("Enter The Number :"))
for x in range(y):
    print(random.randint(0,101))
# Import sys package and find the python path
import sys
print(sys.path)
# Install a package and uninstall a package using pip
print("installed and uninstalled a package using pip")