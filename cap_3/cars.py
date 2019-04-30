cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars, 'lista certa')
print(sorted(cars), 'ordem temporária')
print(cars, 'lista deppois do sorted')
cars.sort(reverse=True)
print(cars, 'lista depois do sort (reverse = True)')
cars.reverse()
print(cars, 'lista depois do reverse')
print(len(cars))
