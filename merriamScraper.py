#Luke De Vos


'''
Scrapes Merriam Webster's Online Dictionary (collegiate) for a requested word's (or text file of words) syllable structure and first listed pronunciation. If a word's first listed pronunciation depends on its part of speech, a line for each pronunciation and associated part of speech will be returned.
'''

import sys
import re
import urllib.request

def findSylls(raw):
	try:
		sylPattern = "\"word-syllables\">.*?<"
		sylMatch = re.findall(sylPattern, raw)
		sylMatch = re.findall(">.+?<", sylMatch[0])
		sylMatch = re.sub("·&#8203", "", sylMatch[0][1:-1])
		return sylMatch
	except:
		return "n/a"

def findPhos(raw):
	try:
		phoPattern = "span class=\"pr\">.+?</"
		phoMatch = re.findall(phoPattern, raw)[0]
		phoMatch = re.findall(">.+?<", phoMatch)[0]
		phoMatch = phoMatch[2:-1]
		return phoMatch
	except:
		return "n/a"

def findPartOfSpeech(raw):
	try:
		posPattern = "<a class=\"important-blue-link\" href=\"/dictionary/.+?\">.+?</a>"
		partMatch = re.search(posPattern, raw).group(0)
		partMatch = partMatch[49:] #trim leading characters
		partMatch = re.search(".+?\"", partMatch).group(0)
		partMatch = partMatch[0:-1] #trim trailing quote
		return partMatch
	except:
		return "n/a"
	

'''
#MAIN ===============================================================
'''

#requested word(s)
requestL=[]
if sys.argv[1][-4:] == '.txt':
	try:
		with open(sys.argv[1]) as file:
			for line in file:
				requestL.append(line[:-1]) 
	except:
		print("File not found")
		exit()
else:
	requestL = [sys.argv[1].lower()]

#
for request in requestL:
	wordForURL = re.sub(' ','%20', request)
	wordForURL = re.sub('\'','%27', wordForURL)
	try:
		fp = urllib.request.urlopen("https://www.merriam-webster.com/dictionary/" + wordForURL)
	except:
		print('\''+ request + '\' INVALID URL')
		continue

	#extract html
	mybytes = fp.read()
	htmlText = mybytes.decode("utf8")
	fp.close()

	#split all htmlText by 'hword' 
	#for each resulting text block, take first pr and word-syllables
	htmlText = htmlText.replace('\n', '')

	posDict = {}
	phoL = [] #keeps track of recorded pronunciations to avoid redundant entries
	for textBlock in htmlText.split("class=\"hword\"")[1:]:

		#ensure headword matches requested word. sometimes the url for words like "placed" may provide the page for the word "place"
		hword = re.search(">.+?<", textBlock).group(0)
		hword = hword[1:-1]
		if request != hword:
			break

		phoMatch = findPhos(textBlock)
		if phoMatch == 'n/a' or phoMatch in phoL or 'span class' in phoMatch:
			continue
		phoL.append(phoMatch)

		if '-' in phoMatch:	    #thus >1 syllables
			syllMatch = findSylls(textBlock)
		else:
			syllMatch = request

		partMatch = findPartOfSpeech(textBlock)
		if partMatch != 'n/a':
			if partMatch not in posDict:
				posDict[partMatch] = [syllMatch, phoMatch]
	
	if not posDict:
		print(request + '\tN/A')
	else: 
		for key,value in posDict.items():
			if len(posDict) < 2:
				partOfSpeech = '_'
			else:
				partOfSpeech = key
			print(request + '\t' + value[0] + '\t' + value[1] + '\t' + partOfSpeech)











