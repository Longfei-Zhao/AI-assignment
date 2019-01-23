""" File name:   dfa.py
    Author:      Longfei Zhao
    Date:        24.2.2017
    Description: This file defines a function which reads in
                 a DFA described in a file and builds an appropriate datastructure.

                 There is also another function which takes this DFA and a word
                 and returns if the word is accepted by the DFA.

                 It should be implemented for Exercise 3 of Assignment 0.

                 See the assignment notes for a description of its contents.
"""

import os
def load_dfa(dfa_file_name):
    """ This function reads the DFA in the specified file and returns a
        data structure representing it. It is up to you to choose an appropriate
        data structure. The returned DFA will be used by your accepts_word
        function. Consider using a tuple to hold the parts of your DFA, one of which
        might be a dictionary containing the edges.

        We suggest that you return a tuple containing the names of the start
        and accepting states, and a dictionary which represents the edges in
        the DFA.
        (str) -> Object
    """
    path = './exercise3_dfa/' + dfa_file_name
    file = open(path)
    dfa = {}
    for line in file:
        words = line.split()
        if words[0] == 'initial':
            dfa['initial'] = words[1:]
        elif words[0] == 'accepting':
            dfa['accepting'] = words[1:]
        elif words[0] == 'transition':
            edge = tuple(words[1:3])
            char = words[3]
            dfa.setdefault(char, []).append(edge)
    return dfa

def accepts_word(dfa, word):
    """ This function takes in a DFA (that is produced by your load_dfa function)
        and then returns True if the DFA accepts the given word, and False
        otherwise.

        (Object, str) -> bool
    """

    status = dfa['initial'][0]
    for char in word:
        dfa.setdefault(char, [])
        if len(dfa[char]) > 0:
            for edge in dfa[char]:
                #print(edge[0], edge[1])
                #print(type(status), type(edge[0]))
                if status == edge[0]:
                    status = edge[1]
                #print(status)
    for status_accepting in dfa['accepting']:
        if status == status_accepting:
            return True
    return False
