import nltk
from nltk import PCFG
from nltk import InsideChartParser

# Read PCFG rules from the file
grammar_file = "pcfg_grammar.txt"
pcfg_grammar = nltk.data.load(grammar_file, format='pcfg')

# CYK parsing function
def cyk_parse(sentence, pcfg_grammar):
    parser = InsideChartParser(pcfg_grammar)
    parses = list(parser.parse(sentence.split()))
    return parses

# Input sentence
input_sentence = "cat chased bird"

# Parse the sentence using CYK algorithm
parses = cyk_parse(input_sentence, pcfg_grammar)

# Print the parses and their probabilities
for parse in parses:
    print(f"Parse: {parse}")
    print(f"Probability: {pcfg_grammar.prob(parse)}")
    print()

# Output the most probable parse
if parses:
    most_probable_parse = max(parses, key=lambda parse: pcfg_grammar.prob(parse))
    print("Most Probable Parse:")
    print(most_probable_parse)
    print(f"Probability: {pcfg_grammar.prob(most_probable_parse)}")
else:
    print("No valid parse found.")
