'''
Each package has a __init__.py file which makes it a package in python

package can be imported two ways

from ecommerce import shipping (Here shipping is a module)
from ecommerce.shipping import rate (rate is a function here)

'''

from shopping import shopping
from ecommerce import shipping

shipping.ship(10)

shopping.shipping_rates("10$")
