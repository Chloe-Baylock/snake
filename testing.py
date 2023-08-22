class Word:
  def __init__(self, body):
    self.body = body

a = Word([((1,1))])
b = Word([((2,2))])

wordList = [a,b]

for w in wordList:
  if (((1,1)) in w.body):
    print('here')

if any(((1,1)) in w.body for w in wordList):
  print('here')

# x = [w.body for w in wordList]
# print(((1,1)) in x)
# print(x)