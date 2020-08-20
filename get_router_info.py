import scapy.all as S


## First let's determine what interfaces are available.

if_list = get_if_list()
print(if_list)

## Routes are stored in the conf.route. Let's display them and store in a variable
print("[*]THESE ARE THE AVAILABLE ROUTES ON YOUR ROUTER  \n", S.conf.route)

## Now let's determine the router IP address

conf_route_network_IP = S.get_if_addr(conf.iface)
print("[*]THIS IS YOUR IP ADDRESS: ", conf_route_network_IP)

## Get MAC address using iface
get_mac = S.get_if_hwaddr(conf.iface)
print("[*] THIS IS YOUR MAC ADDRESS: " , get_mac)

## REJECTED BY IP. not useful
# if conf_route_network_IP is not None:
#     sock.connect(("192.168.0.5", 80))
#     ss = StreamSocket(sock, Raw)
#     ss.sr1(Raw("GET /\r\n"))

"""
Let's do something with this information
"""

