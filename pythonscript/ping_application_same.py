import cmd
import platform  # For getting the operating system name
import subprocess  # For executing a shell command


def ping(ip):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', '-c', '2', ip]

    if subprocess.call(command) == 0:
        msg = 'Ping  ' + ip + ' successfully :)'
    else:
        msg = 'Ping  ' + ip + ' failed :('

    return msg

host = '127.0.0.1'

ip1 = '172.18.0.2'
ip2 = '172.18.0.3'
ip3 = '172.18.0.4'
ip4 = '172.18.0.5'
print(ping(ip1))
print(ping(ip2))
print(ping(ip3))
print(ping(ip4))
