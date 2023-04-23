import logging
import os
from datetime import datetime


class Log:
    def __init__(self, logger=None):
        # 创建logger对象
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%('
                                      'message)s')
        self.log_path = os.getcwd() + '/../logs'
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)
        self.log_name = os.path.join(self.log_path, datetime.now().strftime('%Y-%m-%d') + '.log')

        # 创建不同类型的handler
        fh = logging.FileHandler(self.log_name, 'a')  # 'a'追加模式
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 设置格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        # 关闭
        fh.close()
        ch.close()

    def getlog(self):
        """
        获取日志对象
        :return:
        """
        return self.logger
