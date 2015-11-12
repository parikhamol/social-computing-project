import re

def get_liwc_lexicons(filename):
	liwc_lexicons_directory = "resources/liwc_lexicons"
	lexicon = []
	lexicon_str = "("
	with open("{0}/{1}".format(liwc_lexicons_directory, filename), "r") as file_handle:
		for line in file_handle:
			lexicon_item = line.strip()
			if "*" in lexicon_item:
				lexicon_item = r"\b{0}\b".format(lexicon_item.replace("*", ".*?"))
			else:
				lexicon_item = r"\b{0}\b".format(lexicon_item)
			lexicon_str += lexicon_item + "|"
	lexicon_str = lexicon_str[:-1] + ")"
	lexicon.append(lexicon_str)
	return lexicon

def extract_liwc_features():
	#initialize the liwc dict and read the lexicon files using the function above (needs to be done once)
	liwc_lexicons = {}
	liwc_lexicons["positive_affect"] = get_liwc_lexicons("positive_affect")
	liwc_lexicons["negative_affect"] = get_liwc_lexicons("negative_affect")

	liwc_lexicons["anger"] = get_liwc_lexicons("anger")
	liwc_lexicons["anxiety"] = get_liwc_lexicons("anxiety")
	liwc_lexicons["preposition"] = get_liwc_lexicons("preposition")
	liwc_lexicons["article"] = get_liwc_lexicons("article")

	liwc_lexicons["pronoun"] = get_liwc_lexicons("pronoun")
	liwc_lexicons["discrepancies"] = get_liwc_lexicons("discrepancies")
	liwc_lexicons["inhibition"] = get_liwc_lexicons("inhibition")
	liwc_lexicons["negation"] = get_liwc_lexicons("negation")
	liwc_lexicons["death"] = get_liwc_lexicons("death")
	liwc_lexicons["causation"] = get_liwc_lexicons("causation")
	liwc_lexicons["certainty"] = get_liwc_lexicons("certainty")
	liwc_lexicons["tentativeness"] = get_liwc_lexicons("tentativeness")

	liwc_lexicons["see"] = get_liwc_lexicons("see")
	liwc_lexicons["hear"] = get_liwc_lexicons("hear")
	liwc_lexicons["feel"] = get_liwc_lexicons("feel")
	liwc_lexicons["percept"] = get_liwc_lexicons("percept")
	liwc_lexicons["insight"] = get_liwc_lexicons("insight")
	liwc_lexicons["relative"] = get_liwc_lexicons("relative")

	liwc_lexicons["verbs"] = get_liwc_lexicons("verbs")
	liwc_lexicons["auxiliary_verbs"] = get_liwc_lexicons("auxiliary_verbs")
	liwc_lexicons["adverbs"] = get_liwc_lexicons("adverbs")

	liwc_lexicons["past_tense"] = get_liwc_lexicons("past_tense")
	liwc_lexicons["present_tense"] = get_liwc_lexicons("present_tense")
	liwc_lexicons["future_tense"] = get_liwc_lexicons("future_tense")

	liwc_lexicons["conjunction"] = get_liwc_lexicons("conjunction")
	liwc_lexicons["friends"] = get_liwc_lexicons("friends")
	liwc_lexicons["social"] = get_liwc_lexicons("social")
	liwc_lexicons["work"] = get_liwc_lexicons("work")
	liwc_lexicons["health"] = get_liwc_lexicons("health")
	liwc_lexicons["humans"] = get_liwc_lexicons("humans")
	liwc_lexicons["religion"] = get_liwc_lexicons("religion")
	liwc_lexicons["bio"] = get_liwc_lexicons("bio")
	liwc_lexicons["body"] = get_liwc_lexicons("body")
	liwc_lexicons["money"] = get_liwc_lexicons("money")
	liwc_lexicons["achievement"] = get_liwc_lexicons("achievement")
	liwc_lexicons["home"] = get_liwc_lexicons("home")
	liwc_lexicons["sadness"] = get_liwc_lexicons("sadness")

	liwc_lexicons["first_person_singular"] = get_liwc_lexicons("first_person_singular")
	liwc_lexicons["first_person_plural"] = get_liwc_lexicons("first_person_plural")
	liwc_lexicons["second_person"] = get_liwc_lexicons("second_person")
	liwc_lexicons["third_person"] = get_liwc_lexicons("third_person")

	return liwc_lexicons

	'''
	#for testing
	sample_author_id = "test"
	sample_content_text = "Anyone else have a sore throat and drainage AFTER you quit smoking? I'm still feeling pretty agitated all the time, but I do not think of smoking nearly as often. My anxiety is also high, as I think of how much I never want to be a smoker again. Allen Carr's book is helping-but I get pissed every time he writes it is easy."


	author_id_to_liwc_lexicon_to_count = {}		#this dict keeps the author-specific counts for each LIWC lexicon
	
	#this block initializes the dict above for each author (to make things simpler afterwards)
	'''

def getLex(post, liwc_lexicons):
	liwc_lexicon_to_count = {}
	for liwc_lexicon_name in set(liwc_lexicons.keys()):
		liwc_lexicon_to_count[liwc_lexicon_name] = 0

	#this block examines some text (here: sample_content_text) and updates the LIWC counts using regular expressions
	for liwc_lexicon_name, liwc_lexicon_items in liwc_lexicons.iteritems():
		for liwc_lexicon_item in liwc_lexicon_items:
			pattern = re.compile(liwc_lexicon_item)
			count = len(pattern.findall(post))
			liwc_lexicon_to_count[liwc_lexicon_name] += count
	return liwc_lexicon_to_count

	'''
	#for testing
	for author_id, liwc_lexicon_to_count in author_id_to_liwc_lexicon_to_count.iteritems():
		for liwc_lexicon, count in liwc_lexicon_to_count.iteritems():
			print("author: {0}, liwc lexicon: {1}, count: {2}".format(author_id, liwc_lexicon, count))
	'''


# if __name__ == "__main__":
#	extract_liwc_features()
