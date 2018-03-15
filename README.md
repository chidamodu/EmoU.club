What's EmoU.club?
It's a travel companion that suggests enriched experiences to customers during their time of visit to a place of visit. For example: say, a customer is traveling to Stockholm from 15 September to 28 September. Suggesting 'must have' or 'not to be missed' experiences that will be happening during that time of their visit, is what EmoU.club is striving to achieve.

It might come across as bit too bold to claim that EmoU.club provides 'must have experiences', but there are reasons to justify its claim. 
	1. Scraping data off from blogs and websites, including the potential of interesting reviews/comments of community forums, that are done intentionally with unique perspective straight from experimental and explorative mindsets contributed to the opportunity of building an awesome dataset. Interracial couples' blogs, solo travelers' websites discussing their fun trips and challenges they had while travelling, and unique personal websites that explain gastronomical and transformational travel experiences that got them out of depression were some of the awe-inspiring sources of information where I pulled my data from.
	2. To sync details of thousands of live events that happen every day, I know, I have to link some real time data sources. But there are many such sites out there doing the same and so I didn't want to go that route. I went after annual traditional, cultural, and other local/regional events for which I was able to find details, approximately, re their dates of happenings. I made sure of consistency with regards to getting details of those events, in particular, live events. If at least, say, five legit websites mentioned that Mardi Gras happens annually during February - March in Sydney, then the logic is that it must be true. Also made sure to mention the happenings, mostly, during a range of period, meaning from March to April rather than mentioning an event that might or not happen exactly on 20th April every year unless very certain.
	3. Scraped data under three major categories: gastronomy, music, and cultural experiences. The cultural category also included traditional, significant with national or international appeal, regional, and local, and off-the-beat experiences that only locals know about. Example: the info about Taiwanese love for books and the bookstores that are open all day and night to cater to their craving for reading is a sample of off-the-beat experience I am talking about.
	
What's the motivation?
It doesn't shy away from following Bayesian principles, of course, i.e., having prior knowledge about some event or place will lead to a different posterior probability of happenings than not having that prior knowledge. If I do not know what I would have liked had I had some prior knowledge about some happenings or events or places to visit, how would I be able to translate that to a travel company or an agent? I experienced something similar myself when I travelled to Stockholm. While browsing personal travel blogs for my trip a word 'Fikka' popped up and one of the blogs read, "You need to have Fikka experience in the oldest part of the city if possible!" So I started searching to book a room near Fikka, but, after hours of research, figured out that Fikka is a Swedish experience to have a traditional cinnamon pastry with coffee and that Swedes take it very seriously. When I finally managed to have this experience at a generations old café in the oldest and historic part of the city, the Gamla Stan, it made my trip. But if I didn't know that I would have missed that experience. Even if I, say, book special experiences with a travel company, if Fikka is not listed on its website then I, very likely, would miss having that experience. And that's the motivation!

How does it achieve?
Workflow
Phase I:
Most often we come across huge blob of text hiding a treasure trove of information. Scouring the internet is a tough task and even worse is to maneuver through pages after pages to find about specific information. One solution is to extract important information out of the text. I decided to recognize necessary entities in the text and extract necessary information (relationship between different entities) using NLP (Natural Language Processing) techniques. My first choice was to turn to NLTK's techniques. I followed the standard procedure of tokenizing my scraped text and Parts-Of-Speech (POS) tagging using nltk.word_tokenize and nltk.pos_tag, except for removing the stop words and that I had done in Phase II. And that's all I used NLTK in my project.

