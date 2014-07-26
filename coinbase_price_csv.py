import pandas as pd


f=open('history.csv','w')
f.truncate()
f.close()


i=0
while True:
    next=pd.read_csv('https://coinbase.com/api/v1/prices/historical?page='+str(i))
    if next.empty:
        break
    next.to_csv('history.csv',mode='a',index=False,header=False)
    i+=1
    
