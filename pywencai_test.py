import pywencai
import pandas as pd
from pandas import DataFrame
# import os

def query_wencai(query):
    res = pywencai.get(question=query, loop=True)
    print(res)

    print(type(res))
    print(res.keys())

    for key in res.keys():
        print(f'==== key = {key}')
        print(res[key])
        print(type(res[key]))

        if type(res[key]) is DataFrame:
            print('获取到DataFrame数据')
            df = DataFrame(res[key])
            # print(df.keys())
            #
            # i = 0
            # for df_key in df.keys():
            #     print(f'==== {i} ====')
            #     i += 1
            #     print(f"{df_key}:  {df.loc[:, df_key]}")

            return df
    return None

query_lst = {
        '长电科技 主力资金&资金',
        '中芯国际 主力资金&资金',
        '宁德时代 主力资金&资金',
        '北方华创 主力资金&资金'
        }
for query in query_lst:
    df = query_wencai(query)
    # os.getcwd()  # 获取当前工作路径

    df.to_csv('result.csv', mode='a')


