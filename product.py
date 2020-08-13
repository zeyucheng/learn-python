import os
def read_file(filename):
	product = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name,price = line.strip().split(',')
			product.append([name,price])
	return product

def user_input(product):
	while True:
		name = input('plz input the name of the product:')
		if name == 'q':
			break
		price = input('plz input the price of the product:')
		product.append([name,price])
	return product

def print_products(product):
	for p in product:
		print(p[0] + ' is ' + p[1] + ' dollars')

def write_file(filename, product):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('product name,product price\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	products = []
	if os.path.isfile(filename):
		print('file load success')
		products = read_file(filename)
	else:
		print('file is not exist')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
