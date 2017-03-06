# sample target expansion data to use 
adset.update({
	AdSet.Field.name: 'My AdSet',
	AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
	AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
	AdSet.Field.bid_amount: 150,
	AdSet.Field.daily_budget: 2000,
	AdSet.Field.campaign_id: <CAMPAIGN_ID>,
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

#-----------------------
# target search code
params = {
	'q': 'baseball',
	'type': 'adinterest'
}

resp = TargetingSearch.search(params=params)
print(resp[0])
#'''
targeting = {
	'geo_locations': {
		'countries': ['Vietnam'],
	},
	'age_min': 13,
	'age_max': 30,
	'flexible_spec': [{
		'interests': [
			{
				'id': resp[0]["id"],
				'name': resp[0]["name"]
			},
		],
	},],
}

# Define how long the ad will run

today = datetime.date.today()

start_time = str(today + datetime.timedelta(hours=4))
end_time = str(today + datetime.timedelta(hours=10))

adset = AdSet(parent_id=my_id)
campaign_id = '23842548820110548'


adset.update({
	AdSet.Field.name: "Irene's test Ad Set",
	AdSet.Field.campaign_id: campaign_id,
	AdSet.Field.daily_budget: 200,
	AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
	AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
	AdSet.Field.bid_amount: 200,
	AdSet.Field.targeting: targeting,
	AdSet.Field.start_time: start_time,
	AdSet.Field.end_time: end_time,
})