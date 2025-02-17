import datetime
import sys
import logging

# 日志配置文件
from copy import deepcopy

_filename = 'log.txt'
# _format = "%(asctime)-15s [%(levelname)s] [%(name)s] %(message)s"
_format = "%(asctime)-15s %(message)s"
_datefmt = "%Y/%m/%d %H:%M:%S"
_level = logging.DEBUG

if _filename:
    handlers = [logging.StreamHandler(sys.stdout), logging.FileHandler(_filename)]
else:
    handlers = [logging.StreamHandler(sys.stdout)]

logging.basicConfig(format=_format, datefmt=_datefmt, level=_level, handlers=handlers)

# 目前查询的$symbol均为：<货币>USTD (可选：{ USDT, BTC })
# 时间间隔均为1min(可选：{ 1min, 5min, 15min, 30min, 60min, 1day, 1mon, 1week, 1year })
SYMBOL = "USDT"
PERIOD = "1min"

# 计算n分钟内的涨跌幅
N_MINUTES_STATE = 10

# 当达到以下值，发出警报通知，触发下一步动作
PRICE_ALERT_INCREASE_POINT = 1.25
PRICE_ALERT_DECREASE_POINT = -1.25

# 买入和卖出策略目前写死在代码里
# 卖出策略 - 达到PRICE_ALERT_DECREASE_POINT时
# 以当时的成交价格卖出，如果这种货币为降幅最小两个之一，则等待不卖出

# 买入策略 - 达到PRICE_ALERT_INCREASE_POINT时
# 以60%和40%的比例分别买涨价最高/次高的

# 设定参考货币的类型，权重及初始默认拥有的货币数量
COINS = {
    "BTC": {
        "WEIGHT": 1,
        "AMOUNT": 0
    },
    # "BCH": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # },
    # "ETH": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # },
    # "LTC": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # },
    # "XRP": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # },
    # "DASH": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # },
    # "ETC": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # },
    # "EOS": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # },
    # "OMG": {
    #     "WEIGHT": 1,
    #     "AMOUNT": 0
    # }
}

# 用户当前USDT账户余额
USDT_CURRENCY = 0

# 备份原始COIN/CURRENCY数据，作对比用
ORIGINAL_USDT_CURRENCY = USDT_CURRENCY
ORIGINAL_COINS = deepcopy(COINS)
ORIGINAL_WEALTH = None

# 将从火币上获取到的交易信息保存到数据库(mongodb)
DATABASE_RECORD = False

# 配置以下项目以初始化数据库
DATABASE_SERVER_ADDRESS = None
DATABASE_SERVER_PORT = 27017
DATABASE_NAME = "huobi_exchange"

# 这里的模拟起止仅用于数据库交易模拟分析
SIMULATE_START = datetime.datetime(2017, 12, 1, 0, 0, 0)
SIMULATE_END   = datetime.datetime.now()

# 如果数据库有用户名/密码，则定义如下
DATABASE_SERVER_USERNAME = None
DATABASE_SERVER_PASSWORD = None

# 邮件通知，配置SMTP，获取其AuthCode即可发送邮件
MAIL_ACCOUNT = None
MAIL_AUTH_CODE = None
MAIL_RECEIPIENTS = []
