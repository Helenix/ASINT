from dbUI import dbUI
import Pyro4

nameServer = Pyro4.locateNS("127.0.0.1")
#remoteObjectName = input("Remote object name: ")
remoteObjectName = "DBserver"
uri = nameServer.lookup(remoteObjectName)
storage = Pyro4.Proxy(uri)

ui = dbUI(storage)
