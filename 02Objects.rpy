##This file contains objects and object-methods (characters are object-method hybrids, why i have no idea, renpy default parser makes the distinction somewhere.)
##Objects include transitions (GUI and visual effects), characters, audio channels,
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Shaker class. Creates GUI and sprite shakes ingame. 
init python:    
    import math
    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer- turns floating point numbers to integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)
    
    
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Audio channel instantiation(s)
    renpy.music.register_channel("soundmain") #soundchannel for most usages
    
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  
#Voice blip callback instantiation  
#By standard, normal voice blips are squarewaves at a certain frequency of duration .02s, followed by a silence of .03s, creating a .05s iterated sound clip.
    def detectiveVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("detectiveBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
            #renpy.music.play("detectiveBlip.ogg", channel="sound", loop=False)
       
    def druglordVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("druglordBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def dadVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("dad.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def otakuVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("otakuBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound") 
    def fashonistaVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("fashonistaBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def sportsVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("sportsBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def chessmasterVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("chessmasterBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def roboticistVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("roboticistBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def sailorVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("sailorBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def drunkardVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("drunkardBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def programmerVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("programmerBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def romanticistVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("romanticistBlip.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def dadVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("dad.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
    def typeVoice(event, **kwargs):
        if event == "show":
            renpy.music.play("type.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def brd(event, **kwargs):
        if event == "show":
            renpy.music.play("brda.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#CTC blinking arrow callback methods
image ctcA:
       "GUI/arrow.png"
       yalign 0.9 xalign .9
       pause .5 alpha 0
       pause .5 alpha 1
       repeat


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Character instantiation
#define characterCode = Character("Displayed Character Name",callback=callbackSoundName, ctc="ctcA",ctc_position="fixed")
#All instantiations must contain the final two arguments above to create the click-to-continue arrow (ctcA).
define det = Character("Antonia Villafuerte", callback=detectiveVoice,ctc="ctcA",ctc_position="fixed")
define dett = Character("Antonia Villafuerte {size=-10}{i}(Thinking){/i}{/size}",callback=detectiveVoice,ctc="ctcA",ctc_position="fixed",what_color="#53c0e8")
define detu = Character(" ", callback=detectiveVoice,ctc="ctcA",ctc_position="fixed")
define n = Character(" ", callback=detectiveVoice,ctc="ctcA",ctc_position="fixed")   #"Narration' Voice (1st person past, from AV)
define dgl = Character("Vinny Bellucci", callback=druglordVoice,ctc="ctcA",ctc_position="fixed")
define dglu = Character("???", callback=druglordVoice,ctc="ctcA",ctc_position="fixed")
define otk = Character("Otaku {size=-10}{i}(Unnamed!){/i}{/size}", callback=otakuVoice,ctc="ctcA",ctc_position="fixed")
define fsh = Character("Fashonista {size=-10}{i}(Unnamed!){/i}{/size}", callback=fashonistaVoice,ctc="ctcA",ctc_position="fixed")
define slr = Character("Jessica Meyers", callback=sailorVoice,ctc="ctcA",ctc_position="fixed")
define prg = Character("Programmer{size=-10}{i}(Unnamed!){/i}{/size}", callback=programmerVoice,ctc="ctcA",ctc_position="fixed")
define rob = Character("Roboticist{size=-10}{i}(Unnamed!){/i}{/size}", callback=roboticistVoice,ctc="ctcA",ctc_position="fixed")
define chs = Character("Chessmaster{size=-10}{i}(Unnamed!){/i}{/size}", callback=chessmasterVoice,ctc="ctcA",ctc_position="fixed")
define rom = Character("Ian Novakov", callback=romanticistVoice,ctc="ctcA",ctc_position="fixed")
define spj = Character("Lex Wolfe", callback=sportsVoice,ctc="ctcA",ctc_position="fixed")
define drk = Character("Alan Braxton", callback=drunkardVoice,ctc="ctcA",ctc_position="fixed")

define letter = Character("Letter", callback=typeVoice,ctc="ctcA",ctc_position="fixed")
define brd = Character("Tom Brady", callback=brd,ctc="ctcA",ctc_position="fixed")

define dadu = Character(" ", callback=dadVoice,ctc="ctcA",ctc_position="fixed")



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Other instantiations
##Transition instantiations: ATL
define sshake = Shake((0, 0, 0, 0), 1.0, dist=10)
define mshake = Shake((0, 0, 0, 0), 1.0, dist=30)
define lshake = Shake((0, 0, 0, 0), 1.0, dist=50)
image tbc = "ybv.jpg"




