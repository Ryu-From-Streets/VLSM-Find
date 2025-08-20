
GIVEN_ADDR = 0
NET_PREFIX_LEN = 0
HOST_SUFFIX_LEN = 0
NET_MASK = 0
NET_ADDR = 0

def strtoiIPV4(ipv4_str):
    ipv4_int = 0
    for val in ipv4_str.split("."):
        ipv4_int <<= 8
        ipv4_int |= int(val)
    return ipv4_int

def prefixLenToNetMask(prefix_len):
    net_mask = 0
    for i in range(int(prefix_len)):
        net_mask <<= 1
        net_mask |= 1
    net_mask <<= 32 - int(prefix_len)
    return net_mask

def getSortedSubnetHosts(num_subnets):
    subnet_hosts = []
    for i in range(num_subnets):
        subnet_name = input(f"Enter the name of subnet {i}: ")
        num_hosts = int(input(f"Enter the number of hosts you wish to have under the subnet \"{subnet_name}\": "))
        subnet_hosts.append((subnet_name, num_hosts))
    subnet_hosts = sorted(subnet_hosts, key=lambda x: x[0])
    return sorted(subnet_hosts, key=lambda x: x[1], reverse=True)

def main():
    cidr_ipv4_str = input("Enter your network's IPv4 base address in decimal and CIDR notation(v.w.x.y/z): ").split("/")
    GIVEN_ADDR = strtoiIPV4(cidr_ipv4_str[0])
    NET_PREFIX_LEN = int(cidr_ipv4_str[1])
    HOST_SUFFIX_LEN = 32 - NET_PREFIX_LEN
    NET_MASK = prefixLenToNetMask(NET_PREFIX_LEN)
    NET_ADDR = GIVEN_ADDR & NET_MASK
    print("Given Address Binary = " + bin(GIVEN_ADDR))
    print("Network Prefix Length = " + str(NET_PREFIX_LEN))
    print("Host Suffix Lenght = " + str(HOST_SUFFIX_LEN))
    print("Network Mask = " + bin(NET_MASK))
    print("Network Address = " + bin(NET_ADDR))
    
    num_subnets = int(input("Enter number of subnets you wish to add to your network: "))
    subnet_hosts = getSortedSubnetHosts(num_subnets)
    print("Subnet Hosts = " + str(subnet_hosts))

    total_needed_hosts = sum(e[1] for e in subnet_hosts)
    max_possible_hosts = pow(2, HOST_SUFFIX_LEN) - 2
    if (total_needed_hosts > max_possible_hosts):
        print("NOT ENOUGH HOSTS AVAILABLE TO ALLOCATE SUBNETS")

if __name__ == "__main__":
    main()
