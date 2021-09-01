import urllib.request as req

# ああああ import requests

url = 'https://script.google.com/macros/s/AKfycbwt6VY5zjFc3h0jga5qLyxzRdCwrmhhZva_1z9251ga3wUgj_f1eTTwlwigW6OJtyJXsQ/exec'


import requests

def main():
	data = {
		'functionName': 'SetCellValuesStringedArray',
		'stringedArray': 'AAA\nBBB\n\nCCC\nDDD\n\nXXX\nYYY\n\nAAA\nBBB\n\nCCC\nDDD\n\nXXX\nYYY'
	}
	response = requests.post(url, data)
	print(response.status_code)    # HTTPのステータスコード取得
	print(response.text)	# レスポンスのHTMLを文字列で取得

if __name__ == "__main__":
	main()

