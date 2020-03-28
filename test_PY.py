
import pandas as pd
columns = ['bird', 'cow', 'pig']
df = pd.DataFrame(columns = columns)
print (df)
testdf = pd.DataFrame([[1,1,1]], columns = columns)
df = pd.concat([df, testdf], ignore_index=True)
df.to_csv('test.csv', index=False)
print (df)
