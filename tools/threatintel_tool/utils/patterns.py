# utils/patterns.py
"""
Common regex patterns for threat hunting and log analysis
"""

IOC_PATTERNS = {
    "ipv4": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "ipv6": r"\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b",
    "domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
    "url": r"https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?",
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    
    # Hashes
    "md5": r"\b[a-fA-F0-9]{32}\b",
    "sha1": r"\b[a-fA-F0-9]{40}\b",
    "sha256": r"\b[a-fA-F0-9]{64}\b",
    
    # File extensions
    "suspicious_file": r"\b(\w+\.(exe|dll|js|vbs|bat|scr|ps1|jar|sh|cmd|php|docm|xlsm))\b",
    "any_file": r"\b[\w,\s-]+\.[A-Za-z0-9]{1,5}\b",
    
    # File paths
    "windows_path": r"[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*",
    "unix_path": r"\/(?:[\w.-]+\/)*[\w.-]+",
    
    # Ports
    "port": r"\b(?:[0-9]{1,5})\b",
    
    # UUIDs / GUIDs
    "uuid": r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
    
    # Timestamps
    "iso8601": r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\b",
    "syslog": r"\b[A-Z][a-z]{2} +\d{1,2} \d{2}:\d{2}:\d{2}\b",
    
    # Usernames (basic)
    "username": r"\b[a-zA-Z0-9._-]{3,20}\b",
    
    # Common C2 / Malware indicators (hardcoded ports and extensions)
    "suspicious_ports": r"\b(4444|5555|6666|1337|8080|8443)\b",
}
