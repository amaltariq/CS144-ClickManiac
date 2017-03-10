from facebookads.api import FacebookAdsApi
from facebookads import objects
from facebookads.objects import AdSet
from facebookads.adobjects.targetingsearch import TargetingSearch 
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebookads.adobjects.ad import Ad
import datetime

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
params_charity = {              # Interest: charity
    'q': 'charity',
    'type': 'adinterest'
}
params_commissues = {           # Interest: Community issues 
    'q': 'Community issues',
    'type': 'adinterest'
}
params_volunteering = {         # Interest: Volunteering
    'q': 'Volunteering',
    'type': 'adinterest'
}

params_nonprofitorg = {         # Interest: Nonprofit organizations
    'q': 'Nonprofit organization',
    'type': 'adinterest'
}

params_animal = {               # Interest: Animals
    'q': 'animals',
    'type': 'adinterest'
}
params_disneychannel = {        # Interest: Disney Channel
    'q': 'Disney Channel',
    'type': 'adinterest'
}
params_disneyprincess = {       # Interest: Disney Princesses
    'q': 'Disney Princess',
    'type': 'adinterest'
}
params_frozenmovie = {          # Interest: Frozen Movie
    'q': 'Frozen (2013 film)',
    'type': 'adinterest'
}
params_frozenfranchise = {      # Interest: Frozen Franchise
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

# Specify Targeting
targeting = {
    # Specify radius of 12 miles around New Delhi
    'geo_locations': {
        'cities' : [{'key':'1037239', 'radius':12, 'distance_unit':'mile'}]
        # The custom locations code below should have worked since it was 
        #   identical to the documentation code, but, when used as the only
        #   location specification, it returns an error code 100, subcode
        #   1487851, with title "Incorrect Location Format" and message
        #   "Before you can place your order you need to enter a valid
        #   location in the targeting section so you can reach people near
        #   your business"
        # 'custom_locations': [
        #     {
        #         'latitude': 77.209, 
        #         'longitude': 22.6267,
        #         'radius': 50,
        #         'distance_unit': 'mile',
        #     },
        # ],
    },
    'age_min': 13,
    'age_max': 25,
    'genders': 2,           # Specify female gender

    # Target demographic behavior
    'flexible_spec': [      
      {
        # Target audience should be interested in one of the following
        'interests': [
            {'id': int_charity[0]['id'], 'name': int_charity[0]['name']},
            {'id': int_commissues[0]['id'], 'name': int_commissues[0]['name']},
            {'id': int_volunteering[0]['id'], 'name': int_volunteering[0]['name']},
            {'id': int_nonprofitorg[0]['id'], 'name': int_nonprofitorg[0]['name']},
            {'id': int_disneychannel[0]['id'], 'name': int_disneychannel[0]['name']},
            {'id': int_disneychannel[1]['id'], 'name': int_disneychannel[1]['name']},   # Disney Channel International
            {'id': int_disneychannel[6]['id'], 'name': int_disneychannel[6]['name']},   # Disney Channel Asia
            {'id': int_disneyprincess[0]['id'], 'name': int_disneyprincess[0]['name']},
            {'id': int_frozenmovie[0]['id'], 'name': int_frozenmovie[0]['name']},
            {'id': int_frozenfranchise[0]['id'], 'name': int_frozenfranchise[0]['name']},],
        
        # Or they must be friend of someone who has already liked the page
        'friends_of_connections': [
            {'id':103185246428488},],
      },
    ],
    # This code also returned an error (even though it was taken straight
    #   from the documentation and used with our Ideas Behind the Web page ID)
    #   The erro code was 100, subcode 1885097, title "Type Mismatch," and
    #   message "The type string is expected but a type integer was received
    #   with value 0." The same error occurred whether the ID was input as a
    #   string or integer. When this code was commented out, there was no
    #   error.
    # Exclude people who've already liked the page
    # 'exclusions': [
    #   {
    #     'connections': [{'id':'103185246428488'},],
    #   },
    # ],
    
}

# Code to retrieve the campaign ID: 
# campaign = Campaign(campaign_id)
# campaign.remote_read(fields=[Campaign.Field.name, Campaign.Field.objective,])
# print(campaign)

# Create the Adset
adset = AdSet(parent_id=my_id)
campaign_id = '23842548820110548'

# We attempted to set a time at which our ads would be broadcast, but this 
#   required a lifetime budget rather than a daily budget.
'''
    # Attempt 1:
    AdSet.Field.pacing_type: ['day_parting'],
    AdSet.Field.adset_schedule: {
        'start_minute': 60,
        'end_minute': 540,
        'days': [0, 1, 2, 3, 4, 5, 6],
    }

    # Attempt 2:
    AdSet.Field.start_time: str(datetime.datetime(year=2017, month=3, day=6, hour=1, minute=36)),
    AdSet.Field.end_time: str(datetime.datetime(year=2017, month=3, day=6, hour=6, minute=0)),
'''

# Update the Adset
my_page_id = '103185246428488'      # Ideas Behind the Web page ID
adset.update({
    AdSet.Field.name: 'Adset Name',
    AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
    AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
    AdSet.Field.daily_budget: 200,
    AdSet.Field.promoted_object: {
        'page_id': my_page_id,
    },
    AdSet.Field.campaign_id: campaign_id,
    AdSet.Field.targeting: targeting,
    AdSet.Field.is_autobid: True,
})

# Remotely create the adset
adset.remote_create(params={
    'status': AdSet.Status.active,
})
print("Remotely created the adset")

#### Creating the Ads ########################################################
# The code below was our attempt at creating ads, however, we encountered the
#   error with code 100, subcode 144305, title "Error Loading Image," and
#   message "The ad image could not be loaded". We checked our code for
#   uploading an ad image with two other groups who were able to successfully
#   upload an ad and it was the same. So we were unable to find a solution to
#   this problem.

'''
# Remote read the adset
a = adset.remote_read(fields=[AdSet.Field.id])
# my_adset_id = a["id"]
my_adset_id = "23842548820110548"
print("my adset id", my_adset_id)
# Should be: "23842548820110548"?

### AD CREATIVE SECTION
account = AdAccount(my_id)
images = account.get_ad_images()
#print(images)

image_path = './clickmaniac-ads/homeless_services/begging-hands.jpg'

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
