MOD=2
LAN="eth2"
WAN="eth1"
LAN_NETWORK="192.168.0.0/24"
IP="192.168.0.254"
HTTP="80"
HTTPS="443"
NGINX_PYCAPTIVE="14901"
PROXY="3128"
SSH="22"
DNS="53"
DHCP_SERVER="67"
DHCP_CLIENT="68"
DNS_RNDC="953"

FILE = "rules.v4"

with open(FILE, "w") as f:
    # mangle
    f.write("*mangle\n")
    f.write(":PREROUTING ACCEPT [0:0]\n")
    f.write(":INPUT ACCEPT [0:0]\n")
    f.write(":FORWARD ACCEPT [0:0]\n")
    f.write(":OUTPUT ACCEPT [0:0]\n")
    f.write(":POSTROUTING ACCEPT [0:0]\n")
    f.write("-N INTERNET\n")
    f.write("-N PYCAPTIVE\n")
    f.write("-A PREROUTING -i {0} -p tcp -m tcp --dport {1} -j PYCAPTIVE\n".format(LAN, HTTP))
    f.write("-A PREROUTING -i {0} -p tcp -m ucp --dport {1} -j PYCAPTIVE\n".format(LAN, HTTP))
    f.write("-A PREROUTING -i {0} -p tcp -m tcp --dport {1} -j DROP\n".format(LAN, HTTPS))
    f.write("-A PREROUTING -i {0} -p tcp -m udp --dport {1} -j DROP\n".format(LAN, HTTPS))
    f.write("-A PYCAPTIVE -j MARK --set-mark 1\n")
    f.write("-A INTERNET -j ACCEPT\n")
    # nat
    f.write("*nat\n")
    f.write(":PREROUTING ACCEPT [0:0]\n")
    f.write(":INPUT ACCEPT [0:0]\n")
    f.write(":OUTPUT ACCEPT [0:0]\n")
    f.write(":POSTROUTING ACCEPT [0:0]\n")
    rule="-A PREROUTING -i {0} -p tcp -m tcp -m mark --mark 1 -j DNAT --to-destination {1}:{2}\n".format(LAN, IP, NGINX_PYCAPTIVE)
    f.write(rule)
    rule="-A PREROUTING -i {0} -p tcp -m ucp -m mark --mark 1 -j DNAT --to-destination {1}:{2}\n".format(LAN, IP, NGINX_PYCAPTIVE)
    f.write(rule)
    rule="-A PREROUTING -i {0} -s {1} -p tcp -d {2} --dport {3} -j DNAT --to-destination {4}:{5}\n".format(LAN, LAN_NETWORK, IP, HTTP, IP, NGINX_PYCAPTIVE)
    f.write(rule)
    if MOD == 2:
        f.write("-A PREROUTING -i {0} -s {1} -p tcp --dport {2} -j DNAT --to-destination {3}:{4}\n".format(LAN, LAN_NETWORK, HTTP, IP, PROXY))
    f.write("-A POSTROUTING -o {0} -j MASQUERADE\n".format(WAN))
    if MOD == 2:
        f.write("-A PREROUTING -i {0} -p tcp --sport {1} -j REDIRECT --to-port {2}\n".format(LAN, HTTP, PROXY))
    # filter
    f.write("*filter")
    f.write(":INPUT ACCEPT [0:0]")
    f.write(":FORWARD ACCEPT [0:0]")
    f.write(":OUTPUT ACCEPT [0:0]")
    f.write("-A INPUT -p icmp -m conntrack --ctstate NEW,ESTABLISHED,RELATED --icmp-type 8 -j ACCEPT\n")
    f.write("-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT\n")
    f.write("-A INPUT -i lo -j ACCEPT\n")
    f.write("-A INPUT -i {0} -p tcp --dport {1} -j ACCEPT\n".format(LAN, SSH))
    f.write("-A INPUT -i {0} -p udp --dport {1} -j ACCEPT\n".format(LAN, DNS))
    f.write("-A INPUT -i {0} -p tcp --dport {1} -j ACCEPT\n".format(LAN, DNS))
    f.write("-A INPUT -i {0} -p udp --dport {1} --sport {2} -j ACCEPT\n".format(LAN, DHCP_SERVER, DHCP_CLIENT))
    f.write("-A INPUT -i {0} -p udp --dport {1} --sport {2} -j ACCEPT\n".format(LAN, DHCP_CLIENT, DHCP_SERVER))
    f.write("-A INPUT -i {0} -p udp --dport {1} -j ACCEPT\n".format(LAN, DNS_RNDC))
    f.write("-A INPUT -i {0} -p tcp --dport {1} -j ACCEPT\n".format(LAN, DNS_RNDC))
    f.write("-A INPUT -j REJECT\n")
    f.write("-A OUTPUT -j ACCEPT\n")
