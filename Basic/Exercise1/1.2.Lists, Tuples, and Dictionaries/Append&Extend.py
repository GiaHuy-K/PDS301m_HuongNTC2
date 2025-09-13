# When we used .append above, each time we append one item, which we saw was often a list. What if we
# wanted to simply combine two lists into one longer one? That's what .extend does, or its equivalent, adding
# lists together with a + operator which is really simpler so we'll use that:
Pacific = ['AK','CA','OR','WA']
Desert = ['AZ','NV','UT']
Mountain = ['ID','MT','WY','CO','NM']
WestStates = Pacific + Desert + Mountain
print(WestStates)

States = Pacific
States.append(Desert)  
print(States) 
States.extend(Mountain)
print(States)
