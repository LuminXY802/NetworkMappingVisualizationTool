def icmp_ping(target):
    return {
        "type": "icmp",
        "target": target,
        "status": "up"
    }