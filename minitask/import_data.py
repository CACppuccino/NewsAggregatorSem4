import pandas as pd
import requests
import json

"""
Need to create the index first before using this script
curl -XPUT https://localhost:9200/example3 --insecure -u admin:admin
"""
URL = 'https://localhost:9200/example3/_doc/'
def start_import():
    df = pd.read_csv('./extractor.csv')
    # print(df.iloc[0])
    for index, row in df.iterrows():
        data=dict(title=row['article_title'], url=row['article_url'], content=row['article_content'])
        print('inserting:', data['title'])
        res = requests.post(URL+str(index), json=data, auth=('admin', 'admin'), verify=False)
        print('get response: ', res.text)
        if res.json().get('status', 200) >= 400:
            print('*'*90)

if __name__ == '__main__':
    start_import()
