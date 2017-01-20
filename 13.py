from xmlrpc.client import ServerProxy, Error

with ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy)

    try:
        print(proxy.phone("Bert"))
    except Error as v:
        print("ERROR", v)