import cohere
import pandas as pd
import re
import string

# read in the data
df = pd.read_excel('BookQuotes.xlsx')

co = cohere.Client('25jaWHrlyPTir6DppLZWPNEyTRo0Id02EIMG20tt')

# create hashtags for book quotes
tags = []
for quote in df['Text']:

    initial_prompt = 'Post: Why are there no country songs about software engineering\nHashtag: #softwareengineering\n--\nPost: Your soulmate is in the WeWork you decided not to go to\nHashtag: #wework\n--\nPost: If shes talking to you once a day im sorry bro thats not flirting that standup\nHashtag: #standup\n--'
    prompt = initial_prompt + '\nPost: ' + quote + '\nHashtag:'

    response = co.generate(
    model='large',
    prompt=prompt,
    max_tokens=10,
    temperature=0.5,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=["--"],
    return_likelihoods='NONE')
    #print('Prediction: {}'.format(response.generations[0].text))

    tag = response.generations[0].text
    tag = tag.strip('\n--')
    tags.append(tag)


df['Tags'] = tags
print(df.head())

# save to a file
df.to_csv('BookTags.csv')

