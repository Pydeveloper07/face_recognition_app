import ctypes
import pathlib
import ctypes.util
import database as db
import time
import json

db_connection = db.connect()
db.create_tables(db_connection)
# getting absolut path
libname = pathlib.Path().absolute() / "libmy.so"
# loading shared library
c_lib = ctypes.cdll.LoadLibrary(libname)
# loading tools to use free()
libc = ctypes.CDLL(ctypes.util.find_library('c'))

# Setting args and return types
c_lib.ReadDatShit.restype = ctypes.c_void_p
c_lib.SendDatShit.argtypes = [ctypes.POINTER(ctypes.c_char), ]
c_lib.Forker.restype = ctypes.c_int
libc.free.argtypes = (ctypes.c_void_p,)

# Running Main()
c_lib.main()

# Seeding DATABASE
db.seed_users(db_connection)

c_lib.NewProcess()
isClientOff = False
while True:
    isPass = False
    # Running ReadDatShit()

    _result = c_lib.ReadDatShit()

    value = ctypes.c_char_p(_result).value.decode()
    value = json.loads(value)

    libc.free(_result)

    print("Client:", value)
    # getting the returned value and checking from DictOfPass then responding respectively

    # if len(returnS) == 2:
    #     user = db.get_user_by_id_password(db_connection, returnS[0], returnS[1])
    #     if len(user) > 0:
    #         isPass = True
    #         retvalue = "Yes"
    #     else:
    #         retvalue = "No"
    # elif len(returnS) == 0:
    #     isClientOff = True
    # else:
    #     retvalue = "No"

    retvalue = 'yes'

    # Running SendDatShit()
    if isClientOff:
        break
    c_lib.SendDatShit(retvalue.encode("ISO-8859–1"))
    if isPass:
        break
    break
c_lib.ReceiveFile()

# Face Recognition goes here

resFaceVar = "yes"

c_lib.SendDatShit(resFaceVar.encode("ISO-8859–1"))

c_lib.CloseShit()
