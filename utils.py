# 1.导包
import logging
from logging import handlers
import app

# 2.定义初始化日志函数
def init_log():
    # 定义日志器
    logger = logging.getLogger()  # 初始化日志对象
    logger.setLevel(logging.INFO)  # 定义日志级别

    # 定义处理器
    sh = logging.StreamHandler()
    log_file = app.BASE_DIR + "/log/Ego.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_file,  # 定义日志名称
                                                   when="D",  # 定义记录日志时间：天
                                                   interval=1,  # 定义记录日志的频率，
                                                   backupCount=7,  # 保存日志的时间
                                                   encoding="UTF-8")  # 字符编码格式
    # 定义格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 设置处理日志的格式
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
