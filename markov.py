#!/usr/bin/env python
#from sys import argv
import sys 
import string
import random
import twitter

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
    for idx in range(len(word_list)- 5): #range(0,1): 

        # create a key tuple pulling sets of values from the list based on index position
        #key = (word_list[idx], word_list[idx + 1])
        #val = word_list[idx + 2]

        # Extra Credit 2: Modify the program to allow any number of words to use as keys, ie: choose the size of your n-gram used in your chain
        # capture the value after the set of words. 
        #Now key is comprised of 5 words
        key = (word_list[idx], word_list[idx + 1], word_list[idx + 2], word_list[idx + 3], word_list[idx + 4])

        val = word_list[idx + 5]

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

    #Twitter Authorization settings for Ron Suess user account
    api = twitter.Api(consumer_key='dw71KKcWg6fzxozOv5W0Q',consumer_secret='AxoPHUcRDl211E9a0PdpK6dg4ezkEYynZA79ZgO78', access_token_key='1278546524-FaFhodBWscK8KUH85Q4lzxpP4O1T6zaP4WAuY52',access_token_secret='AU0VPtJJQIyASUfirYQ0tNOZLY2UBLjNsBvTbom49Ho')

    #Send tweet of random_text to twitter account
    status = api.PostUpdate(random_text)
    print random_text

if __name__ == "__main__":
    main()
