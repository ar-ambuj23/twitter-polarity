## Inspiration
In recent years, Twitter has become increasingly popular among researchers, students, politicians, media, and the general public, making it a platform where information is circulated quickly. As making a tweet or re-tweeting it is free and uncomplicated, Twitter has become prone to spread false or biased information quickly. Thus, to solve this problem, we propose to add a feature to Twitter that can visually aid a user, for any hashtag, with the chances of it having false or biased information. For this purpose, we have built a web application that demonstrates our prototype.

## What it does
There are two primary features of our application.
- **Polarity graphs for trending hashtags on the home page**

When the user logs in to Twitter, they will be able to see polairty graphs for all the trending hashtags besides them which can guide the user about the biasness of the hashtag.

- **Sentiment Trend for a particular hashtag searched by user**

When the user searches for a particular hashtag or clicks on the Polarity graph of one of the trending hashtags, they would be shown the sentiment analysis for that hashtag with positive, negative and neutral tweets for that hashtag, in a visual manner. This gives a simple and detailed view of the polarity of the hashtag. 

## Demo Video
Please click [here](https://youtu.be/vd3dEeNv5so) to watch the demo.

## How we built it
- To get the information about the journey of a hashtag since its origin (7-days for this prototype), we collect the data of all tweets with this hashtag and calculate the sentiment scores for each tweet on a daily basis using the NLTK library. 
- We used the Twitter Standard API to collect the data. 
- The backend is hosted on Flask using Python which communicates with the frontend, built with Vue.js.


## Challenges we ran into
- **Limited data** We had access to the Twitter Standard API which allowed us to get data only for the last 7 days. Ideally, this would be scaled for all the data since a hashtag is originated.
- **Slow Response** Again, due to the limitations of the Twitter Standard API, the response time of the API is slow.

## Accomplishments that we're proud of
- We are proud that we worked on this project as a team and could make a working prototype.
- We are also proud of the fact that we address a very pressing concern, and are trying to make Twitter a safe space for everyone.

## What we learned
- We learned the usage of Twitter API and Tweepy in an efficient way.
- We learned that it is not difficult to work with strangers when you do have a common goal. We turned out to be a good team in the end.
- We also learned about Flask, Vue.js and sentiment analysis using the NLTK library.

## What's next for twitter-polarity
- By using premium version of the Twitter API, all the tweets can be collected for a hashtag since its origin.
- The response time can also be reduced by using premium version of the API.
- The sentiment analysis can be improved by including different languages and emojis, and not just English.
- We can have more interactive visualizations for a hashtag to study its behavior over time.
