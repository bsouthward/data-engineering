import sys
import json
import pandas as pd
import numpy as np

def read_to_pd(ticker):
	t = open('/home/brien/kirill/repo/data/transcript/tt/json/'+ticker, 'r').read()
	tq = open('/home/brien/kirill/repo/data/transcript_quarters/json/'+ticker, 'r').read()
	
	t_data = json.loads(t)["result"]["docs"]
	tq_data = json.loads(t)["result"]

	t_pd = pd.DataFrame(t_data)
	tq_pd = pd.DataFrame(tq_data)

	result = merge_json (t_pd, tq_pd) # pd.concat([t_pd, tq_pd]).drop_duplicates(subset="id")

	return result

def merge_json(json1, json2):
	return  pd.concat([json1, json2]).drop_duplicates(subset="id")

def pd_to_json(result):
	return pd.DataFrame.to_json(result)

if __name__ == '__main__':
	for ticker in sys.argv[1:]:
		result = read_to_pd(ticker)
		print(result)
		
