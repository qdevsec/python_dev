# utils/patterns.py
"""
Common regex patterns for threat hunting and log analysis, log lines df will be structured from this
"""

IOC_PATTERNS = {

    # =========================
    # IP Addresses
    # =========================
    "ipv4": r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b",

    # More realistic IPv6 support (compressed included)
    "ipv6": r"\b(?:[A-Fa-f0-9:]+:+)+[A-Fa-f0-9]+\b",

    "mac_address": r"\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b",

    # =========================
    # Domains / URLs
    # =========================
    "domain": r"\b(?:[a-zA-Z0-9-]+\.)+(?:com|net|org|io|ru|cn|xyz|info|biz|co|uk|de|jp|fr|edu|gov)\b",

    "url": r"https?://[^\s\"'>]+",

    "tor_onion": r"\b[a-z2-7]{16,56}\.onion\b",

    "ftp_url": r"ftp://[^\s]+",

    "s3_bucket": r"\b(?:s3://|https://s3\.amazonaws\.com/)[^\s]+\b",

    # =========================
    # Email
    # =========================
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    # =========================
    # Hashes
    # =========================
    "md5": r"\b[a-fA-F0-9]{32}\b",

    "sha1": r"\b[a-fA-F0-9]{40}\b",

    "sha256": r"\b[a-fA-F0-9]{64}\b",

    "sha512": r"\b[a-fA-F0-9]{128}\b",

    "imphash": r"\b[a-fA-F0-9]{32}\b",

    # =========================
    # CVEs
    # =========================
    "cve": r"\bCVE-\d{4}-\d{4,7}\b",

    # =========================
    # File Indicators
    # =========================
    "suspicious_file": (
        r"\b[\w,\s-]+\."
        r"(exe|dll|js|vbs|bat|scr|ps1|jar|sh|cmd|php|"
        r"docm|xlsm|hta|lnk|msi|sys|drv|tmp|dat)\b"
    ),

    "archive_file": r"\b[\w,\s-]+\.(zip|rar|7z|iso|cab)\b",

    "script_file": r"\b[\w,\s-]+\.(ps1|js|vbs|hta|bat|cmd|py|pl|sh)\b",

    "any_file": r"\b[\w,\s-]+\.[A-Za-z0-9]{1,8}\b",

    # =========================
    # File Paths
    # =========================
    "windows_path": (
        r"[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*"
        r"[^\\/:*?\"<>|\r\n]*"
    ),

    "unc_path": r"\\\\[A-Za-z0-9._$-]+\\[A-Za-z0-9.$_-]+",

    "unix_path": r"(?:/[^/\s]+)+",

    # =========================
    # Registry Keys
    # =========================
    "registry_key": (
        r"\b(?:HKLM|HKCU|HKCR|HKU|HKEY_LOCAL_MACHINE|"
        r"HKEY_CURRENT_USER)\\[^\s]+"
    ),

    # =========================
    # PowerShell
    # =========================
    "powershell_encoded": (
        r"(?i)(?:powershell|pwsh).*?-enc(?:odedcommand)?\s+[A-Za-z0-9+/=]+"
    ),

    "powershell_download": (
        r"(?i)(Invoke-WebRequest|iwr|wget|curl|DownloadString)"
    ),

    # =========================
    # Command Execution
    # =========================
    "cmd_execution": (
        r"(?i)\b(cmd\.exe|powershell\.exe|wscript\.exe|"
        r"cscript\.exe|rundll32\.exe|mshta\.exe)\b"
    ),

    # =========================
    # Network Indicators
    # =========================
    "port": r"\b(?:6553[0-5]|655[0-2]\d|65[0-4]\d{2}|"
            r"6[0-4]\d{3}|[1-5]?\d{1,4})\b",

    "suspicious_ports": (
        r"\b(4444|5555|6666|1337|31337|8080|8443|9001|"
        r"1080|2222)\b"
    ),

    "user_agent": r"\b(?:Mozilla|curl|Wget|python-requests)[^\r\n]*",

    # =========================
    # IDs / UUIDs
    # =========================
    "uuid": (
        r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{12}\b"
    ),

    # =========================
    # Timestamps
    # =========================
    "iso8601": (
        r"\b\d{4}-\d{2}-\d{2}"
        r"T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?\b"
    ),

    "syslog": r"\b[A-Z][a-z]{2}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}\b",

    # =========================
    # Windows Event IDs
    # =========================
    "windows_event_id": r"\b(?:EventID|Event ID)\s*[:=]?\s*\d{3,5}\b",

    # =========================
    # Authentication / Secrets
    # =========================
    "jwt": r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9._-]+\.[A-Za-z0-9._-]+",

    "aws_key": r"AKIA[0-9A-Z]{16}",

    "aws_secret": r"(?i)aws(.{0,20})?(secret|key)[\"']?\s*[:=]\s*[\"'][A-Za-z0-9/+=]{40}[\"']",

    "slack_token": r"xox[baprs]-[A-Za-z0-9-]{10,48}",

    "github_token": r"ghp_[A-Za-z0-9]{36}",

    # =========================
    # Encoded / Obfuscated Data
    # =========================
    "base64": r"\b(?:[A-Za-z0-9+/]{20,}={0,2})\b",

    "hex_blob": r"\b(?:0x)?[A-Fa-f0-9]{16,}\b",

    # =========================
    # Malware / Persistence
    # =========================
    "mutex": r"\b(?:Global\\|Local\\)[A-Za-z0-9_-]+\b",

    "scheduled_task": r"(?i)\bschtasks(?:\.exe)?\b",

    "service_creation": r"(?i)\bsc(?:\.exe)?\s+create\b",

    # =========================
    # ASN
    # =========================
    "asn": r"\bAS\d{1,10}\b",
}

# IOC_PATTERNS = {
#     "ipv4": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
#     "ipv6": r"\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b",
#     "domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
#     "url": r"https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?",
#     "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    
#     # Hashes
#     "md5": r"\b[a-fA-F0-9]{32}\b",
#     "sha1": r"\b[a-fA-F0-9]{40}\b",
#     "sha256": r"\b[a-fA-F0-9]{64}\b",
    
#     # File extensions
#     "suspicious_file": r"\b(\w+\.(exe|dll|js|vbs|bat|scr|ps1|jar|sh|cmd|php|docm|xlsm))\b",
#     "any_file": r"\b[\w,\s-]+\.[A-Za-z0-9]{1,5}\b",
    
#     # File paths
#     "windows_path": r"[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*",
#     "unix_path": r"\/(?:[\w.-]+\/)*[\w.-]+",
    
#     # Ports
#     "port": r"\b(?:[0-9]{1,5})\b",
    
#     # UUIDs / GUIDs
#     "uuid": r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
    
#     # Timestamps
#     "iso8601": r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\b",
#     "syslog": r"\b[A-Z][a-z]{2} +\d{1,2} \d{2}:\d{2}:\d{2}\b",
    
#     # Usernames (basic)
#     "username": r"\b[a-zA-Z0-9._-]{3,20}\b",
    
#     # Common C2 / Malware indicators (hardcoded ports and extensions)
#     "suspicious_ports": r"\b(4444|5555|6666|1337|8080|8443)\b",
# }
