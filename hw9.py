"""
Author: Sanjana Madhu
Collaborator: Michael Gajdosik
Pledge: I pledge my honor that I have abided by the Stevens Honor System
"""


PREF_FILE = "musicrecplus.txt"

def main():
    '''The main function running the music recommender. Takes in nothing.
    Loads a user_map. Asks for a username and checks if it exists in the
    user_map. If it does exist there, the menu is displayed, and if not
    preferences are requested, and then the menu is displayed. This
    function is called to run the program.'''

    PREF_FILE = "musicrecplus.txt"
    
    user_map = load_users(PREF_FILE)
    print("Welcome to the music recommender system!")

    username = input("Please enter your name: ")
    print ("Welcome,", username)

    if username not in user_map:
        get_preferences(username, user_map)
    menu(username, user_map)


def load_users(filename):
    '''Takes in a filename and loads a database users and their preferred artist
    in the form "FirstName LastName:Artist1,Artist2,Artist3..." from this file.
    Returns a mapping of usernames to their preferred artists.'''
    file = open(filename, 'r')
    user_dict = {}
    for line in file:
        [username, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        user_dict[username] = bandList
    file.close()
    return user_dict

def get_preferences(username, user_map):
    '''Takes in a username and user_map. Asks the user to input their preferences
    (indicating completion of input by pressing the enter key (entering the empty
    string). Makes a list of these preferences and then sorts the list. Stores
    the preferences in a dictionary called user_dict by the key of the input username.'''
    pref = []
    while(True):
        prefrences =  input("Please input a favorite artist. Press enter to continue:")
        if prefrences == "":
            break
        pref.append(prefrences)
    pref.sort()
    user_map[username] = pref
    save_user_preferences(username, pref, user_map, PREF_FILE)
    
def save_user_preferences(username, prefs, user_map, filename):
    '''Takes in a username, prefs, a user_map, and a filename.
    Writes all of the user preferences to the file. Returns nothing.'''
    user_map[username] = prefs
    file = open(filename, "w")
    for user in user_map:
        toSave = str(user) + ":" + ",".join(user_map[user]) + \
                 "\n"
        file.write(toSave)
    file.close()    

def menu(username, user_map):
    '''Takes in a username and user_map. Displays the abilities of the music
    recommender to the user. Allows him to select an option to execute.
    Calls a function to execute the selected option and then displays all the
    possible options once again repeatedly until the user quits the program.'''

    while True:
        option = input('Enter a letter to choose an option:' + '\n' + '\t' + 'e - enter preferences' + '\n' + '\t' 'r - get recommendations' + '\n' + '\t' \
            + 'p - show most popular artists' + '\n' +'\t' + 'h - how popular is the most popular' + \
            '\n' + '\t' + 'm - which user has the most likes' + '\n' + '\t' + 'q - save and quit')
        if option == 'e':
            prefs = [input("\nEnter your preferences separated by a comma.\n")]
            save_user_preferences(username, prefs + user_map[username], user_map, PREF_FILE) 
        if option == 'r':
            #print(get_recommendations(username, user_map))
            recs = get_recommendations(username, user_map)
            print_recs(recs, username)
        if option == 'p':
            print(best_artists(user_map))
        if option == 'h':
            print(how_pop_is_most_pop_artist(user_map))
        if option == 'm':
            print(best_user(user_map))
        if option == 'q':
            return None
        if option not in ['e','r','p','h','m','q']:
            print("That is not an option.")

def print_recs(recs, username):
    '''Takes in a list of recommendations and a username. Prints recommendations
    for the username. If no recommendations are available for the input username,
    a notification of such information is printed to the screen.'''
    if len(recs) == 0 or len(recs) == 1:
        print("I'm sorry but I have no recommendations")
        print("for you right now.")
    else:
        print(username, "based on the users I currently")
        print("know about, I believe you might like:")
        for artist in recs:
            print(artist)
        print("I hope you enjoy them! I will save your")
        print("preferred artists and have new")
        print(" recommendations for you in the future")
   # save_user_preferences(username,pref,user_map,PREF_FILE)

def get_recommendations(curr_user, user_map):
    '''Takes in a current user, preferences, and a user_map. Finds the user
    whose likes are most similar to that of the current user (without being 
    exactly the same. Returns artist recommendations for the current user
    based on whatever artists are liked by the most similar user that are
    not already liked by the current user.'''
    bestUser = find_best_user(curr_user, user_map)
    if bestUser != None:    
        recommendations = drop(user_map[curr_user], user_map[bestUser])
        return recommendations
    else:
        return []

def delete_duplicates(lst):
    '''Takes in a list. Returns a list with all elements from the original
    list occurring exactly once.'''
    newlst = []
    for x in lst:
        if x not in newlst:
            newlst.append(x)
    return newlst

def find_best_user(curr_user, user_map):
    '''Takes in a current user, preferences, and a user_map. Finds the user whose
    artist preferences are most similar to the current user without being exactly
    the same. Returns this user.'''
    users = user_map.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        score = num_matches(user_map[curr_user], user_map[user])
        if score > bestScore and curr_user != user and user[-1] != "$" :
            bestScore = score
            bestUser = user  
    return bestUser

def num_matches(L1, L2):
    '''Takes in two SORTED lists and returns the number of matching elements 
    between the two lists.'''
    L1.sort()
    L2.sort()
    matches = 0
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] == L2[j]:
            matches += 1
            i += 1
            j += 1
        elif L1[i] < L2[j]:
            i += 1
        else:       
            j += 1
    return matches

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3

def best_artists(user_map):
    '''Takes in a user_map. Prints out the most popular artist or artists.
    If no artist is found, the user is notified by printing a message telling
    them that no artists were found.'''
    maxScore = 0
    bestArtist = {}
    bestList = []
    for username, artistList in (user_map.items()):
        for values in artistList:
            if values in bestArtist and username[-1] != "$":
                bestArtist[values] += 1
            elif values not in bestArtist and username[-1] != "$":
                bestArtist[values] = 1
    for artist, score in bestArtist.items():
        if score > maxScore:
            maxScore = score
            bestList = [artist]
        elif score == maxScore:
            bestList.append(artist)
    return bestList
    
def how_pop_is_most_pop_artist(user_map):
    '''Takes in a user_map. Prints out how popular (a number) the most popular
    artist(s) is(are) based on how many users like a given artist.'''
    maxScore = 0
    bestArtist = {}
    for username, artistList in (user_map.items()):
        for values in artistList:
            if values in bestArtist and username[-1] != "$":
                bestArtist[values] += 1
            elif values not in bestArtist and username[-1] != "$":
                bestArtist[values] = 1
    for values in bestArtist.values():
         if values > maxScore:
            maxScore = values
    return maxScore

def best_user(user_map):
    '''Takes in a user_map. Returns the user with the most likes.'''
    maxLen = 0
    bestList = []
    for username, artistList in user_map.items():
        if username[-1] != "$" or len(artistList) == maxLen:
            bestList.append(username)
        elif username[-1] != "$" or len(artistList) > maxLen:
            maxLen = len(artistList)
            bestList = [username]
    return bestList     
    
main()
