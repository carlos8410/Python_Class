#!/usr/local/bin/python3
"""
This function sets a score to a player if score is higher than 
the player's recorded score or if it's missing.
"""

import shelve
import random
import os
import tempfile
import shutil

def high_score(player, score):
    # Read the shelf file from the current working directory for history
    # score data and save new high score data to the file

    shelf = shelve.open(os.path.join(os.getcwd(), 'shelf.score'))

    # This case is not defined in requirements
    if player not in shelf:
        print ("New player %s is added to the list." % player)
        shelf[player] = score
        player_score = shelf[player]
        shelf.close()
        return player_score  # For player not in the list, add the player to the list and return score

    if type(score) != int:
        print("Please input a valid score, it should be int value.")
        return shelf[player]

    shelf[player] = max(score, shelf.get(player)) if shelf.get(player) else score
    player_score = shelf[player]
    shelf.close()
    return player_score


if __name__ == "__main__":

    test_dir = tempfile.mkdtemp("_testdir")
    os.chdir(test_dir)
    shelf = shelve.open(os.path.join(test_dir, 'shelf.score'))
    score_list = {'Adam': 1, 'Bob': 2, 'Clark': 3, 'Dave': 4, 'Eason': None}
    print ('Initial score list:')

    for name in sorted(score_list.keys()):
        shelf[name] = score_list[name]
        print ("%s: %s" % (name, score_list[name]))

    shelf.close()

    for name in sorted(score_list.keys()):
        new_score = random.randint(-10, 10)
        # new_score = None
        return_score = high_score(name, new_score)
        print ('%s: %s    Assign score %s ===> %s: %s'
               % (name, score_list[name], new_score, name, return_score))

    high_score('new', 10)
    shelf = shelve.open(os.path.join(test_dir, 'shelf.score'))
    for name in sorted(shelf.keys()):
        print ('%s: %s' % (name, shelf[name]))
    shelf.close()

    try:
        shutil.rmtree(test_dir, ignore_errors=True)
    except IOError:
        pass
