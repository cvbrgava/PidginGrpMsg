import dbus
import time
import gobject
from dbus.mainloop.glib import DBusGMainLoop

bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface( obj, "im.pidgin.purple.PurpleInterface" )

def sendmessage(group,string):
    for online in purple.PurpleFindBuddies( (purple.PurpleAccountsGetAllActive())[0], '' ):
        if ( purple.PurpleBuddyGetAlias( online ) in group):
            conv = purple.PurpleConversationNew(1, (purple.PurpleAccountsGetAllActive())[ 0 ] , purple.PurpleBuddyGetName( online ) )
            purple.PurpleConvImSend(purple.PurpleConvIm(conv), string)
        

lab = ['IronButt Iyer','Shiny shoulder shekar','Sudharshan Viswanathan','Nigga Sarkari','Pardouche Gupto','Elbarato Mustachio','Ammi Jaan']

while True:    
	msg = raw_input()
	sendmessage(lab,msg)
