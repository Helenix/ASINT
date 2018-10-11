from dbUI import dbUI
from bookDB import BookDB
import Pyro4

BookDBremote = Pyro4.expose(BookDB)
remoteStorage = BookDBremote()

ns = Pyro4.locateNS("127.0.0.1")
daemon = Pyro4.Daemon("127.0.0.1")
uri = daemon.register(remoteStorage, "DBserver")
ns.register("DBserver", uri)
print(uri)
daemon.requestLoop()

