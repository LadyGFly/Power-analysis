# 学号:202056230
# 姓名:郭武钢
# 操作时间:2022/5/13 23:42
import pandas as pd
import csv
import os
# 导入excel数据表
df = pd.read_excel("1647848272130494.xlsx")
# #显示所有列
pd.set_option('display.max_columns', None)
# #显示所有行
pd.set_option('display.max_rows', None)
# """

dirPath = '用户类型.csv'
try:
    csvfile = open(dirPath,"w",encoding='utf-8-sig')
    writer = csv.writer(csvfile)
    # 写入标题
    writer.writerow(['用户编号',"平均缴费金额",'平均缴费次数','用户类型'])
    # 求用户的平均缴费金额
    idx = 1000000001
    for key in range(100):
        user = df.loc[df['用户编号'] == idx]
        temp = user['缴费金额（元）']
        # 每个用户的平均缴费金额
        ave_money = temp.mean()
        # 用户总缴费次数
        count = len(temp)
        maxVal = str(user['缴费日期'].values.max())
        minVal = str(user['缴费日期'].values.min())
        # 用户缴费用时几年
        use_year = int(maxVal[:4]) - int(minVal[:4]) + 1
        # 用户平均缴费次数
        ave_give = count // use_year
        print('用户：', str(idx), '平均缴费金额为:', ave_money, '平均缴费次数为:', ave_give)
        # 平均金额
        ave_total = df['缴费金额（元）'].mean()
        # 平均次数
        ave_count = len(df) // 200
        # 用户类型
        user1 = str('高价值型用户')
        user2 = str('潜力型用户')
        user3 = str('大众型用户')
        user4 = str('低价值型用户')
        # 大于等于平均次数且大于等于平均缴费金额
        if ave_money >= ave_total and ave_give >= ave_count:
            user_type = user1
            print('用户：', str(idx), '为',user_type)
        # 大于等于平均次数且小于平均缴费金额
        elif ave_money >= ave_total and ave_give < ave_count:
            user_type = user2
            print('用户：', str(idx), '为',user_type)
        # 小于平均次数且大于等于平均缴费金额
        elif ave_money < ave_total and ave_give >= ave_count:
            user_type = user3
            print('用户：', str(idx), '为',user_type)
        # 小于平均次数且小于平均缴费金额
        elif ave_money < ave_total and ave_give < ave_count:
            user_type = user4
            print('用户：', str(idx), '为',user_type)
        writer.writerow([idx,ave_money,ave_give,user_type])
        idx += 1
finally:
    print('Three maybe')
