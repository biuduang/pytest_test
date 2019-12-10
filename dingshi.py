#
# from datetime import datetime
# from datetime import date
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# def job(text):
#     print(text)
#
# scheduler = BlockingScheduler()
# # 在 2019-8-30 运行一次 job 方法
# scheduler.add_job(job, 'date', run_date=date(2019, 8, 30), args=['text1'])
# # 在 2019-8-30 01:00:00 运行一次 job 方法
# scheduler.add_job(job, 'date', run_date=datetime(2019, 8, 30, 1, 0, 0), args=['text2'])
# # 在 2019-8-30 01:00:01 运行一次 job 方法
# scheduler.add_job(job, 'date', run_date='2019-8-30 01:00:00', args=['text3'])
#
# scheduler.start()

# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test(x):
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)

scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, args=('你好',), trigger='cron', second='*/5')
scheduler.start()
