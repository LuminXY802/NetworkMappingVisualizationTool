from scapy.all import IP, ICMP, Raw, sr1
import time


def ping_host(host: str, count: int = 5, interval: float = 1.0):
    payload = b"X" * 32

    sent = 0
    received = 0
    rtts = []

    for seq in range(1, count + 1):
        pkt = IP(dst=host) / ICMP(seq=seq) / Raw(load=payload)

        start = time.time()
        reply = sr1(pkt, timeout=2, verbose=False)
        rtt = (time.time() - start) * 1000

        sent += 1

        if reply and ICMP in reply and reply[ICMP].type == 0:
            received += 1
            rtts.append(rtt)

        if seq < count:
            time.sleep(interval)

    loss_pct = ((sent - received) / sent) * 100
    avg_rtt = sum(rtts) / len(rtts) if rtts else None

    return {
        "host": host,
        "sent": sent,
        "received": received,
        "loss_pct": loss_pct,
        "avg_rtt_ms": avg_rtt,
        "status": "up" if received > 0 else "down"
    }