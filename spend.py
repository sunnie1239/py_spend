product = []

while True :
	item = input("今天買了什麼? (離開則輸入q) ")
	if item == 'q' :
		break
	price = input('請輸入金額: ')
	# p = []
	# p.append(item)
	# p.append(price)
	# product.append(p)
	product.append([item, price]) # 二維list

print('product list 的資料內容: ', product)    
print('product list 有幾個項目: ', len(product))

# 依序列出資料內容
# for i in range(len(product)) :
# 	print(product[i][0], '價格是', product[i][1])
for p in product :
	print(p[0], '價格是', p[1])