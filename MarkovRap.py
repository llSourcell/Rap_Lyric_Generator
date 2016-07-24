import random, re

def addToLib(fileName, currLib):
	f = open(fileName, 'r')
	words = re.sub("\n", " \n ", f.read()).split(' ')
	curr = 0

	while curr < len(words) - 1:
	#looping through all words including \n in this song
		currWord = words[curr].lower()
		nextWord = words[curr + 1].lower()
		if currWord in currLib.keys():
			#if we've seen this word anytime before
			if nextWord in currLib[currWord].keys():
				#if we've seen the sequence currWord -> nextWord before
				currLib[currWord][nextWord] += 1
			else:
				#haven't seen sequence currWord -> nextWord before
				currLib[currWord][nextWord] = 1
		else:
			#haven't seen this word before
			currLib[currWord] = {nextWord: 1}
		curr += 1

	#change counts to percentages
	for key in currLib.keys():
		#for each word
		keyTotal = 0
		for probKey in currLib[key].keys():
			keyTotal += currLib[key][probKey]
		for probKey in currLib[key].keys():
			currLib[key][probKey] = currLib[key][probKey]/keyTotal
	return currLib

def markov_next(currword, probDict):
	if currword not in probDict.keys():
		return random.choice(probDict.keys())
	else: 
		wordprobs = probDict[currword]
		randProb = random.uniform(0.0, 1.0)
		currProb = 0.0
		for key in wordprobs:
			currProb += wordprobs[key]
			if randProb <= currProb:
				return key
		return random.choice(probDict.keys())

def makeRap(startword, probDict):
	rap, curr, wc = '', startword, 0
	while wc < 50:
		rap += curr + ' '
		curr = markov_next(curr, probDict)
		wc += 1
	return rap

def testMarkov(startword):
	rapLib = {}
	addToLib('allLyrics.txt', rapLib)
	return makeRap(startword, rapLib)

startWord = raw_input("What do you want to start your rap with?\n")

print testMarkov('\nAlright, here\'s your rap: \n' + testMarkov(startWord))