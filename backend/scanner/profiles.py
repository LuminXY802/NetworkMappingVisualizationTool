"""
The profiles file will serve to be the execution logic for each of the tools
"""
import tools

DISCOVERY_PROFILES = {
    "quick_discovery": {
        "category": "discovery",
        "tools": [
            "icmp_ping",
            "arp_scan",
            "nmap_host_discovery"
        ]
    },

    "full_discovery": {
        "category": "discovery",
        "tools": [
            "icmp_ping",
            "arp_scan",
            "nmap_host_discovery",
            "nmap_port_scan",
            "service_detection",
            "dns_lookup",
            "traceroute",
            "banner_grab"
        ]
    }
}

SCAN_PROFILES = {
    "os_detection": "-O",
    "service_detection": "-sV",
    "tcp_scan": "-sS",
    "full_scan": "-A"
}

TOOL_REGISTRY = {
    "icmp_ping": tools.icmp_module.run,
    "arp_scan": tools.arp_module.run,
    "nmap_host_discovery": tools.nmap_module.run
}