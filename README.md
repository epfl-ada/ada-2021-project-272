
# Title: Origins of Opinions and Their Influences


## Abstract:

> In this project, we study the link between opinions, time and people. We would like to tell the story of how one’s speech is influenced by who they are, and how does that end up shaping their opinions versus external factors. However, if external factors are more influential, and if one’s opinion is just a derivative of what has already been said, then the question would instead be focused on finding the originator of that initial thought. Therefore, studying sentence structures and their content will help us study the possible origins of ideas and put to bed the age-old question of whether people could be placed in boxes. 



## Research Questions:

> 1.	*Predicting people’s background from quotes:* The question we would like to answer here is how is speech influenced by a person’s age, gender, race and education level. All these aspects of a person's identity can manifest in a person's use of different vocabulary and style of speech. For instance, millennials are more likely to use certain phrases that baby boomers might not understand. While a millennial might describe a party as being "lit", the boomer would refer to it as being "loaded." Furthermore, people of different ethnicities are more likely to incorporate words or sentence structures from their ethnic language while speaking English.

> 2.	*Tracking the change in individual’s opinions on certain topics:* Given a subject, an individual might start with a certain opinion, and might end up with a completely different one. This is not an uncommon phenomenon, since with time we learn and gain insight about certain topics. However, some people’s sudden change of opinion might not be so honorable. Thus, how can we use data analysis to understand people’s shifts in beliefs.  

> 3.	*Checking whether sub-groups have similar opinions:* The question here is whether people with similar profiles have similar views. Do all gen Z’s believe in the grave issue of global warming, while gen X’s think it is a hoax? More educated people will more likely form a well thought threw opinion on certain topics, and will less likely be influenced by fear.

> 4.	*Tracing back the originator of an idea/opinion:* There exists a hypothesis on how no idea is original. All individual ideas are just a reiteration of some initial idea. To test this theory, we would like to trace back the spread of an idea through quotes, to find out who was the first person to utter it.



## Additional Datasets:
> -	Wikidata: Since we are studying the link between quotes and speakers’ profile, we intend to use Wikidata that will provide us with such information. It will be used to answer the first research question.

> -	Twitter data: To track people’s change in opinions, we would require a series of quotes from each individual. In cases when the quotebank does not have enough quotes by a certain individual, we can enrich our dataset by using tweets. 



## Methods:

> 1.	To answer the first research question, we would train a recurrent neural network (RNN) with the quotes and the corresponding speaker as input. The output would be a vector with the following attributes: generation (gen Z/millennial/gen X/baby boomer), gender (female/male), race (White/African/Asian/Latino/Other), education (non/high school/undergrad/graduate). The network should be able to predict the speaker’s profile from a quote. 

> 2.	To track change in opinions, we first focus on a list of topics: American presidential elections, global warming, human rights. We then apply some opinion mining techniques to figure out people’s opinions on these topics: whether they are positive, negative, or neutral. We could use BERT model to 

> 3.	To check whether people with similar backgrounds tend to have the same opinions, we cluster the different speakers into different sub-groups and check the distribution of opinions on the aforementioned topics. If we see the distribution is centered, then we can conclude that sub-groups tend to have similar views. 

> 4.	To study the origin of an idea based on how it was said, i.e., some catch phrase, we could look back in time to the first person who ever used said catch phrase. To verify that person is the true originator, we would compare the idea implied in the phrase with other quotes. For example, to trace back that Trump was the originator of the phrase "build a wall", we would need to verify that not only was he the first person to say it, but also he was actively promoting the idea of building a wall in his speeches. 



## Timeline:

>1.	Week 1:
>      1. Preprocess the data:
>       *      Remove samples with missing unknown authors.
>       *      Remove duplicate quotes. 
>       *	     Combine authors with different names under one name, e.g., Donald Trump and President Donald Trump.
>      2. Prepare the data for the RNN: 
>        *	    Extract the output vectors from the Wikidata. 
>        *	    Map the categorical vector into the Euclidean space.
>      3. Prepare the data for opinion mining:
>        *	    Split quotes into the three specified topics, and disregard those that deal with different topics.  
>    4. 	Extract extra quotes from the Twitter data.
> 2.	Week 2: 
>    *	Train the RNN. 
>    *	Run opinion mining on the selected quotes. 
>    *	Study how individual opinions have changed over time. 
>3.	Week 3:  
>    *	Cluster speakers into sub-groups and study distributions of the opinions in each sub-group. 
>    *	Study origins of some catch phrases.
>4.	Week 4: 
 >   *   Trace back first appearance of catch phrase.
 >   *   Check similar quotes on same subject by each speaker.



## Team Organization: 

> 1.	Antoine: prepare data for opinion mining. Run opinion mining on quotes. Trace original catch phrase.
> 2.	Elsa: Prepare data for RNN. Train RNN. Organize the data story.
> 3.	Nataliya: Preprocess the data. Run clustering algorithm. Check similar quotes to the catch phrase.
> 3.	Nataliya: Preprocess the data. Run clustering algorithm. Check similar quotes to the catch phrase.
> 4.	Tikhon: Extract twitter quotes. Study evolution of opinions. Organize the data story.

## Questions for TAs:
> We are not sure whether all the ideas we have are too much. Instead of working on the four ideas, should we instead focus our project on maybe two of them? Or are the four ideas together feasible for one project?

