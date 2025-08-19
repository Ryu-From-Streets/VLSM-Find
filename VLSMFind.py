
def getBaseAddr(DEC_BASE_ADDR):
    BASE_ADDR = 0
    for val in DEC_BASE_ADDR.split("."):
        BASE_ADDR <<= 8
        BASE_ADDR |= int(val)
    return BASE_ADDR

def getBaseAddrMask(DEC_BASE_CIDR_VAL):
    BASE_MASK = 0
    for i in range(int(DEC_BASE_CIDR_VAL)):
        BASE_MASK <<= 1
        BASE_MASK |= 1
    BASE_MASK <<= 32 - int(DEC_BASE_CIDR_VAL)
    return BASE_MASK

def getSortedSubnetHosts(num_subnets):
    subnet_hosts = []
    for i in range(num_subnets):
        subnet_name = input(f"Enter the name of subnet {i}: ")
        num_hosts = input(f"Enter the number of hosts you wish to have under the subnet \"{subnet_name}\": ")
        subnet_hosts.append((subnet_name, num_hosts))
    subnet_hosts = sorted(subnet_hosts, key=lambda x: x[0])
    return sorted(subnet_hosts, key=lambda x: x[1], reverse=True)

def main():
    DEC_CIDR_BASE_ADDR = input("Enter your network's IPv4 base address in decimal and CIDR notation(v.w.x.y/z): ").split("/")
    BASE_ADDR = getBaseAddr(DEC_CIDR_BASE_ADDR[0])
    print(bin(BASE_ADDR))
    BASE_MASK = getBaseAddrMask(DEC_CIDR_BASE_ADDR[1])
    print(bin(BASE_MASK))
    print(bin(BASE_ADDR & BASE_MASK))
    
    num_subnets = int(input("Enter number of subnets you wish to add to your network: "))
    subnet_hosts = getSortedSubnetHosts(num_subnets)
    print(subnet_hosts)

if __name__ == "__main__":
    main()
