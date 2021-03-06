import ctypes
import pathlib
import ctypes.util
import server_utils as utils

# getting absolut path
libname = pathlib.Path().absolute() / "libmy.so"
# loading shared library
c_lib = ctypes.cdll.LoadLibrary(libname)
# loading tools to use free()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Setting args and return types
c_lib.ReadData.restype = ctypes.c_void_p
c_lib.SendData.argtypes = [ctypes.POINTER(ctypes.c_char), ]
c_lib.Forker.restype = ctypes.c_int
libc.free.argtypes = (ctypes.c_void_p,)

# Running Main()
c_lib.main()


utils.setup_database()

while True:
    c_lib.NewProcess()
    if c_lib.Forker()==0:
        c_lib.Closesockfd()

        while True:
            _result = c_lib.ReadData()

            if _result is None:
                continue

            Value = ctypes.c_char_p(_result).value.decode("ISO-8859–1")
            if len(Value)==0:
                break

            libc.free(_result)

            output = ''

            if len(Value) > 0:
                try:
                    output = utils.parse_request(Value)
                except:
                    print("error occurred while parsing request")

            if output != '':
                c_lib.SendData(output.encode("ISO-8859–1"))
c_lib.Closenewsockdf()