Stop words in English from nltk.corpus
{'its', 'in', 'off', 'by', 'below', 'had', 'themselves', 'don', 'were', 'you', 'd', 'from', 'through', 'hers', 'at', 'theirs', 'under', 'some', 'wasn', 'him', 'has', 'ma', 'whom', 'this', 'those', 'once', 'each', 'not', 'we', 'how', 'doing', 'during', 'with', 'is', 'couldn', 'does', 'up', 'ain', 'their', 'won', 'an', 'shouldn', 'a', 'being', 're', 'any', 'about', 'are', 'who', 'out', 'having', 'as', 'only', 'can', 'other', 'and', 'on', 've', 'y', 'needn', 'didn', 'until', 'if', 'of', 'so', 'himself', 'no', 'ours', 'when', 'yours', 'to', 'than', 'most', 'while', 'between', 'mightn', 'my', 'where', 'all', 't', 'will', 'o', 'll', 'did', 'both', 'very', 'doesn', 'was', 'she', 'it', 'm', 'your', 'the', 'or', 'for', 'just', 'these', 'further', 'me', 'more', 'own', 'ourselves', 'down', 'haven', 'myself', 'been', 'wouldn', 'they', 'aren', 'yourselves', 'itself', 'then', 'again', 'hasn', 'because', 'hadn', 'but', 'isn', 'there', 'nor', 'yourself', 'before', 'am', 'our', 'what', 'why', 'weren', 'mustn', 'over', 'he', 'after', 'into', 'now', 'which', 'against', 'too', 'above', 'do', 'same', 'that', 'herself', 'have', 'shan', 'such', 'here', 'should', 'her', 'i', 'few', 'his', 'be', 's', 'them'}

Why I coded Hidden Markov Model using Viterbi algorithm myself?
Before explaining why I coded the above said algorithms myself, I have to explain what were the shortcomings I experienced with NLTK.

How does the workflow look like using NLTK?
Currently, if I have to depend on NLTK the workflow will look similar to the following:
	1. Parse the tagged words of text data
	2. Chunk a group of words to make sense according to the context of case in point
	3. One can either use a tagged corpus of NLTK and train and test their dataset by setting a grammar pattern on Parts-Of-Speech tags using REGEX (Regular Expressions) or train a classifier (nltk.MaxentClassifier) to group entities in a more meaningful way
	Example of a grammar pattern set on Parts-Of-Speech tags 
			NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
	4. To extract named entities out of text one can either pull out the chunked words in ways mentioned in 3rd point or use nltk.ne_chunk (named entity chunker) to get the output. A sample output looks like as follows:
			(S
  The/DT
  (GPE U.S./NNP)
  is/VBZ
  one/CD
  ...
  according/VBG
  to/TO
  (PERSON Brooke/NNP T./NNP Mossman/NNP)
  ...)
	The named entities in the above sample are GPE (Geo Political Entity) and PERSON. Although it seems like the nltk.ne_chunk has accurately identified the US as GPE and Brooke Mossman as PERSON, it's not the case in reality.
	5. If one has to extract the relationship, after extracting the entities, between different entities, nltk.sem.extract_rels might come in handy
	A sample output as follows:
			[ORG: 'McGlashan &AMP; Sarrail'] 'firm in' [LOC: 'San Mateo']
	The relationship is identified as 'firm in' between the two entities: ORG and LOC

Challenges
	1. NLTK's parser and chunkers offer easy solutions, but the underneath 'Tree' structure, used by NLTK, groups words differently by joining sentences , if need be, together and that makes traversing the tree structure difficult. 
	2. And the option of using the Maxent Classifier offered by NLTK didn't work as the algorithm is broken and not been updated recently.
	3. The idea of using NLTK's named entity chunker (nltk.ne_chunk ) wasn't satisfying as the chunker recognized an event 'Bronx Week' as PERSON and NLTK didn't offer an option to recognize events.

Now back to Hidden Markov Model/Viterbi Algorithm
I loved the idea of fitting a probabilistic model to my data and retrieving information by optimizing the sentence structures. The Hidden Markov Model calculates the probability of each Parts-Of-Speech tag occurring in a corpus and the Viterbi algorithm finds an optimum sentence by back propagating through the different options of Parts-Of-Speech tags for the same sentence.


