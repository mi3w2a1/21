#!/usr/bin/env python
# coding: utf-8

url = 'https://script.google.com/macros/s/AKfycbwt6VY5zjFc3h0jga5qLyxzRdCwrmhhZva_1z9251ga3wUgj_f1eTTwlwigW6OJtyJXsQ/exec'

import requests

def main():
	data = {
		'functionName': 'SetCellValuesStringedArray',
		'stringedArray': 'abcd\nzxcv\n\nqwer\n123DDD\n\n123XXX\ntestYYY\n\ntestAAA\ntestBBB\n\ntestCCC\ntestDDD\n\ntestXXX\ntestYYY'
	}
	response = requests.post(url, data)
	print(response.status_code)    # HTTPのステータスコード取得
	print(response.text)	# レスポンスのHTMLを文字列で取得

if __name__ == "__main__":
	main()

