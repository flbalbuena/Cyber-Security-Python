

log_file = "auth.log"
alert_threshold = 3
failed_attempts = {}
with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            words = line.split()
            from_position = words.index("from")
            ip_address = words[from_position +1]

            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1

print("\n=== FAILED login REPORT ===")

for ip, attempts in failed_attempts.items():
    print(ip, attempts)
    if attempts >= 3:
        print(ip, attempts, "ALERT: possible brute force attack")
    else:
        print(ip, attempts, "Normal")
