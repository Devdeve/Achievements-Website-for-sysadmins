"""
Functions
"""
import math
NAMES = [
    "Trickster",
    "Spellbinder",
    "Journeyman",
    "Conjurer",
    "Illusionist",
    "Shaman",
    "Channeler",
    "Witch",
    "Enchanter",
    "Visionist",
    "Alkhest",
    "Seer",
    "Sage",
    "Summoner",
    "Junior of some elements",
    "Junior of all elements",
    ##beginning ranks ^^^
    "Alchemist",
    "Shadowcaster",
    "Pyromancer",
    "Necromancer",
    "Warlock",
    "Sorcerer",
    "Beguiler",
    "Acolyte",
    "Evoker",
    "Apparitionist",
    "Phantasmist",
    "Learner of all elements",
    "Acolyte of all Elements",
    ##Experienced ranks
    "Theurgist",
    "Thaumaturgist",
    "Magician",
    "Arcanist",
    "Wizard",
    "Adept",
    "Magister",
    "Mage",
    "Magus",
    "Prestidigitator",
    "Arcanus",
    "Invoker",
    "Thaumaturge",
    "Adept of all elements", # Adept ranks
    "Eunuch",
    "Prestidgitator",
    "Theurge",
    "Cabalist",
    "Incantatrix",
    ## Highly experienced ranks
    "Guildmaster",
    "Overseer",
    "Arch-mage",
    "Master teacher",
    "Master of all Elements",
    "Master Teacher of all Elements",] ##master Ranks

PREFIXES = [
    "Convert",
    "Recruit",
    "Initiate",
    "Trainee",
    "Inexperienced",
    "Beginner",
    "In training",
    "Rookie",
    "Novice",
    "Accepted",
    #beginning PREFIX's
    "Journeyman",
    "Apprentice",
    "Top of the class",
    "Top of the year",
    "Experienced",
    ##Experienced PREFIX's
    "Highly Experienced",
    "Major",
    "Captain of",
    "Warlord",
    "Army general",
    "Corporal",
    "Leader",  ## Adept PREFIX's
    "Grand master",
    "Teacher of",
    "Idolised",
    "Supreme",
    "World known",
    "Sublime",
    "Legendary",
    "DemiGod like",
    "God like"] # Master PREFIX's

NAME_COUNT = len(NAMES)
PREFIX_COUNT = len(PREFIXES)
MAXRANK = NAME_COUNT * PREFIX_COUNT - 1

"""
Rank to name Calculator
"""
def rank_to_name(rank):
    """
    Rank to name Calc
    """
    if rank > -1:
        rank = min(rank, MAXRANK) #makes sure it is not above the highest rank.
        name_num = int(rank/PREFIX_COUNT) #calculates NAME
        pref_num = rank%PREFIX_COUNT #calculates PREFIX
        return "%s %s" % (PREFIXES[pref_num], NAMES[name_num])
    else:
        return False #returns false to go.py

def prog_bar(percentage): # not really needed.
    """
    Progress bar calculator
    """
    print"."+"-"*100+"."
    if percentage <= 10:
        print "|%s%s%.0f%%|" % (
            "#"*int(percentage),
            "-"*(98-int(percentage)),
            percentage
        )

    else:
        print "|%s%s%.0f%%|" % (
            "#"*int(percentage),
            "-"*(97-int(percentage)),
            percentage
        )
    print"'"+"-"*100+"'"#Goes to "go.py"

def xp_to_rank(points):
    """
    Experience to rank definition. gets xp from go.py
    """
    points = int(points) # Defines xp variable
    if points >= 0:
        rank = int(math.sqrt(points/1000))
        #calculates the rank by square rooting the xp divided by 1000
        return rank
    else:
        return 0

def rank_to_xp(ranktoxp):
    """
    Rank to experience converter.
    """
    if ranktoxp >= 0:
        points = int(ranktoxp**2)*1000 #Calculates rank squaring ranktoxp
        return points #Go's to "go.py"
    else:
        return 0

def xp_to_percent(rank, points):
    """
    Experience to Percent calculator definition
    """
    xpcurrentrank = (rank**2)*1000.0 #lowest xp for current rank
    xpnextrank = ((rank+1)**2)*1000.0 #lowest xp for next rank up
    xpgap = xpnextrank-xpcurrentrank #Calculates the difference
    xpprogress = points-xpcurrentrank # This provides the progress
    try:
        percent = int((xpprogress/xpgap)*100) #gos to a percentage
    except ZeroDivisionError:
        percent = 0
    return percent, xpnextrank
