from scapy.all import *

'''
foward scanning data from host to honeys host
'''

ip = "172.0.0.1"
ports = [53, 80]
honeys = [8080, 8443]

blocked = []


def analyzePackets(p):
    global blocked
    if p.haslayer(IP):
        response = Ether(src=p[Ether].dst, dst=p[Ether].src) /\
            IP(src=p[IP].dst, dst=p[IP].src) /\
            TCP(sport=p[TCP].dport, dport=p[TCP].sport, ack=p[TCP].seq+1)
        source = p[IP].src
    else:
        response = Ether(src=p[Ether].dst, dst=p[Ether].src) /\
            IPv6(src=p[IPv6].dst, dst=p[IPv6].src) /\
            TCP(sport=p[TCP].dport, dport=p[TCP].sport, ack=p[TCP].seq+1)
        source = p[IPv6].src
    if p[TCP].flags != "S":
        return
    port = p[TCP].dport
    if source in blocked:
        if port in ports:
            response[TCP].flags = "RA"
            print("Sending reset")
        elif port in honeys:
            response[TCP].flags = "SA"
        else:
            return
        sendp(response, verbose=False)
    else:
        if port not in ports:
            blocked += [source]
            if port in honeys:
                response[TCP].flags = "SA"
                sendp(response, verbose=False)


f = "dst host "+ip+" and tcp"
sniff(filter=f, prn=analyzePackets)
