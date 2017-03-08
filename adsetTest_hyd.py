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
params = {
    'q': 'hyderabad',
    'type': 'adgeolocation',
    'location_types': ['city'],
}

resp = TargetingSearch.search(params=params)
print(resp)
'''
targeting = {
    'geo_locations': {
        'cities' : [{'key': '1027234', 'radius':12, 'distance_unit':'mile'}]
        #'custom_locations': [
        #    {
        #        'latitude': 77.209, 
        #        'longitude': 22.6267,
        #        'radius': 50,
        #        'distance_unit': 'mile',
        #    },
        #],
        #'location_types':['recent', 'home'],
    },
    'age_min': 13,
    'age_max': 35,
    'flexible_spec': [
      {
        # Interested in one of the below issues
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
    # Exclude people who've already liked the page
    'exclusions': [
     {
       'connections': [{'id':103185246428488},],
     },
    ],
    
}

#print(targeting)

adset = AdSet(parent_id=my_id)
campaign_id = '23842548820110548'

#campaign = Campaign(campaign_id)
#campaign.remote_read(fields=[Campaign.Field.name, Campaign.Field.objective,])
#print(campaign)
'''

    AdSet.Field.pacing_type: ['day_parting'],
    AdSet.Field.adset_schedule: {
        'start_minute': 60,
        'end_minute': 540,
        'days': [0, 1, 2, 3, 4, 5, 6],
    }

today = datetime.date.today()
'''

my_page_id = '103185246428488'
# Update adset

#   AdSet.Field.start_time: str(datetime.datetime(year=2017, month=3, day=6, hour=1, minute=36)),
#   AdSet.Field.end_time: str(datetime.datetime(year=2017, month=3, day=6, hour=6, minute=0)),

adset.update({
    AdSet.Field.name: 'Hyderabad Test',
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



print("Updated adset")
adset.remote_create(params={
    'status': AdSet.Status.active,
})
print("remote created adset")
'''

a = adset.remote_read(fields=[AdSet.Field.id])
#my_adset_id = a["id"]
my_adset_id = "23842548820110548"
print("my adset id", my_adset_id)
# Should be: "23842548820110548"?

### AD CREATIVE SECTION
account = AdAccount(my_id)
images = account.get_ad_images()
#print(images)

image_path = '/Users/SeemaMacbook/Desktop/AmalsWork/CS:EE144/Projects/ClickManiac/clickmaniac-ads/homeless_services/begging-hands.jpg'

image = AdImage(parent_id=my_id)
image[AdImage.Field.filename] = image_path
image.remote_create()
print(image)
# Output image Hash
#print(image[AdImage.Field.hash])
#print(onlineimage)
image_id =  "196943804042546:96cb46d0d1eba007768d38308b03c057"

link_data = AdCreativeLinkData()
link_data[AdCreativeLinkData.Field.message] = '"Like" us and help give homeless people a helping hand'
link_data[AdCreativeLinkData.Field.link] = 'https://www.facebook.com/caltech.clickmaniac/'
link_data[AdCreativeLinkData.Field.caption] = 'https://www.facebook.com/caltech.clickmaniac/'
link_data[AdCreativeLinkData.Field.image_hash] = AdImage.Field.hash

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = my_page_id
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id=my_id)
creative[AdCreative.Field.name] = 'Helping Hand'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()
c = creative.remote_read()
my_creative_id = c["id"]
print(c)

print("creative id", my_creative_id)

# Create Facebook ad with Ad
ad = Ad(parent_id=my_id)
ad[Ad.Field.name] = "Helping Hand Ad"
ad[Ad.Field.adset_id] = my_adset_id
ad[Ad.Field.creative] = {
    'creative_id':my_creative_id,
}

# Activate ad
ad.remote_create(params={
    'status': Ad.Status.active,
})

print("activated adset")
'''
