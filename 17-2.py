from xmlrpc.client import ServerProxy, Error
url = "http://www.pythonchallenge.com/pc/phonebook.php"

with ServerProxy(url) as proxy:
    print(proxy)

    try:
        print(proxy.phone("the flowers are on their way."))
    except Error as v:
        print("ERROR", v)