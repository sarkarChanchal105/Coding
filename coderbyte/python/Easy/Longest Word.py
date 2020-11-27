"""
https://coderbyte.com/editor/Longest%20Word:Python3


Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love

"""


def LongestWord(sen):

  # code goes here
  new_word=''

  for letter in sen:
      if letter.isalpha() or letter.isnumeric():
            new_word+=letter
      else:
          new_word+=" "
  print(new_word)

  #k=list(map(lambda x:len(x),new_word.split()))
  return max(new_word.split(),key=len)


# keep this function call here
print(LongestWord(input()))