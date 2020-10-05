import os

results_file = open("results.txt", "w")
ip_list = ["8.8.8.8", "8.8.4.4", "66.254.114.41", "192.168.1.1"]

#for ip in range(1, 10):
#    ip_list.append("192.168.178." + str(ip))

print(len(ip_list))

for ip in ip_list:
    response = os.popen(f"ping {ip} -n 1").read()
    if "Received = 1" and "Approximate" in response:
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        results_file.write(f"DOWN {ip} Ping Unsuccessful" + "\n")

results_file.close()
