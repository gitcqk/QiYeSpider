# -*- coding: utf-8 -*-

# Scrapy settings for qyxx project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qyxx'

SPIDER_MODULES = ['qyxx.spiders']
NEWSPIDER_MODULE = 'qyxx.spiders'


# 设置增量式爬虫
# DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# SCHEDULER_PERSIST = True
# REDIS_URL = 'redis://122.114.250.225:6379'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qyxx (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 关闭robots.txt 规则
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 设置下载延迟
DOWNLOAD_DELAY = 5.5

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qyxx.middlewares.QyxxSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 启用浏览器中间件
DOWNLOADER_MIDDLEWARES = {
    'qyxx.middlewares.SeleniumMiddleware': 300,
#    'qyxx.middlewares.QyxxDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'qyxx.pipelines.QyxxPipeline': 300,
}

# Mysql 配置信息
# 根据服务器进行修改
MYSQL_HOST = '122.114.250.225'
MYSQL_DBNAME = 'qyxx'     # 数据库名
MYSQL_USER = 'root'         # 数据库用户
MYSQL_PASSWORD = '********'   # 数据库密码
MYSQL_PORT = 3306

# 定义显示日志的等级
LOG_LEVEL = "WARNING"



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
