product = []

# 讀取檔案並存入list
with open('spend.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		# s = line.strip().split(',')
		# product.append(s)
		# 可化簡為以下
		item, price = line.strip().split(',') 
		product.append([item, price])

# 取得新資料
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

# 寫入檔案
with open('spend.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in product:
		f.write(p[0] + ',' + p[1] + '\n')