import time
import os
import datetime as dt
from dateutil.relativedelta import relativedelta,WE
from dateutil import tz 
import locale
import random

logs=[
["Three days, and no sign of Borg or bio-ships. We appear to be out of danger,but the entire crew is still on edge and so am I. Not even the calm of Master Leonardo da Vinci's workshop is enough to ease my mind."],
["Warp drive is still offline and we don't know whether the Borg have detected us. Kes's psychokinetic abilities continue to damage the ship's structural integrity, and as a result our defenses have been compromised."],
["Our condition has left us vulnerable to spatial anomalies and to any alien species eager for a piece of hardware. We've taken refuge in a class-9 nebula."],
["We've spent the last three days on the Mari homeworld. It's been a while since we've had the opportunity to make new friends and the crew seems to be making the most of our stay."],
["Seven of Nine and Commander Tuvok suffered no serious physical damage after their encounter on the alien ship. I've been eager to hear Tuvok's impressions of the species who took them hostage."],
["While the alien intruder remains trapped in the body of his last victim, The Doctor has found a way to return Tom, Steth, and me to our own bodies."],
["After two days at high warp, we've rendezvoused with the Dauntless. Arturis has helped us reconstruct most of the Starfleet message. The pieces of this puzzle are finally coming together"],
["It's been five months since we received the encoded message from the Alpha Quadrant. We know that the transmission was from Starfleet Command but we still can't decrypt it. B'Elanna thinks it's a lost cause, that too much of the data stream has been destroyed, but I haven't given up. I keep hoping inspiration will strike, somehow."],
[" We've arranged for our guests in sickbay to be taken back to their homeworld, and we can finally put this mission behind us. This will be my last encrypted log concerning the Omega Directive. The classified data files will now be destroyed."],
[" The damage to Voyager has been extreme. Both sides have taken heavy casualties and it's clear that no one is going to win this conflict. The fighting has reached a standstill and the remaining Hirogen have agreed to negotiate a truce."]
]


#print(f"Captain's Log, dana {sadasnji_trenutak}. {random_log}", end=' ')

def main():
    
    while True:
        odabir=input('Za nastavak stisnite +, a za izaz stisnite *: ')
        if odabir == '+':
            sadasnji_trenutak=dt.datetime.now()
            random_log=random.choice(logs)
            print(f"Captain's Log, dana {sadasnji_trenutak}. {random_log[0]}", end='\n')
        elif odabir == '*':
            break
        else:
            print('Pogrešan unos, pokušajte ponovno. ')
    
main()


