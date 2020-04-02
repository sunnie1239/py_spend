product = []

while True :
	item = input("今天買了什麼? (離開則輸入q)")
	if item == 'q' :
		break
	price = input('請輸入金額:')
	# p = []
	# p.append(item)
	# p.append(price)
	# product.append(p)
	product.append([item, price]) # 二維list

print(product)    