"""
This port scanner takes an IPv4 and scans the top 20 TCP ports according to Nmap's database.
Run in terminal with IPv4 following this file.
"""


import logging
import sys
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


try:
    import functions as fn
    logging.DEBUG
except:
    logging.critical("Missing functions.py!")
    print("Missing functions.py! Exiting...")
    sys.exit()


# Nmap's top 20 ports
top20 = {21 : 'ftp',
            22 : 'ssh',
            23 : 'telnet',
            25 : 'smtp',
            53 : 'dns',
            80 : 'http',
            110 : 'pop3',
            111 : 'rpcbind',
            135 : 'msrpc',
            139 : 'netbios-ssn',
            143 : 'imap',
            443 : 'https',
            445 : 'microsoft-ds',
            993 : 'imaps',
            995 : 'pop3s',
            1723 : 'pptp',
            3306 : 'mysql',
            3389 : 'ms-wbt-server',
            5900 : 'vnc',
            8080 : 'http-proxy'
            }


# Call functions
fn.targetDef()
fn.banner(fn.targetIP)
fn.portCheck(top20)
fn.results(fn.resultDict)
