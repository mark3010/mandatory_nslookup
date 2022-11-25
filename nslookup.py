import subprocess

domain_name = input("Enter the domain name: ")

command = "nslookup {}".format(domain_name).split(';')[0]

response = subprocess.check_output(command, shell=True, encoding="UTF-8")

print(response)

