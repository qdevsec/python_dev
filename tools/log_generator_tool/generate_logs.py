import random
from utils.pattern_injector import inject_iocs
from datetime import datetime, timedelta

def generate_sample_logs(filename="access.log", num_entries=100):
    ips = ["192.168.1.10", "172.16.0.5", "10.0.0.99"]
    pages = ["/index.html", "/login", "/dashboard", "/api/v1/data"]
    
    with open(filename, "w") as f:
        # Generate 50 normal lines
        current_time = datetime.now()
        # for i in range(50):
        #     timestamp = (start_time + timedelta(seconds=i)).strftime("%d/%b/%Y:%H:%M:%S")
        #     ip = random.choice(ips[:2])
        #     status = "200"
        #     f.write(f'{ip} - - [{timestamp} +0000] "GET {random.choice(pages)} HTTP/1.1" {status} 512\n')
        
        # # Simulate Brute Force: 15 failed logins in 30 seconds from 10.0.0.99
        # for i in range(15):
        #     timestamp = (start_time + timedelta(seconds=i)).strftime("%d/%b/%Y:%H:%M:%S")
        #     f.write(f'10.0.0.99 - - [{timestamp} +0000] "POST /login HTTP/1.1" 401 128\n')


        for _ in range(num_entries):
            current_time += timedelta(seconds=random.randint(1, 5))
            timestamp = current_time.strftime("%d/%b/%Y:%H:%M:%S")

            base_log = (
                f'192.168.1.{random.randint(1,255)} - - '
                f'[{timestamp} +0000] "GET /index.html HTTP/1.1" '
                f'{random.choice([200,404,500])} {random.randint(100,5000)}'
            )

            log_with_iocs = inject_iocs(base_log)
            f.write(log_with_iocs + "\n")

    print(f"File '{filename}' generated successfully.")

generate_sample_logs()