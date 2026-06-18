"""
The profiles file will serve to be the execution logic for each of the tools
"""
import scanner.tools.arp_module as arp_scan
import scanner.tools.icmp_module as icmp_ping
import scanner.tools.nmap_module as nmap_host_discovery

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
    "icmp_ping": icmp_ping,
    "arp_scan": arp_scan,
    "nmap_host_discovery": nmap_host_discovery
}