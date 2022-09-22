import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# import the data with hashtags
df = pd.read_csv('BookTags.csv')


# create a bar graph of the five most common hashtags from the quotes
df['Tags'].value_counts()[0:5].plot(kind='bar', figsize = (10,10))
plt.xlabel('Hashtag')
plt.ylabel("Frequency")
plt.title("Most Frequent Hashtags")
plt.savefig('TopFiveTags.png')


# create word clouds of the hashtags from each book
for book in set(df['Book']):

    book_df = df[df['Book'] == book]
    all_tags = (" ").join(book_df['Tags'])

    wordcloud = WordCloud(width = 1000, height = 500).generate(all_tags)
    plt.figure(figsize=(15,8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(book.replace(" ", "")+"Tags.png", bbox_inches='tight')

        

