from string import Template

a, b = 10, 100

# Old style
print('Sum: %d Product: %d' % (a + b, a * b))

# New style
print('Sum: {} Product: {}'.format(a + b, a * b))
print('Sum: {sum} Product: {product}'.format(sum=a+b, product=a*b))

# String Literals
print(f'Sum: {a + b} Product: {a * b}')

# String Template
t = Template('Sum: $sum Product: $product')
print(t.substitute(sum=a+b, product=a*b))
