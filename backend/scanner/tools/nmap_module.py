from profiles import SCAN_PROFILES
import subprocess

def run_scan(profile, target):
    profile = SCAN_PROFILES[profile]

    subprocess.run(
        hosts=target,
        arguments=profile["arguments"]
    )