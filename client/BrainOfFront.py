import ctypes
import pathlib
import ctypes.util

# getting absolut path
libname = pathlib.Path().absolute() / "SocketPrograms/libmy.so"
# loading shared library
c_lib = ctypes.cdll.LoadLibrary(libname)
# loading tools to use free()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Setting args and return types
c_lib.ReadData.restype = ctypes.c_void_p
c_lib.SendData.argtypes = [ctypes.POINTER(ctypes.c_char), ]
libc.free.argtypes = (ctypes.c_void_p,)


def RunMain():
    c_lib.main()


def SendData(input):
    c_lib.SendData(input.encode('ISO-8859–1'))


def ReadData():
    _result = c_lib.ReadData()
    value = ctypes.c_char_p(_result).value.decode('ISO-8859–1')
    libc.free(_result)
    return value



def CloseAll():
    c_lib.CloseShit()
