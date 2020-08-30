from scapy.all import *
ap_list = []
def PacketHandler (pkt) :
    if pkt.haslayer (Dot11) :
        if pkt.type == 0 and pkt.subtype == 8 :
            if pkt.addr2 not in ap_list :
                ap_list.append(pkt.addr2)
                print("Available SSID: %s And it's MAC addr: %s " %(pkt.info, pkt.addr2))
sniff(iface = "wlan0" , prn = PacketHandler)