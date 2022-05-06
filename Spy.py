import os, sys
try:
    __import__("spy1").spypro()
except Exception as e:
    exit(str(e))
