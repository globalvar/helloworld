__author__ = 'root'

import argparse
import socket

x = argparse.ArgumentParser(description="Here should be some kind of description")
x.add_argument('--name',type=str,help="This should be the website name e.g example.com",required=True)
x.add_argument('-o',type=str,help="This should show/print the ip addr of the entered website",required=False)

#var y as cmdargs
y = x.parse_args()
i_var= y.name

ipaddr = socket.gethostbyname(i_var);
print(ipaddr);
