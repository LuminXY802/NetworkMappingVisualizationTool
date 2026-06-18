from scapy.all import ARP, Ether, srp 

def arp_scan(network: str):
    arp_request = ARP(pdst=network)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    answered, unanswered = srp(packet, timeout=1, verbose=False)

    results = []

    for sent, received in answered:
        results.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "status": "up"
        })

    return results