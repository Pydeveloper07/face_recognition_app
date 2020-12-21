import ctypes
import pathlib
import ctypes.util
import database as db
from request_handler import handle_request, is_stop
import sys

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


def stop_server():
    c_lib.CloseShit()
    sys.exit(0)


def run():
    while True:
        if is_stop():
            stop_server()
        _result = c_lib.ReadDatShit()
        Value = ctypes.c_char_p(_result).value.decode("ISO-8859–1")
        libc.free(_result)
        retvalue = handle_request(db_connection, Value)
        if retvalue is not None:
            c_lib.SendDatShit(retvalue.encode())

        # if 'action' in Value:
        #     retvalue = handle_request(db_connection, Value)
        #     c_lib.SendDatShit(retvalue.encode("ISO-8859–1"))
        #     continue
        #
        # returnValue = Value.strip()
        # print("Client:", Value)
        # # getting the returned value and checkingfrom DictOfPass then responding respectively
        # returnS = returnValue.split()
        #
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
        #
        # # Running SendDatShit()
        # if isClientOff:
        #     break
        # c_lib.SendDatShit(retvalue.encode("ISO-8859–1"))
        # if isPass:
        #     break

    # c_lib.ReceiveFile()
    #
    # Face Recognition goes here
    #
    # resFaceVar = "yes"
    #
    # c_lib.SendDatShit(resFaceVar.encode("ISO-8859–1"))


if __name__ == '__main__':
    run()
