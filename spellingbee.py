import string

cleanwords = sorted(set([word.strip().lower() for word in open('words','r')]))
print ('...using the 1934 Websters international dictionary, with ',len(cleanwords), 'words')
keyletter = [input('the mandatory letter? ')]
##sixletters= ['a','i','n','o','p','v']
sixletters=input('enter the six periphery letters, lowercase, no spaces: ')
dirtyletters = sorted(set(string.ascii_lowercase) - set(sixletters) - set(keyletter))
print('here be the puzzle as I understand you', keyletter, '+', sixletters)
notanswers = {}
dirtywords=[]
hivelist = []
answers = {}
allletters = list(sixletters) + keyletter

## generates a list of words that contain the mandatory center letter. this cuts processing time dramatically.
def ifcounts(wordlist, test):
    hivelist = []
    for word in wordlist:
        if test[0] in word:
            hivelist.append(word)
    list.sort(hivelist)
    return hivelist

##similar to ifcounts, but iterates over a list of keyletters
def lavalist(wordlist, letterlist):
    for char in letterlist:
        cache = []
        cache = ifcounts(wordlist, char)
        notanswers[char] = cache
    return notanswers

## the way to go! should pull the words in good that are NOT in bad. sets deduplicate the lists
def comparator(good, bad):
    step = []
    g = set(good)
    for key in bad:
        step.extend(bad[key])
        print (len(step))
    b = set(step)
    answer = g.difference(b)
    return answer

## winner: list of words that count. letters: ALL hive letters.
def score(winner, letters):
    points = 0
    for word in winner:
        counter = set(word)
        if len(counter) >= 7:
            points = points + 3 #words using all the letters are worth 3 points
            print (word)
        else:
            points = points + 1
    return points

##this is the impossibly slow way. I've left the function here to illustrate another method. Pull each bad word (with one of the 19 other letters) out of the centerlist
def trim(goodlist, baddict):
    for key in baddict:
        print (key, len(baddict[key]))
        for word in baddict[key]:
            print(':')
            if word in baddict[key]: #will error out if try to remove an item not in the list
                goodlist.remove(word)
    return goodlist

## the meaty bits!
centerwords = ifcounts(cleanwords,keyletter) #all words with the essential letter. this cuts the searching in half, since all answers have to have that letter. All of the answers will be in this list.
print(len(centerwords),' contain the center letter')
dirties = lavalist(centerwords, dirtyletters) #all words w/ essential letter and any letter not on the allowed list
final = comparator(centerwords, dirties)
print(len(final),' words satisfy the conditions')
print('they are ', final)
thisround = score(final, allletters)
print('the maximum possible score for this puzzle is: ',thisround)
