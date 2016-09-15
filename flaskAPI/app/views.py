from app import app
from random import randint

adjectives, adverbs, nouns = [], [], []
with open("C:\\Users\\amcafee\\Documents\\GitHub\\Lynk\\adjectives\\adjectives.txt") as f:
	adjectives = f.read().split()
with open("C:\\Users\\amcafee\\Documents\\GitHub\\Lynk\\adverbs\\adverbs.txt") as f:
	adverbs = f.read().split()
with open("C:\\Users\\amcafee\\Documents\\GitHub\\Lynk\\nouns\\nouns.txt") as f:
	nouns = f.read().split()

print((adjectives[0]  + adjectives[1]).encode("utf-8", errors='waaaat'))

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World. Fucker"

@app.route('/shortener')
def shortener():
	return (adjectives[randint(0,len(adjectives))] + adverbs[randint(0,len(adverbs))] + nouns[randint(0,len(nouns))])

@app.route('/test')
def tester():
	return "Testing"

