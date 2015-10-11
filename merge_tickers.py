import sys
import json
import pandas as pd
import numpy as np

def read_to_pd(ticker):
	# read data from current file path for the specified ticker
	t = open('/home/brien/kirill/repo/data/transcript/tt/json/'+ticker, 'r').read()
	tq = open('/home/brien/kirill/repo/data/transcript_quarters/json/'+ticker, 'r').read()
	
	# json ticker data; saving in separate variables in case it's useful later
	t_data = json.loads(t)["result"]["docs"]
	tq_data = json.loads(t)["result"]["docs"]

	# pandas dataframes made from the ticker data
	t_pd = pd.DataFrame(t_data)
	tq_pd = pd.DataFrame(tq_data)

	# merge the dataframes using the function below
	result = merge_json(t_pd, tq_pd)

	return result

def merge_json(pd1, pd2):
	# concatenate the dataframes and drop duplicates based on ID
	return  pd.concat([pd1, pd2]).drop_duplicates(subset="id")

def pd_to_json(result):
	# convert dataframes back into json; might be useful later
	return pd.DataFrame.to_json(result)

if __name__ == '__main__':
	for ticker in sys.argv[1:]:
		result = read_to_pd(ticker)
		print(result)
		
