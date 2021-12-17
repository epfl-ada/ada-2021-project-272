
# Title: Origins of Opinions and Their Influences
[data story](https://antebachmann.github.io/Emotiolitics/)



## Abstract:

> In this project, we study the link between opinions, time and people. We would like to tell the story of how one’s speech is influenced by who they are, and how does that end up shaping their opinions versus external factors. However, if external factors are more influential, and if one’s opinion is just a derivative of what has already been said, then the question would instead be focused on finding the originator of that initial thought. Therefore, studying sentence structures and their content will help us study the possible origins of ideas and put to bed the age-old question of whether people could be placed in boxes.

> In fact we have worked on the emotionality of politics relative to time and social groups.

## Research Questions:

> 1.	*Is emotionality predicated on social group*

> 2.	*Does discourse change over time*  



## Additional Datasets:
> -	Wikidata: Since we are studying the link between quotes and speakers’ profile, we intend to use Wikidata that will provide us with such information. It will be used to answer the first research question.

## Structure of the project
The project can be split into three main steps
1. **Extracting data from the Quotebank and wikidata.** Code we used for this is in the notebook *Preprocessing*. And files that were extracted are in the */data* folder.
2. **Sentimental analysis.** For this purpose we used a *Sentiment analysis* notebook.
3. **Analysis.** We did three different analyses (over the data, years and speakers) and used three different notebooks for it respectively (*Comparing issues*, *Comparing epoch*, *Comparing people*).


## Timeline:

>1.	Week 1:
>    * Preprocess the data:
>         * Remove samples with missing unknown authors.
>         * Remove duplicate quotes.
>         *	Combine authors with different names under one name, e.g., Donald Trump and President Donald Trump.
>    * Prepare the data for the RNN:
>         *	Extract the output vectors from the Wikidata.
>         *	Map the categorical vector into the Euclidean space.
>    * Prepare the data for opinion mining:
>         *	Split quotes into the three specified topics, and disregard those that deal with different topics.  
>    *	Extract extra quotes from the Twitter data.
>2.	Week 2:
>    *	Train the RNN.
>    *	Run opinion mining on the selected quotes.
>    *	Study how individual opinions have changed over time.
>3.	Week 3:  
>    *	Cluster speakers into sub-groups and study distributions of the opinions in each sub-group.
>    *	Study origins of some catch phrases.
>4.	Week 4:
>    *   Trace back first appearance of catch phrase.
>    *   Check similar quotes on same subject by each speaker.



## Team Organization:

> 1.	Antoine: prepare data for opinion mining. Run opinion mining on quotes. Trace original catch phrase.
> 2.	Elsa: Prepare data for RNN. Train RNN. Organize the data story.
> 3.	Nataliya: Preprocess the data. Run clustering algorithm. Check similar quotes to the catch phrase.
> 3.	Nataliya: Preprocess the data. Run clustering algorithm. Check similar quotes to the catch phrase.
> 4.	Tikhon: Extract twitter quotes. Study evolution of opinions. Organize the data story.

