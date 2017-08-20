#!/user/bin/python

import requests

# class CryptoCurrencyPrice:
class BxPrice():
	def lastPrice(self):
		response = requests.get("https://bx.in.th/api/")
		self.data = response.json()

	def GetlastPrice(self):
		response = requests.get("https://bx.in.th/api/")
		_data = response.json()
		return(_data)

	def GetBTCtoTHB(self):
		# self.lastPrice()
		return(self.data['1']['last_price'])

	def GetETHtoTHB(self):
		# self.lastPrice()
		return(self.data['21']['last_price'])

	def GetBTCtoZEC(self):
		# self.lastPrice()
		return(self.data['8']['last_price'])

	def GetZECtoTHB(self):
		# self.lastPrice()
		_btc = self.data['1']['last_price']
		_zecTobtc = self.data['8']['last_price']
		'''

		_btc      1
		----- = -----
		  x    _zecTobtc

		'''
		res = float(_zecTobtc) * float(_btc)
		return(res)
		# return(self.data['8']['last_price'])


class CryptopiaPrice():
	def lastPrice(self):
		response = requests.get("https://www.cryptopia.co.nz/api/GetMarkets/12")
		self.data = response.json()

	def GetSigttoBTC(self):
		# x=0
		# for i in self.data['Data']:
		# 	print(str(x) + " ===> " + str(i))
		# 	x+=1
		return(("%.8f" % ((self.data['Data'])[1043]["LastPrice"])))
		

if __name__ == '__main__':
	c = BxPrice()
	c.lastPrice()
	# print(c.GetBTCtoTHB())
	# print(c.GetETHtoTHB())
	# print(c.GetBTCtoZEC())
	# print(c.GetZECtoTHB())
	cr = CryptopiaPrice()
	cr.lastPrice()
	print(cr.GetSigttoBTC())
	# cr.GetBTCtoSigt()

