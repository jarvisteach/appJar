import string
def validateString(data):
    for p in string.punctuation:
        if p in data:
            return False
    return True

# get inputs and make uppercase
while True:
    sentence = input("Enter a sentence: ").upper()
    if not validateString(sentence):
        print("ERROR - you can't have punctuation in the sentence!")
        continue
    # if we get here - it's all valid!
    break

while True:
    searchWord = input("Enter a search word: ").upper()
    if not validateString(searchWord):
        print("ERROR - you can't have punctuation in the search word!")
        continue
    # if we get here - it's all valid!
    break

# print out variables
print("You are searching for:", searchWord)
print("In:", sentence)

sentenceArray = sentence.split(" ")
wordCount = len(sentenceArray)
print("SentenceArray:", sentenceArray)
print("Word count:", wordCount)

