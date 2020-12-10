# USE THIS ONLY FOR LEARNING PURPOSE
import ctypes
import pathlib
import ctypes.util
import time

#getting absolut path   
libname = pathlib.Path().absolute() / "libmy.so"
#loading shared library
c_lib = ctypes.cdll.LoadLibrary(libname)
#loading tools to use free()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

#Setting args and return types    
c_lib.ReadDatShit.restype = ctypes.c_void_p
c_lib.SendDatShit.argtypes = [ctypes.POINTER(ctypes.c_char), ]
libc.free.argtypes = (ctypes.c_void_p,)

#Running Main()
c_lib.main()

while True:
	
	print()
	Val = input("Enter your name: ");

	#Running SendDatShit()
	c_lib.SendDatShit(Val.encode('ISO-8859–1'))
	if Val.lower() == "bye":
		break
	#Running ReadDatShit()
	_result = c_lib.ReadDatShit()
	Value = ctypes.c_char_p(_result).value.decode("ISO-8859–1")
	libc.free(_result)
	print("Server:",Value)
c_lib.CloseShit()
