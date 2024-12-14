import pandas as pd

pd.set_option('display.max_colwidth', None)

df = pd.read_pickle("./greek-tragedy-by-line.pickle")

for i in list(df['text']):
    print(i)