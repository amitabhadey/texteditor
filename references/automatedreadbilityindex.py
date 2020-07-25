import textstat
#import readtime


test_data = "Hello world. Welcome to my home!"

print ("Flesch Reading Ease : " + str (textstat.flesch_reading_ease(test_data)))
print ("Smog Index : " + str (textstat.smog_index(test_data)))
print ("Flesch Kincaid Grade : " + str (textstat.flesch_kincaid_grade(test_data)))
print ("Coleman Liau Index : " + str(textstat.coleman_liau_index(test_data)))
print ("Automated Readibility Index : " + str(textstat.automated_readability_index(test_data)))
print ("Dale Chall Readability Score : " + str(textstat.dale_chall_readability_score(test_data)))
print ("Difficult Words : " + str(textstat.difficult_words(test_data)))
print ("Linsear Write Formula : " + str(textstat.linsear_write_formula(test_data)))
print ("Gunning Fog : " + str(textstat.gunning_fog(test_data)))
print ("Text Stamdard : " + str(textstat.text_standard(test_data)))

res = len(test_data.split())
print ("Word Count : " + str(res))









"""
Average reading speed of an adult - roughly 256 words per minute


256 words can be read in 60 seconds

1 word can be read in (60/256) seconds

n words can be read in (60/256) * n seconds




"""




















#neuro_reading_time = readtime.of_text (test_data)
#print ("Reading Time : " + str(neuro_reading_time.text))





#textstat.syllable_count(text)
#Returns the number of syllables present in the given text.

#textstat.lexicon_count(text, removepunct=True)
#Calculates the number of words present in the text. Optional removepunct specifies whether we need to take punctuation symbols into account while counting lexicons. Default value is True, which removes the punctuation before counting lexicon items.

#textstat.sentence_count(text)
#Returns the number of sentences present in the given text.

#textstat.flesch_reading_ease(text)
#Returns the Flesch Reading Ease Score.




#The following table can be helpful to assess the ease of readability in a document.
#The table is an example of values. While the maximum score is 121.22, there is no limit on how low the score can be. A negative score is valid.

"""

Score   Difficulty
90-100  Very Easy
80-89   Easy
70-79   Fairly Easy
60-69   Standard
50-59   Fairly Difficult
30-49   Difficult
0-29    Very Confusing

"""

#The Flesch-Kincaid Grade Level
#Returns the Flesch-Kincaid Grade of the given text. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.


#The Fog Scale (Gunning FOG Formula)
#Returns the FOG index of the given text. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.


#The SMOG Index
#Returns the SMOG index of the given text. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.
#Texts of fewer than 30 sentences are statistically invalid, because the SMOG formula was normed on 30-sentence samples. textstat requires at least 3 sentences for a result.


#Automated Readability Index
#Returns the ARI (Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text.
#For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade


#The Coleman-Liau Index
#Returns the grade level of the text using the Coleman-Liau Formula. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.

#Linsear Write Formula
#Returns the grade level using the Linsear Write Formula. This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.

#Dale-Chall Readability Score
#Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula.


"""
Score   Understood by
4.9 or lower    average 4th-grade student or lower
5.0–5.9 average 5th or 6th-grade student
6.0–6.9 average 7th or 8th-grade student
7.0–7.9 average 9th or 10th-grade student
8.0–8.9 average 11th or 12th-grade student
9.0–9.9 average 13th to 15th-grade (college) student

"""


#Readability Consensus based upon all the above tests
#Based upon all the above tests, returns the estimated school grade level required to understand the text.


"""
Documentation:
https://pypi.org/project/textstat/

"""



"""
Readability Index in Python(NLP)? - Tutorials Point
https://www.tutorialspoint.com/readability-index-in-python-nlp
"""

"""

Readability Index in Python(NLP) - Geeks for Geeks
https://www.geeksforgeeks.org/readability-index-pythonnlp/

"""

"""
py-readability-metrics
https://py-readability-metrics.readthedocs.io/en/latest/

"""

"""
Hemmingway Help
http://www.hemingwayapp.com/help.html

"""
