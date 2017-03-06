from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import AdSet
from facebookads.adobjects.targetingsearch import TargetingSearch 
from facebookads.adobjects.targeting import Targeting
import datetime


my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
my_access_token = 'EAAEQRPLI1TYBAL52HZBz9FukEcoeHNTjaQP3kAWz0T3AtiDKC6A1ZA0LEX3auJJGKHZCZAANwAPgNBkJQGYAFuo5hqqoJ50UWSrQdomGxWCIOItdUdlhAV5HMN6AHh5E5KYHi40TV49eleTFiujRUmIdyDIBt1CTP9mGMTC0jAZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = objects.AdUser(fbid='me')
ad_accounts = me.get_ad_accounts()
print(ad_accounts)

my_account_id = ad_accounts[0]["account_id"]
# my account id = 196943804042546
my_id = ad_accounts[0]["id"]
# my id =  act_196943804042546

# create an ad set.
# define target audience
params = {
	'q': 'baseball',
	'type': 'adinterest'
}
adset = AdSet(parent_id=my_id)
campaign_id = '23842548820110548'

# Update adset
adset.update({
	AdSet.Field.name: 'My AdSet',
	AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
	AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
	AdSet.Field.bid_amount: 150,
	AdSet.Field.daily_budget: 2000,
	AdSet.Field.campaign_id: campaign_id,
	AdSet.Field.targeting: {
		'geo_locations': {
			'countries': ['US'],
		},
		'relationship_statuses': [2],
		'user_adclusters': [
			{
				'id': 6002714886772,
				'name': 'Food & Dining',
			},
		],
	},
})
print("Updated adset")
print(adset)

# remote creating gives error message still. TODO
'''
  "error": {
    "message": "Invalid parameter",
    "error_user_msg": "Please specify a promoted object for the ad set.",
    "type": "OAuthException",
    "fbtrace_id": "FECaro17KfP",
    "is_transient": false,
    "error_user_title": "No promotion object found",
    "code": 100,
    "error_subcode": 1815430
'''

adset.remote_create(params={
	'status': AdSet.Status.paused,
})

'''
print("Paused adset")

'''