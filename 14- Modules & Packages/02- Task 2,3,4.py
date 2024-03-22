# ----------------------
# in my_mod.py file:
# ----------------------

def say_welcome(name):
    """Prints a welcome message."""
    print(f"Welcome {name}")

def say_hello(name):
    """Prints a hello message."""
    print(f"Hello {name}")

# ==================================================

# ----------------------
# in  main.py file:
# ----------------------

import sys
import my_mod  # Importing the entire module

sys.path.append(r"")

# Calling the Whole module
my_mod.say_welcome("A,r")
my_mod.say_hello("Noor")

# Calling Function only
from my_mod import say_welcome
say_welcome("Amr")

from my_mod import say_hello
say_hello("Noor")

# Using Alias
from my_mod import say_welcome as welcome
welcome("Amr")

from my_mod import say_hello as hello
hello("Noor")
