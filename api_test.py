import requests

# ========================== API fields ==========================

cid = 'YmZmNTAxOTE3NzI4OGE5OWJkNzBjZGE1NWI1Yjk3Nzg2'
s = 'KScIU4ZRGgvU1kBYr3QJCWFf6R9tyPn6AphCcIVL'

root_dev_url = 'http://sandbox.delivery.com'
root_prod_url = 'https://api.delivery.com'

merchant_search_url = '/merchant/search/'

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
  return merchants


merchants = test_search()
print merchants.keys()

print merchants['cuisines'] + '\n'
print len(merchants['merchants']) + '\n'
print merchants['message'] + '\n'
print merchants['categories'] + '\n'
print merchants['verticals'] + '\n'
print merchants['cuisines'] + '\n'
