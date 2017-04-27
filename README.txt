TO RUN: in terminal, your local directory should be spelling-bee
Then, enter ‘python spellingbee.py’


This script should prompt the user for the letters in the week's NYT Magazine "Spelling Bee" puzzle by Frank Longo.
Every valid answer-word must contain the 'key' letter. Counted words can have any of the other six letters, but ONLY those six. For example: https://www.nytimes.com/2017/01/21/crosswords/a-little-variety.html

Another example: L + A I N O P V
Answers: Pavilion (uses all letters, so 3 points) + ['Aioli', 'anvil', 'appall', 'avail', 'lanai', 'lanolin', 'llano', 'lollipop', 'naval', 'papal', 'papillion', 'pianola', 'plain', 'polio', 'poplin', 'vanilla', 'villa', 'villain', 'viola', 'violin', 'voila']
Example 3: N + A B C H I L ::
answers: bacchanalia, bacchanalian, banal, banana, blanch, blini, cabana, cabin, canal, cancan, cannibal, chain, china, chinchilla, cinh, clinch, clinic, clinical, clinician, lanai, niacin

spelling-bee.py generates a list of all words that contain the center letter. Then another list contains every word that has a letter NOT in the 'hive.' The set of all words with the key letter and NOT any letter in the 'dirty' list yields the answer list. Then the script counts up its score.

n.b.: the magazine lists DRAMATICALLY less words than count, based on this (very old) dictionary.
