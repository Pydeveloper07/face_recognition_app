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
c_lib.Forker.restype = ctypes.c_int
libc.free.argtypes = (ctypes.c_void_p,)

#Running Main()
c_lib.main()

#Simulating DATABASE
DictOfPass = {'admin': 'admin',
	'Javokhir': 'admin',
	'Tukhtamurod': 'forker'}

c_lib.NewProcess()
while True:
	isPass=False
	#Running ReadDatShit()
	
	_result = c_lib.ReadDatShit()
	Value = ctypes.c_char_p(_result).value.decode("ISO-8859–1")
	libc.free(_result)
	returnValue = Value.strip()
	print("Client:", Value)
	#getting the returned value and checkingfrom DictOfPass then responding respectively
	returnS = returnValue.split()		
	if (returnS[0] in DictOfPass.keys()) and (DictOfPass[returnS[0]] == returnS[1]):
		isPass = True
		retvalue = "Yes"
	else:
		retvalue = "No"
	
	#Running SendDatShit()
	c_lib.SendDatShit(retvalue.encode("ISO-8859–1"))
	if isPass:
		break
	
c_lib.CloseShit()
