import sys
import json
import pandas as pd
import numpy as np

def read_to_pd(ticker):
	t = open('/home/brien/kirill/repo/data/transcript/tt/json/'+ticker, 'r').read()
	tq = open('/home/brien/kirill/repo/data/transcript_quarters/json/'+ticker, 'r').read()
	
	# raw ticker data; keeping in separate variables in case I need to refind this later
	t_data = json.loads(t)["result"]["docs"]
	tq_data = json.loads(t)["result"]

	# pandas data to work with
	t_pd = pd.DataFrame(t_data)
	tq_pd = pd.DataFrame(tq_data)

	# run the merge function below on the pandas data
	result = merge_json (t_pd, tq_pd))

	return result

def merge_json(json1, json2):
	# combine the two dataframes and drop the duplicates
	return  pd.concat([json1, json2]).drop_duplicates(subset="id")

def pd_to_json(result):
	# for converting back to json (might be useful later)
	return pd.DataFrame.to_json(result)

if __name__ == '__main__':
	# run the script for each ticker argument
	for ticker in sys.argv[1:]:
		result = read_to_pd(ticker)
		print(result)
		
