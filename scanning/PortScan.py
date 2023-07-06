from scapy.all import *
import ipaddress
 
"""
Scapy require these field:

dst: Destination IP address 
source port: default is 20 , can set another port
destination port: allows list port
TCP flag: SYN/ACK/FIN
    - SYN: synchronization
    - ACK: acknowledgement
    - FIN: finish
sr: send/receive
sport: sources port
timeout: set timeout
   
"""
 
ports = [25,80,53,443,445,8080,8443]
 
 """
 this func send a package by sr func, transmit SYN package.
 monitor any response and stored in ans variable.
 
 timeout set in 2 seconds
 
 s[TCP].dport is the code accesses the TCP layer of SYN package it send out and extract the
 destination port to compare  with the src port
 If these port match and package receive SYN/ACK flag => then marked port is OPEN
 
 """
def SynScan(host):
    ans,unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=ports,flags="S")
        ,timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA":
            print(s[TCP].dport)
 
 
"""
this func just have some diff with PortScan
DNS query usually sent out over UDP and include DNS layer
default port is 53
rd: Recurrsion desired -> set to 1
qname: a DNSQR - DNS query
""" 
def DNSScan(host):
    ans,unans = sr(
        IP(dst=host)/
        UDP(dport=53)/
        DNS(rd=1,qd=DNSQR(qname="google.com"))
        ,timeout=2,verbose=0)
    if ans and ans[UDP]:
        print("DNS Server at %s"%host)
    
host = input("Enter IP Address: ")
try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)
 
SynScan(host)
DNSScan(host)