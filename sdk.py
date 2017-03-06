from facebookads.api import FacebookAdsApi
from facebookads import objects

my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
my_access_token = 'EAACEdEose0cBAMgQZB3wMK10JoqkfoVvR91hG07dRHot7eCI8tiZBoddUjD9wkXyRtQHZAg7TZC1PIFLfZCBQMbXq7chbFe458kGIP6wbPQYJz0ZCOg8303oD9NKZAwWqzrFbkCbJ6ufkJjh7SS0OV3yB6lzbT4tGX38K6oZBCnLijptAONq6kKZB2WTlylZAqD2RX5nPZCks3GgwZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = objects.AdUser(fbid='me')
print(me.get_ad_accounts())