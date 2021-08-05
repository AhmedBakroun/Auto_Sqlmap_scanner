# Tested on Windows 10 Python3.7.9
# Author : Lyscf
# 2021.8.4 V1.3
import requests

def get_payload(taskID):
    url = 'http://127.0.0.1:8775/scan/' + taskID + '/data'
    res = requests.get(url)
    print(res.json())
    jsons = res.json()
    print(jsons['data'])
    data = str(jsons['data'])
    result_file = open('sqlmapresult.txt', 'a+', encoding='utf-8')
    # for line in data:
    #    if '{' in line:
    #        result_file.write(line + '\n')
    #    elif'}' in file:
    #        result_file.write(line + '\n')
    #    elif '[' in line:
    #        result_file.write(line + '\n')
    #    elif ']' in line:
    #        result_file.write(line + '\n')
    #   else:
    #        result_file.write(line)
    # 别看了换行不可能修了 这辈子都不可能修了
    result_file.write(data+'\n')
    result_file.close()

    return jsons['data']

def get_scan_result(taskID):
    url = 'http://127.0.0.1:8775/scan/' + taskID + '/data'
    res = requests.get(url)
    payloaad = res.text
    if 'payload' in payloaad:
        print('[√]inject successful!!!')
        return True
    else:
        print('[×]inject faild')
        return False
print('救灾用，请确保taskids.txt还在')
file = open('taskids.txt', 'r')
for id in file:
    id = id.strip('\n')
    if get_scan_result(id) == True:
        get_payload(id)
    else:
        continue
