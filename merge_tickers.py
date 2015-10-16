import sys
import json
import pandas as pd
import numpy as np

def read_to_pd(ticker):
	# read data from current file path for the specified ticker
	t = open('/home/brien/kirill/repo/data/transcript/tt/json/'+ticker, 'r').read()
	tq = open('/home/brien/kirill/repo/data/transcript_quarters/json/'+ticker, 'r').read()
	
	# json ticker data extracted from the raw files
	t_data = json.loads(t)["result"]["docs"]
	tq_data = json.loads(tq)["result"]

	# pandas dataframes made from the ticker data
	t_pd = pd.DataFrame(t_data)
	tq_pd = pd.DataFrame(tq_data)

	# merge some tq datafields into the same names as t
	tq_pd["id"] = tq_pd["docid"]
	tq_pd["title"] = tq_pd["doctitle"]
	del tq_pd["docid"]
	del tq_pd["doctitle"]

	# return dataframes
	return t_pd, tq_pd

def concat_pd(df1,df2):
	# concatenate the dataframes and drop duplicates based on ID
	return pd.concat([df1, df2])#.groupby("id",sort=True)#.drop_duplicates(subset="id")

def combine_pd(ticker):
	tickers = read_to_pd(ticker)	
	return merge_pd(tickers[0],tickers[1])

def merge_pd(df1,df2):
	return pd.merge(left=df1, right=df2, how="outer",  left_on="id", right_on="id")

def pd_to_json(result):
	# convert dataframes back into json; might be useful later
	return pd.DataFrame.to_json(result)

if __name__ == '__main__':
	for ticker in sys.argv[1:]:
		print(combine_pd(ticker))
		#print(merge_pd(read_to_pd(ticker)))
