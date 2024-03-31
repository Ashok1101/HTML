import pandas as pd
df = pd.read_csv("C:/Users/Arvind/Desktop/News/news.csv")
a=df[df.title=="Kerry to go to Paris in gesture of sympathy"]
print(a.label)