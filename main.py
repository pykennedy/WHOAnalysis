import numpy as np
import pandas as pd
import tabulate as tb

pd.options.display.max_columns = None
pd.options.display.width = None


def as_table(dataframe):
    return tb.tabulate(dataframe, 'firstrow', 'psql')


df = pd.read_csv("data/30-70cancerChdEtc.csv")
print(as_table(df.head()))
