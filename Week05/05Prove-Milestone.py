# Adventure Game

print('\n\nGreetings! You have died. However, you have been given the chance to go on one last adventure before you move on for your final judgement.')
adventure = input('\nWould you like to go on this adventure? (YES or NO) ')

if adventure.lower() == 'yes':
    print('\nWonderful choice! Good luck on your adventure!\n')
    print('There are a couple portals prepared, so go ahead and choose one and you will be sent on your way with a guide to journey with you.')
    print('On the otherside of PORTAL1 is a typical fantasy world with dragons, magic, and dungeons. On the otherside of PORTAL2, is an adventure during which you get to experience/survive through different random movie scenarios. So go ahead! Choose one! And don\'t worry about PORTAL3 over there...that one is still under construction. \n')
    world = input('\nWhich portal will you go through? ')
    if world.lower() == 'portal1':
        # PORTAL 1
        print('\nYou enter the fantasy portal and after arriving in the new world, you discover that you are an adventurer. After walking around a bit and taking in your new reality, you see an old man in distress. The old man asks you to save his son who is lost in the forest behind the town. He is too old to search by himself and he is worried that his son may have entered a super dangerous dungeon.')
        print('You can either HELP the old man find his son, or you can LEAVE the old man and find something else to do.')
        fantasy_elder = input('\nWhat will you do? ')
        if fantasy_elder.lower() == 'help':
            # Help Old Man
            print('\nYou decide to help the old man and immediately leave to start looking for the boy as soon as possible. While working your way through the forest, you and your guide go up a mountain and see a boy\'s footprints. Following these prints leads you to a hidden cave. Once inside the cave you see an ancient city in near-perfect condition filled with what appears to be golems. After looking around a bit, the guide spots a child surrounded by some of the golems. In a panic you both run up to the golems and try to attack. However, being only level 1, you basically deal negative damage to the golems.')
            print('\nThinking fast, you work out that you have two courses of action. You can SNATCH the kid and run, or you can WAIT and see what happens next before making more decisions. ')
            save_kid = input('\nWhat will you do? ')
            if save_kid.lower() == 'snatch':
                # Snatch the Kid
                print('\nYou snatch the kid and run faster than you have ever have before. After returning to the town and reuniting the old man and his son, you tell the old man about what you saw. After hearing about the ancient city and the magical golems, the old man declares that he wants to attack the golems \'for revenge for his son\'. He leads the villagers as they take up weapons and kill the golems. For some reason, the golems are actually quite peaceful, and together the villagers take them down without a fight. The ancient city is plundered mercilessly and burned to the ground. Life seems to return to normal when everyone returns to the town. So, you take on a couple more quests as an adventurer before your time in the world ends. \n')
                print('THE END\n')
            elif save_kid.lower() == 'wait':
                # Wait and See
                print('\n You take a step back and see that the golems aren\'t attacking the kid at all. In fact, the kid seems to be very well taken care of. The golems seem to have a collection of fruits and treat the kid like a king. After taking a moment to communicate with the golems, you learn that the golems were tasked with protecting the ancient city, and had long outlived their creators. Another discovery was that the kid had been planning on taking the golems back as slaves. In order to keep the kid there, the golems bribed him with fruits to keep their secret. All they wanted to do was live in peace and protect the city.')
                print('You decide you have two courses of action. Either KILL the golems because they might have lied and could be a threat to the town if they want revenge, or CONVINCE the kid to forget about the golems and go home.')
                kid_end = input('\nWhat would you like to do? ')
                if kid_end.lower() == 'kill':
                    # Kill the Golems
                    print('\nYou strike swiftly, dashing towards the golems. Although the kid seems unharmed, you haven\'t done a thorough examination on him or his mental state. It is better to be safe than sorry. However, it is only after you strike that you remember that you are still only level one. You deal no damage to the golems. The golems divulged the truth and you didn\t believe them. When you attacked they deemed it as a threat and decided to take action.\n')
                    print('YOU DIED\n')
                elif kid_end.lower() == 'convince':
                    # Convince the Kid
                    print('\nIt seems like the golems are telling the truth. The boy does seem to be in good health and spirits after all. You tell the boy that if he tells anyone about the golems, he will face a fate he can only imagine. You continue laying on other threats, playing a sort of good-cop, bad-cop duo with the help of the guide. Afterwards, you return the kid to the village and continue keeping an eye on him while taking on more quests to level up with the limited time you have left in the world.')
                    print('THE END\n')
                else:
                    print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                    print('May God have mercy on your soul.\n')
            else:
                print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                print('May God have mercy on your soul.\n')
        elif fantasy_elder.lower() == 'leave':
            # Leave Old Man
            print('\nYou know what? You are right. Leave the old man to figure things out. It\'s his life and his son. People should help themselves. Life isn\'t about settling for the first choice anyway.')
            print('You tell the old man sorry and that his kid will probably be fine; and that if the boy was really was dumb enough to go into a dungeon alone, he proabably doesn\'t deserve to live anyway.')
            print('You seem like a person who thinks sympathy is for the weak. Are you interested in joining the dark side? Burning cities, wreaking havok, etc.?')
            chaosq = input('\n Would you like to DESTROY the town or leave and go on a different JOURNEY? ')
            if chaosq.lower() == 'destroy':
                # Destroy Town
                print('\nYou really want to do this? Certainly sounds like an adventure.')
                print('You decide to open the back gate and let all the monsters in from the forest so that they can destroy the town. However, you see that the back gate is guarded by soldiers...')
                weapon = input('\nHow do you take them down? With a SWORD or a WAND? ')
                if weapon.lower() == 'sword':
                    # Sword
                    print('\nNice! Easy to use and to clean. Stabbing will make this dark route very real.')
                    print('You kill the guards with ease. Your guide opens the gates and you two quickly find a safe place to wait out the incoming chaos. Monsters flood in through the unguarded gates and the kingdom falls apart incredibly quickly. You see the old man from earlier die because he is old and can\'t run away. \'At least his son is safe in the mountains right?\', you think to yourself.')
                    print('After the chaos dies down a bit, you and your guide head out in the pursuit of more chaos.')
                    print('\nTHE END\n')
                elif weapon.lower() == 'wand':
                    # Wand
                    print('\nOh? A magic caster?')
                    print('...wait...WHAT DO YOU MEAN YOU DON\'T KNOW HOW TO DO MAGIC?!?? The guards are coming! Who picks a wand without knowing how to use it??' )
                    print('The guards easily take you and your guide down in your moment of panic and confusion.')
                    print('\nYOU DIED\n')
                else:
                    print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                    print('May God have mercy on your soul.\n')
            elif chaosq.lower() == 'journey':
                # Don't Destroy Town
                print('\nSo you don\'t want to destroy the town? That\'s probably for the best.')
                print('Since you have a taste for other things in life, you decide to leave the town and go off on a new adventure. You travel around the world going from kingdom to kingdom saving people. You gather comrades, and even find love. Eventually you go and defeat the demon king.')
                print('\nTHE END\n')
            else:
                print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                print('May God have mercy on your soul.\n')
        else:
            print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
            print('May God have mercy on your soul.\n')
    elif world.lower() == 'portal2':
        # PORTAL 2 
        print('\nAfter you enter the portal and open your eyes in the new world, you look down and find yourself and your guide dressed in white clothing. ')
        print('You are an orphan living in a beautiful, enclosed space. There are grass fields, a forest, and a large house for you and the other orphans in the center of the land. The walls surrounding the whole area are thick, tall stone walls. When you turn of age, (12-13) you are sent out of the orphanage to live a happy wonderful life....the end.')
        print('\n Just kidding. Did you really think that was it? In reality, the \'mom\' that raises you and the other orphans, is actually giving you away to monsters who eat you.')
        promised_neverland = input('\nDo you and the guide tell everyone what is going on so that you can form a plan TOGETHER? Or do you create a plan ALONE to save yourself and the children? ')
        if promised_neverland.lower() == 'together':
            # Tell the Kids 
            print('\nYou and your guide work together to gather the children so that you can tell them the truth of the situation. Nothing could possibly go wrong by telling young adolescents that their mother figure wants them dead right?....')
            print('...Well...Unfortunately the children don\'t know what to do with the information that they recieve. They freak out and try to escape without a proper plan. Everything falls apart, the monsters capture them and eat them as you and the guide hide. ')
            print('You might feel guilty, but there is nothing you can do now. A portal opens up and so you enter with the guide before you get caught.')
            print('\nIn the new world, you enter a town named Salem and it seems to be around the time of the 15th century. In this town there is a rogue mafia member on the loose murdering people. You and your guide are detectives and you currently have two suspects: (1) One is an old man named Frank who is a pillar of the community. He helps the poor, constantly strives to be a better person, and is just an outstanding guy in general. (2) Another suspect is a girl named Lucia. She recently moved into the city and the murders started happening shortly after. Is there some kind of correlation? ')
            guilty1 = input('\nWho do you think is guilty? The old MAN or the new GIRL in town? ')
            if guilty1.lower() == 'man':
                # Old Man
                print('You picked the old man???? But Frank hasn\'t ever hurt a fly in his life. And the whole community has vouched for him many times.')
                print('On the other hand...this Lucia girl who no one knows... Her last name is Corleone and she calls her dad the Godfather. I mean, just the other night someone saw her with blood in her clothes. She is really suspicious.')
                guilty2 = input('\nNow decide...Do you want to KEEP your previous answer of the old man being guilty? Or do you want to CHANGE your answer and declare Lucia guilty? ')
                if guilty2.lower() == 'keep':
                    # Old Man 
                    print('Are you serious?? Lucia\'s job here in the city is literally to clean vents. She goes in them all the time. Also, her middle name is \'Sus\'. Her full name is Lucia Sus Corleone!')
                    print('I don\'t think you understand how kind this old man is compared to this weird, sus girl. He rescues kittens and puppies for a living.')
                    print('I don\'t know how to make this more clear. You should really pick Lucia.')
                    guilty3 = input('\nDo you pick FRANK or LUCIA? ')
                    if guilty3.lower() == 'frank':
                        # Old Man!! 
                        print('Okay this isn\'t some momento BS where at the end of the story there is some huge twist and the guilty is the least suspected. Nor is it some Markiplier closet where the decision you\'re forced to make is the wrong decision. Lucia is definitely guilty.')
                        print('I don\'t know how much more I can make this clear. She is more suspicious than a dark figure in the shadows of an anime show. What do you think is going to happen? She is going to be so thankful that you didn\'t kill her? Then watch. She is going to go off killing more of the townsfolk.')
                        final_guilty = input('\nYou only have one more choice now. Pick her. Declare Lucia CORLEONE to be guilty. What do you say? ')
                        if final_guilty.lower() == 'corleone':
                            # Lucia is Guilty
                            print('\nOh!...You picked her. In that case, let the trial begin!')
                            print('The community has already deemed her to be guilty, but lets hear her out...')
                            print('She doesn\'t have any proof that she isn\'t mafia or the murderer. However, this is the 15th century. There is no innocent until proven guilty.')
                            print('Lucia is officially declared guilty and sentenced to death.')
                            print('\n....wait....she wasn\'t guilty?')
                            print('...and she was hanged too....yikes what a twist...')
                            print('\nTHE END\n')
                        else:
                            print('\nReally? There was only one choice there and you still messed that up. Look...I don\'t have time for your childish games so I will end your journey here and send you off to your final judgment.')
                            print('May God have mercy on your soul.\n')
                    elif guilty3.lower() == 'lucia':
                        # Lucia 
                        print('\nOh!...You picked her. In that case, let the trial begin!')
                        print('The community has already deemed her to be guilty, but lets hear her out...')
                        print('She doesn\'t have any proof that she isn\'t mafia or the murderer. However, this is the 15th century. There is no innocent until proven guilty.')
                        print('Lucia is officially declared guilty and sentenced to death.')
                        print('\n....wait....she wasn\'t guilty?')
                        print('...and she was hanged too....yikes what a twist...')
                        print('\nTHE END\n')
                    else:
                        print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                        print('May God have mercy on your soul.\n')
                elif guilty2.lower() == 'change':
                    # Lucia
                    print('\nOh!...You picked her. In that case, let the trial begin!')
                    print('The community has already deemed her to be guilty, but lets hear her out...')
                    print('She doesn\'t have any proof that she isn\'t mafia or the murderer. However, this is the 15th century. There is no innocent until proven guilty.')
                    print('Lucia is officially declared guilty and sentenced to death.')
                    print('\n....wait....she wasn\'t guilty?')
                    print('...and she was hanged too....yikes what a twist...')
                    print('\nTHE END\n')
                else:
                    print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                    print('May God have mercy on your soul.\n')
            elif guilty1.lower() == 'girl':
                # Lucia
                print('\nOh!...You picked her. In that case, let the trial begin!')
                print('The community has already deemed her to be guilty, but lets hear her out...')
                print('She doesn\'t have any proof that she isn\'t mafia or the murderer. However, this is the 15th century. There is no innocent until proven guilty.')
                print('Lucia is officially declared guilty and sentenced to death.')
                print('\n....wait....she wasn\'t guilty?')
                print('...and she was hanged too....yikes what a twist...')
                print('\nTHE END\n')
            else:
                print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                print('May God have mercy on your soul.\n')
        elif promised_neverland.lower() == 'alone':
            # Plan Escape Alone 
            print('\nInstead of suddenly breaking the truth to the children, you and your guide work to devise a plan that is understandable to children, and slowly introduce it to them so that they don\'t become traumatized for life.')
            print('That was the right choice! The adventure you\'ll have now will constantly give you ultimatums. Lets see if you can stay alive until the end!')
            print('\nAfter saving the children, another portal opens and you enter it. Now on the other side, you and your guide see a castle and recognize it as Hogwarts! You are first years and while wandering around, you accidentally enter the chamber where the sorcerers\' stone is hidden and get trapped in the snake-like tendril of The Devil\'s Snare. You can\'t seem to get out of it, and it only gets tighter as you two struggle.')
            print('You know that there was a spell that Hermione used, but you can\'t quite remember....')
            spell = input('\nWhat is LUMOS -something? Or was it LANG -something? ')
            if spell.lower() == 'lumos':
                # Lumos 
                print('\nYou wave your wand with the one hand that is free, chanting the spell lumos-solem. A light emerges from your wand and the plant shrinks and shivers away, freeing you.')
                print('Congrats! You have survived through another story.')
                print('\nA new portal opens for you and your guide to enter. In the new world, you hear an alarm bell going off and as you look around, you see that you are in some kind of secret facility. There are SCP creatures on the loose, the foundation has been breached, and you need to escape.')
                print('You see two doors that you can go through. One says SCP500 on the outside, and the other says SCP6868.')
                scp = input('\nWhich door do you go through? ')
                if scp.lower() == 'scp500':
                    # SCP 500 
                    print('\nYou enter the room of SCP 500 only to see a table with 47 red pills in a plastic can sitting on it. Doesn\'t seem too deadly...')
                    print('With trembling hands, you pick it up and it opens. Meanwhile the guide finds a paper on the floor and reads it. It is a description!')
                    print('One pill, when taken orally, effectively cures the subject of all diseases within two hours! You take one pill and leave the rest there.')
                    print('\n Moving on, you enter a room and the door disappears behind you and your guide. At the center of the room, there is a single die sitting on the table.')
                    print('This test is absolute. It tests the one skill you need to be born with...luck.')
                    is_diceroll = int(input('\nPick a number 1-6 to guess what it will roll: '))
                    if is_diceroll <= 3 and is_diceroll >= 1:
                        print('\nYOU DIED\n')
                    elif is_diceroll <=6 and is_diceroll >= 4:
                        print('\nYOU SURVIVED! Congrats!')
                        print('This is the end of your adventure, but I will put in a good word for you for making it this far. Best of luck going forward.')
                        print('May God have mercy on your soul.')
                    else:
                        print('\nApparently luck wasn\'t the only thing you weren\'t born with...I think it is time you moved on. Clearly you don\'t want to continue this adventure anymore. Best of luck with your judgement.')
                        print('May God have mercy on your soul.')
                elif scp.lower() == 'scp6868':
                    # SCP 6868
                    print('\n You enter the room that holds SCP 6868 and see a purple rubber ducky. It has to be safe right? The duck is so cute!')
                    print('As you and the guide approach it, the duck hops away. You keep approaching the cute duckie until it is cornered with no where to go. When you make an attempt to grab the duck, you start foaming at the mouth and die instantly.')
                    print(' The duck can turn any liquid into water (in this case your blood) and dislikes being touched by humans.')
                    print('\nYOU DIED\n')
                else:
                    print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                    print('May God have mercy on your soul.\n')
            elif spell.lower() == 'lang':
                # Lang
                print('\nYou wave your wand with the one hand that is free and chant lang-lock. Suddenly your guide can\'t speak -- you had cast a spell that makes a target\'s tongue stick to the roof of their mouth. Now the guide is useless and you are out of ideas. Both of you are stuck and have to wait until the headmaster comes to save you...whenever that is.')
                print('\nTHE END\n')
            else:
                print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
                print('May God have mercy on your soul.\n')
        else:
            print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
            print('May God have mercy on your soul.\n')
    elif world.lower() == 'portal3':
        # PORTAL 3
        print('\n...wait....WHAT ARE YOU DOING HERE??!?')
        print('You aren\'t supposed to be here. This area is still under construction. Everything is just a bunch of random words and bits of code still.')
        print('Unfortunately I can\'t just let you leave after what you may have seen in here. You and your guide will be disposed of.\n')
        print('YOU DIED\n')
    else:
        print('\nSorry, that wasn\'t an option. If you didn\'t want to go on this adventure, why didn\'t you just say that you wanted to just move on? I will send you to where you will recieve your final judgement.')
        print('May God have mercy on your soul.\n')
elif adventure.lower() == 'no':
    print('\nIn that case, I wish you the best of luck. May God have mercy on your soul.\n')
else:
    print('\nI see that you decided not to pick an option provided. Unfortunately, this means that I will decide for you, and you will move on without a last adventure. I wish you the best of luck. May God have mercy on your soul.\n')