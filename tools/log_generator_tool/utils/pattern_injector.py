import random
import string
import uuid


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
    "ipv4": lambda: f"192.168.1.{random.randint(1,255)}",
    "domain": random_domain,
    "url": random_url,
    "email": random_email,
    "md5": lambda: random_hash(32),
    "sha1": lambda: random_hash(40),
    "sha256": lambda: random_hash(64),
    "suspicious_file": lambda: f"malware{random.randint(1,10)}.exe",
    "windows_path": random_windows_path,
    "unix_path": random_unix_path,
    "uuid": random_uuid,
    "port": lambda: str(random.randint(1, 65535)),
    "suspicious_ports": lambda: random.choice(["4444","5555","6666","1337","8080","8443"]),
}