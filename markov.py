#!/usr/bin/env python
#from sys import argv
import sys 
import string
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # split string into a list
    word_list = corpus.split()
    # setup var for dictionary for final content
    word_dict = {}
    # setup list to hold possible values for each key
    val = []
    
    # run loop through of word_list
    for idx in range(len(word_list)- 3): #range(0,1): 

        # create a key tuple pulling sets of values from the list based on index position
        key = (word_list[idx], word_list[idx + 1])
        # capture the value after the set of words 
        val = word_list[idx + 2]

        # if key is in the dictionary
        if key in word_dict:
            # append the value to the key in the dictionary
            word_dict[key].append(val)
        else:
            #add key and value to the dictionary if it doesn't already exist
            word_dict[key] = [val]   

    # return dictionary of content
    return word_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    # establish string variables
    rand_text = ""
    clean_text = ""

    # run for loop for a set range - this can be adjusted
    for key in range(0,3):

        # set var rand_key to a random key from the dictionary
        rand_key = random.choice(chains.keys())
        # convert rand_key to a string and assign variable rand_key_str
        rand_key_str = str(rand_key)
        # set var rand_val to a random value from that particular key
        rand_val = random.choice(chains[rand_key]) 
        # add the key and value strings together
        rand_text += rand_key_str + " " + rand_val + " "

    # clean the string by stripping each word by the characters below 
    for word in rand_text:
        word = word.strip("('-_,:.\"*;?!)")
        clean_text += word

    # return random text string from dictionary              
    return clean_text

def main():
    args = sys.argv

    script, filename = args

    #open file and apply to f
    f = open(filename)

    # read and lowercase the content of f and apply to input_text var
    input_text = f.read().lower()

    # runs make_chains function to create dictionary of content
    chain_dict = make_chains(input_text)

    # runs make_text function to generate random text
    random_text = make_text(chain_dict)

    print random_text

if __name__ == "__main__":
    main()
