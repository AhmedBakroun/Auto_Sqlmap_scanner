# Tested on Windows 10 Python3.7.9
# Author : Lyscf
# 2021.8.4 V1.3

from Auto_Sqlmap_scanner.main import get_scan_result, get_payload

print('救灾用，请确保taskids.txt还在')
file = open('taskids.txt', 'r')
for id in file:
    id = id.strip('\n')
    if get_scan_result(id) == True:
        get_payload(id)
    else:
        continue
