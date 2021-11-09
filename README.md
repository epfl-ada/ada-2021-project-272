{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***\n",
    "# Title: Origins of Opinions and Their Influences\n",
    "***"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Abstract:\n",
    "\n",
    "> In this project, we study the link between opinions, time and people. We would like to tell the story of how one’s speech is influenced by who they are, and how does that end up shaping their opinions versus external factors. However, if external factors are more influential, and if one’s opinion is just a derivative of what has already been said, then the question would instead be focused on finding the originator of that initial thought. Therefore, studying sentence structures and their content will help us study the possible origins of ideas and put to bed the age-old question of whether people could be placed in boxes. \n",
    "\n",
    "***\n",
    "\n",
    "## Research Questions:\n",
    "\n",
    "> 1.\t*Predicting people’s background from quotes:* The question we would like to answer here is how is speech influenced by a person’s age, gender, race and education level. All these aspects of a person's identity can manifest in a person's use of different vocabulary and style of speech. For instance, millennials are more likely to use certain phrases that baby boomers might not understand. While a millennial might describe a party as being \"lit\", the boomer would refer to it as being \"loaded.\" Furthermore, people of different ethnicities are more likely to incorporate words or sentence structures from their ethnic language while speaking English.\n",
    "\n",
    "> 2.\t*Tracking the change in individual’s opinions on certain topics:* Given a subject, an individual might start with a certain opinion, and might end up with a completely different one. This is not an uncommon phenomenon, since with time we learn and gain insight about certain topics. However, some people’s sudden change of opinion might not be so honorable. Thus, how can we use data analysis to understand people’s shifts in beliefs.  \n",
    "\n",
    "> 3.\t*Checking whether sub-groups have similar opinions:* The question here is whether people with similar profiles have similar views. Do all gen Z’s believe in the grave issue of global warming, while gen X’s think it is a hoax? More educated people will more likely form a well thought threw opinion on certain topics, and will less likely be influenced by fear.\n",
    "\n",
    "> 4.\t*Tracing back the originator of an idea/opinion:* There exists a hypothesis on how no idea is original. All individual ideas are just a reiteration of some initial idea. To test this theory, we would like to trace back the spread of an idea through quotes, to find out who was the first person to utter it.\n",
    "\n",
    "***\n",
    "\n",
    "## Additional Datasets:\n",
    "> -\tWikidata: Since we are studying the link between quotes and speakers’ profile, we intend to use Wikidata that will provide us with such information. It will be used to answer the first research question.\n",
    "\n",
    "> -\tTwitter data: To track people’s change in opinions, we would require a series of quotes from each individual. In cases when the quotebank does not have enough quotes by a certain individual, we can enrich our dataset by using tweets. \n",
    "\n",
    "***\n",
    "\n",
    "## Methods:\n",
    "\n",
    "> 1.\tTo answer the first research question, we would train a recurrent neural network (RNN) with the quotes and the corresponding speaker as input. The output would be a vector with the following attributes: generation (gen Z/millennial/gen X/baby boomer), gender (female/male), race (White/African/Asian/Latino/Other), education (non/high school/undergrad/graduate). The network should be able to predict the speaker’s profile from a quote. \n",
    "\n",
    "> 2.\tTo track change in opinions, we first focus on a list of topics: American presidential elections, global warming, human rights. We then apply some opinion mining techniques to figure out people’s opinions on these topics: whether they are positive, negative, or neutral. \n",
    "\n",
    "> 3.\tTo check whether people with similar backgrounds tend to have the same opinions, we cluster the different speakers into different sub-groups and check the distribution of opinions on the aforementioned topics. If we see the distribution is centered, then we can conclude that sub-groups tend to have similar views. \n",
    "\n",
    "> 4.\t\n",
    "\n",
    "***\n",
    "\n",
    "## Timeline:\n",
    "\n",
    ">1.\tWeek 1:\n",
    "    -\tPreprocess the data:\n",
    "        -\tRemove samples with missing unknown authors.\n",
    "        -\tRemove duplicate quotes. \n",
    "        -\tCombine authors with different names under one name, e.g., Donald Trump and President Donald Trump.\n",
    "    -\tPrepare the data for the RNN: \n",
    "        -\tExtract the output vectors from the Wikidata. \n",
    "        -\tMap the categorical vector into the Euclidean space.\n",
    "    -\tPrepare the data for opinion mining:\n",
    "        -\t Split quotes into the three specified topics, and disregard those that deal with different topics.  \n",
    "    -\tExtract extra quotes from the Twitter data.\n",
    "> 2.\tWeek 2: \n",
    "    -\tTrain the RNN. \n",
    "    -\tRun opinion mining on the selected quotes. \n",
    "    -\tStudy how individual opinion has changed over time. \n",
    "    -\tCluster speakers into sub-groups and study distributions of the opinions in each sub-group. \n",
    ">3.\tWeek 3:  \n",
    "    -\t\n",
    "> 4.\tWeek 4: \n",
    "\n",
    "\n",
    "***\n",
    "\n",
    "## Team Organization: \n",
    "\n",
    "> 1.\tAntoine\n",
    "> 2.\tElsa\n",
    "> 3.\tNatalya\n",
    "> 4.\tTikhon\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
