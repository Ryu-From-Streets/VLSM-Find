import re

def main():
    DEC_BASE_ADDR = re.split('[./]', input("Enter the decimal base CIDR address:"))
    num_hosts = int(input("Enter number of hosts:"))
    subnets_to_hosts = {}

    for i in range(0, num_hosts):
        subnet = input(f"Enter name of subnet {int(i)}:")
        num_hosts = input(f"Enter number of hosts for this subnet:")
        subnets_to_hosts[subnet] = int(num_hosts)

    print(f"BASE_ADDR: {DEC_BASE_ADDR}")
    print(f"subnets_to_host: {subnets_to_hosts}")



if __name__ == "__main__":
    main()