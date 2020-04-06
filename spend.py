import os

# 讀取檔案並存入list
def read_file(filename):
	product = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line: # 遇到標題則跳至下一迴圈
				continue
			item, price = line.strip().split(',') 
			product.append([item, price])
	return product

# 取得新資料
def user_input(product):
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
	return product

# 依序列出資料內容
def print_data(product):
	# for i in range(len(product)) :
	# 	print(product[i][0], '價格是', product[i][1])
	for p in product :
		print(p[0], '價格是', p[1])

# 寫入檔案
def write_file(filename, product):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')

# 主程式
def main():
	filename = 'spend.csv'
	# 檢查檔案是否存在
	if os.path.isfile(filename): 
		print('檔案已存在')
		product = read_file(filename)
	else:
		print('檔案不存在')
		product = []

	product = user_input(product)
	print_data(product)
	write_file(filename, product)

#程式執行
main()