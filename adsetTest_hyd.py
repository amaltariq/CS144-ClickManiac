from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import AdSet
from facebookads.adobjects.targetingsearch import TargetingSearch 
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.adaccount import AdAccount
import datetime
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebookads.adobjects.ad import Ad

#### Access Credentials ######################################################
my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
my_access_token = 'EAAEQRPLI1TYBAL52HZBz9FukEcoeHNTjaQP3kAWz0T3AtiDKC6A1ZA0LEX3auJJGKHZCZAANwAPgNBkJQGYAFuo5hqqoJ50UWSrQdomGxWCIOItdUdlhAV5HMN6AHh5E5KYHi40TV49eleTFiujRUmIdyDIBt1CTP9mGMTC0jAZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

#### Get the SDK campaign ID and account ID ##################################
me = objects.AdUser(fbid='me')
ad_accounts = me.get_ad_accounts()
my_account_id = ad_accounts[0]["account_id"]    # my account id = 196943804042546
my_id = ad_accounts[0]["id"]                    # my id =  act_196943804042546


#### Specify Adset Targeting #################################################
# Use these queries with TargetingSearch.search(query) to get the actual ad
#   interest ID, this will be used in the targeting specifications
params_charity = {
    'q': 'charity',
    'type': 'adinterest'
}
params_commissues = {
    'q': 'Community issues',
    'type': 'adinterest'
}
params_volunteering = {
    'q': 'Volunteering',
    'type': 'adinterest'
}

params_nonprofitorg = {
    'q': 'Nonprofit organization',
    'type': 'adinterest'
}

params_animal = {
    'q': 'animals',
    'type': 'adinterest'
}
params_disneychannel = {
    'q': 'Disney Channel',
    'type': 'adinterest'
}
params_disneyprincess = {
    'q': 'Disney Princess',
    'type': 'adinterest'
}
params_frozenmovie = {
    'q': 'Frozen (2013 film)',
    'type': 'adinterest'
}
params_frozenfranchise = {
    'q': 'Frozen (franchise)',
    'type': 'adinterest'
}

# Run TargetingSearch.searc(params) to get the actual interests corresponding
#   to the queries above. 
int_charity = TargetingSearch.search(params=params_charity)
int_commissues = TargetingSearch.search(params=params_commissues)
int_volunteering = TargetingSearch.search(params=params_volunteering)
int_nonprofitorg = TargetingSearch.search(params=params_nonprofitorg)

int_animal = TargetingSearch.search(params=params_animal)
int_disneychannel = TargetingSearch.search(params=params_disneychannel)
int_disneyprincess = TargetingSearch.search(params=params_disneyprincess)
int_frozenmovie = TargetingSearch.search(params=params_frozenmovie)
int_frozenfranchise = TargetingSearch.search(params=params_frozenfranchise)

'''
# Getting the city ID of Hyderabad, India
params = {
    'q': 'hyderabad',
    'type': 'adgeolocation',
    'location_types': ['city'],
}

resp = TargetingSearch.search(params=params)
print(resp)
'''

# Specify Targeting
targeting = {
     # Specify radius of 12 miles around New Delhi
    'geo_locations': {
        'cities' : [{'key': '1027234', 'radius':12, 'distance_unit':'mile'}]
    },
    'age_min': 13,
    'age_max': 35,
    'flexible_spec': [
      {
        # Target people who are interested in one of the below issues
        'interests': [
            {'id': int_charity[0]['id'],'name': int_charity[0]['name']},
            {'id': int_animal[0]['id'],'name': int_animal[0]['name']},
            {'id': int_commissues[0]['id'], 'name': int_commissues[0]['name']},
            {'id': int_volunteering[0]['id'], 'name': int_volunteering[0]['name']},
            {'id': int_nonprofitorg[0]['id'], 'name': int_nonprofitorg[0]['name']},],
        # or friend of someone who's liked the page
        'friends_of_connections': [
            {'id':103185246428488},],
      },
    ],
}

# Create the Adset
adset = AdSet(parent_id=my_id)
campaign_id = '23842548820110548'

my_page_id = '103185246428488'      # Ideas Behind the Web page ID

# Update the Adset
adset.update({
    AdSet.Field.name: 'Hyderabad Test-Ignore',
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.daily_budget: 100,
    AdSet.Field.promoted_object: {
        'page_id': my_page_id,
    },
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.targeting: targeting,
    AdSet.Field.is_autobid: True,

})

# Remotely create the adset
print("Updated adset")
adset.remote_create(params={
    'status': AdSet.Status.active,
})
print("remote created adset")