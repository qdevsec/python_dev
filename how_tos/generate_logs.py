import random
from datetime import datetime, timedelta

def generate_sample_logs(filename="access.log"):
    ips = ["192.168.1.10", "172.16.0.5", "10.0.0.99"]
    pages = ["/index.html", "/login", "/dashboard", "/api/v1/data"]
    
    with open(filename, "w") as f:
        # Generate 50 normal lines
        start_time = datetime.now()
        for i in range(50):
            timestamp = (start_time + timedelta(seconds=i)).strftime("%d/%b/%Y:%H:%M:%S")
            ip = random.choice(ips[:2])
            status = "200"
            f.write(f'{ip} - - [{timestamp} +0000] "GET {random.choice(pages)} HTTP/1.1" {status} 512\n')
        
        # Simulate Brute Force: 15 failed logins in 30 seconds from 10.0.0.99
        for i in range(15):
            timestamp = (start_time + timedelta(seconds=i)).strftime("%d/%b/%Y:%H:%M:%S")
            f.write(f'10.0.0.99 - - [{timestamp} +0000] "POST /login HTTP/1.1" 401 128\n')

    print(f"File '{filename}' generated successfully.")

generate_sample_logs()