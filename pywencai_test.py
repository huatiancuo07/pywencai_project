import pywencai
import pandas as pd
from pandas import DataFrame
import os
import time

filepath = 'result.csv'

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

def get_results(query_lst):

    for query in query_lst:
        df = query_wencai(query)
        # os.getcwd()  # 获取当前工作路径
        df["search_time"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        return df

def save_to_csv(df):
    filepath = 'result.csv'

    if os.path.exists(filepath):  # 文件已存在
        df.to_csv(filepath, mode='a', header=False, index=None)
    else:
        df.to_csv(filepath, index=None)




if __name__ == '__main__':
    query_lst = {
        '长电科技 主力资金&资金',
        '中芯国际 主力资金&资金',
        '宁德时代 主力资金&资金',
        '北方华创 主力资金&资金'
    }

    df = get_results(query_lst)
    save_to_csv(df)

    # df = pd.read_csv(filepath)
    # print(df.head())

