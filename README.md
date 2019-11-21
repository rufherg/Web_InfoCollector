# Web_InfoCollector
基于celery+redis分布式队列框架的web信息收集器

用于渗透测试前期收集target的各种信息

## 使用方法

安装基本依赖库（celery + redis）

```shell
$ pip install -r requirements.txt
```

参数说明

```shell
$ python Web_Info.py
usage: Web_Info.py [-h] [-u URL] [-p PORT] [-m]

Web Information Collector

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     目标URL
  -p PORT, --port PORT  待扫描的端口范围(默认1-65535)
  -m, --max             最高线程模式(max=100)
```

eg:

```shell
$ python Web_Info.py -u www.baidu.com -p 1-100 -m
```

注：

- 此处url可以填带协议的url，也可以为ip地址，也可以为域名
- 参数port，可以填单个端口，也可以为一个端口范围，默认为1-65535（全部端口）

## TODO

- 增加子域名爆破、C段扫描
- 扫描报告导出
- 重构任务的分发
- 多线程的优化
- to be continue