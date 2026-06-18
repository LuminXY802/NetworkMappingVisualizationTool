import scanner.profiles as profiles
import subprocess

def run_scan(profile, target):
    profile = profiles.SCAN_PROFILES[profile]

    subprocess.run(
        hosts=target,
        arguments=profile["arguments"]
    )