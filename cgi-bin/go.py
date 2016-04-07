"""xp to rank complete calculator"""
from rank_xp_prog import rank_to_name
from rank_xp_prog import prog_bar #Gets the rank and calculates the Name
from rank_xp_prog import xp_to_rank#turns it into a Rank number
from rank_xp_prog import xp_to_percent#turns it into a percentage

VOWEL = ("a", "e", "i", "o", "u")
Cont = (" a ")
VowNam = (" an ")

def main(points):
    """
    Produces the rank, progress bar, xp and name
    """
    rank = xp_to_rank(points) # Takes xp and turns it to rank
    name = rank_to_name(rank) #turns it to a name
    percent, xpnextrank = xp_to_percent(rank, points)
    xpleft = xpnextrank-points
    if name[0].lower() in VOWEL:
        VowName = VowNam+name
        print"You are"+VowName+" Nice!"
    else:
        ConstantName = Cont+name
        print"You are"+ConstantName+" Nice!"
        
    prog_bar(percent) #Gives prog_bar the percentage
    print "You have: %d xp" % points
    print "and need: %d xp Left to rank up" % (xpleft)


if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        main(int(argv[1]))
    else:
        print"Usage: go.py xp"
        print"   eg. go.py 400000"

        
def mainJSON(points):
    """
    Produces the rank, progress bar, xp and name
    """
    rank = xp_to_rank(points) # Takes xp and turns it to rank
    name = rank_to_name(rank) #turns it to a name
    percent, xpnextrank = xp_to_percent(rank, points)
    xpleft = xpnextrank-points
    if name[0].lower() in VOWEL:
        NameTemp = " is an "+name
    else:
        NameTemp = " is "+Cont+name
    stuff = {
        "percent" : percent,
        "xp" : int(points),
        "xpleft" : int(xpleft),
        "rank" : NameTemp,
        "percentbar" : percent,
        "percentbarshow" : percent,
    }
    return stuff
