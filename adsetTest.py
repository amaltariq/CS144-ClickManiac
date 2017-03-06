from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import AdSet
from facebookads.adobjects.targetingsearch import TargetingSearch 
from facebookads.adobjects.targeting import Targeting
import datetime
from facebookads.adobjects.campaign import Campaign

my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
my_access_token = 'EAAEQRPLI1TYBAL52HZBz9FukEcoeHNTjaQP3kAWz0T3AtiDKC6A1ZA0LEX3auJJGKHZCZAANwAPgNBkJQGYAFuo5hqqoJ50UWSrQdomGxWCIOItdUdlhAV5HMN6AHh5E5KYHi40TV49eleTFiujRUmIdyDIBt1CTP9mGMTC0jAZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

me = objects.AdUser(fbid='me')
ad_accounts = me.get_ad_accounts()
#print(ad_accounts)

my_account_id = ad_accounts[0]["account_id"]
# my account id = 196943804042546
my_id = ad_accounts[0]["id"]
# my id =  act_196943804042546

# create an ad set.
# define target audience
params = {
	'type': 'adgeolocationmeta',
	'zips': ['US:91126','US:95014'],
	'location_types':['zip'],
}
params1 = {
	'type': 'adinterestvalid',
	'interest_list':[ 'Charity and causes', 'Japan'],
}
params2 = {
	'q': 'charity',
	'type': 'adinterest'
}

resp = TargetingSearch.search(params=params2)

targeting = {
	'geo_locations': {
		'countries': ['Vietnam'],
	},
	'age_min': 13,
	'age_max': 30,
	'interests': [
		{
			# Charity and causes
			'id': resp[0]["id"],
			'name': resp[0]["name"]
		},
	],
}


adset = AdSet(parent_id=my_id)
campaign_id = '23842548820110548'
#campaign = Campaign(campaign_id)
#campaign.remote_read(fields=[Campaign.Field.name, Campaign.Field.objective,])
#print(campaign)

# Update adset
adset.update({
	AdSet.Field.name: 'My AdSet',
	AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
	AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
	AdSet.Field.daily_budget: 200,
	AdSet.Field.campaign_id: campaign_id,
	AdSet.Field.targeting: targeting,
	AdSet.Field.is_autobid: True,
})
print("Updated adset")
print(adset)
adset.remote_create(params={
	'status': AdSet.Status.paused,
})


print("Paused adset")
