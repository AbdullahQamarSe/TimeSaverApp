"""
from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection

# optional, use this on Linux and if you are not logged in when using nordvpn command

# optional, use this on Linux and if you are not logged in when using nordvpn command

settings = initialize_vpn("France", "1hZV8hPzFtW2YGhZ6pZPY7gK", "ZaBq4vm9cfZVYrGbKigAjTZ4")  # starts nordvpn and stuff
rotate_VPN(settings)  # actually connect to server
print('hello')

close_vpn_connection(settings)

"""
from nordvpn_switcher import initialize_VPN,rotate_VPN
import time

instr = initialize_VPN(area_input=["spain"],skip_settings=1)

for i in range(3):
    rotate_VPN(instr)
    print('\nDo whatever you want here (e.g. scraping). Pausing for 10 seconds...\n')
    time.sleep(10)
