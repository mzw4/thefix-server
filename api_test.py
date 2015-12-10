import requests

# ========================== API fields ==========================

cid = 'YmZmNTAxOTE3NzI4OGE5OWJkNzBjZGE1NWI1Yjk3Nzg2'
s = 'KScIU4ZRGgvU1kBYr3QJCWFf6R9tyPn6AphCcIVL'

root_dev_url = 'http://sandbox.delivery.com'
root_prod_url = 'https://api.delivery.com'

merchant_search_url = '/merchant/search/'
merchant_menu_url = '/merchant/{merchant_id}/menu'

customer_info_url = '/customer/account'


# /merchant/search/delivery?client_id=abc123&address=199 Water St 10038

# ========================== Functions ==========================

def test_search(addr='4-75 48th Ave, Long Island City, NY 11109', merchant_type='R'):
  params = {
    'client_id': cid,
    'address': addr,
    'merchant_type': merchant_type
  }
  result = requests.get(root_dev_url + merchant_search_url + 'delivery', params=params)
  merchants = result.json()

  print merchants.keys()

  print '\nCuisines'
  print merchants['cuisines']
  print 'Message\n'
  print merchants['message']
  print 'Categories\n'
  print merchants['categories']
  print 'Vertical\n'
  print merchants['verticals']
  print 'Popular cuisines\n'
  print merchants['popular_cuisines']
  print 'Promoted Ids\n'
  print merchants['promoted_merchants_id']
  print '\nMerchants'
  print merchants['merchants']

def test_customer_info():
  # requires access token
  pass

def test_menu(merchant_id='63823'):
  params = {
    'client_id': cid
  }
  result = requests.get(root_dev_url + merchant_menu_url.replace('{merchant_id}', merchant_id), params=params)
  menu = result.json()
  print menu.keys()

  print menu['menu'][0].keys()
  print menu['menu'][0]['description']

test_menu()




