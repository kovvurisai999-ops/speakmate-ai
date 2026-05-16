import ctypes
import os

dll_path = r"C:\Users\hmind\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\lib\c10.dll"
if os.path.exists(dll_path):
    print(f"File exists: {dll_path}")
    try:
        ctypes.WinDLL(dll_path)
        print("Successfully loaded c10.dll")
    except Exception as e:
        print(f"Failed to load c10.dll: {e}")
else:
    print(f"File NOT found: {dll_path}")
