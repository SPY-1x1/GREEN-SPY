import os, sys
try:
    __import__("spy").spypro()
except Exception as e:
    exit(str(e))
