##This file contains the definition of renpy and non-renpy level methods. This does not include objects or object-methods.
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
## Improved Parser. Called by prefacing dialoge with "l", then character name, then text, surrounded by quotes.
## Special characters still need to have the \ character before them (ex. quotation marks, dollar signs etc)
## Will detect "tags" defined by a three letter word beginning with a capital Z (Z**), and perform a certain visual effect (ex. tag ZFB will cause a white flash)
python early:
    import re
    def parse_smartline(lex): ##Pre-parses string and separates into 2 variables: who, the name of the character objects; and what, the requested dialogue. Executed first when "l" is called.
        who = lex.simple_expression()
        what = lex.string()
        print(who)
        print(what)
        #print(w2)
        #print(w3)
        return (who, what)

    def execute_smartline(o):   ##Auto adds tags to "what" string for pauses after punctuation. Scans for "Z**" tags, and displays them at the requested point during dialogue. Z** tags are auto removed.

        who, what = o
        begin = 0           
        itr=0
        nwstr="{nw}"
        what = re.sub("\. ",'.{w=.6} ',what)     ##Regex for adding post-punctuation tags
        what = re.sub("\, ",',{w=.3} ',what)
        what = re.sub("\- ",'—{w=.6} ',what)
        what = re.sub("\— ",'—{w=.6} ',what)
        what = re.sub("\; ",';{w=.6} ',what)
        what = re.sub("\: ",':{w=.6} ',what)
        what = re.sub("\? ",'?{w=.5} ',what)
        what = re.sub("\! ",'!{w=.5} ',what)
        what = re.sub("\.\" ",'.\"{w=.6} ',what)     ##Regex for adding post-punctuation tags in doublequotes
        what = re.sub("\,\" ",',\"{w=.3} ',what)
        what = re.sub("\-\" ",'—\"{w=.6} ',what)
        what = re.sub("\—\" ",'—\"{w=.6} ',what)
        what = re.sub("\;\" ",';\"{w=.6} ',what)
        what = re.sub("\:\" ",':\"{w=.6} ',what)
        what = re.sub("\?\" ",'?\"{w=.5} ',what)
        what = re.sub("\!\" ",'!\"{w=.5} ',what)
        tagLocation=what.find(" Z",0,len(what)) ##Determines if there are any Z** tags in the what string.
        if tagLocation ==-1:
            renpy.say(eval(who),what)
        ## Loop that displays text in piecemeal when mid-text Z** tags are detected. If there are no tags, this loop is ignored, and dialogue is displayed normally (l above.)
        ##{nw} tags are required at the end of piecemeal strings so that there is no interruption in the displaying process. A conditional causes the final piece of the string to not contain the {nw} tag, so the complete dialogue line is not automatically dismissed by Renpy.
        while tagLocation !=-1:
            tagLocation=what.find(" Z",begin,len(what))
            cmd=what[tagLocation+1:tagLocation+4]
            #renpy.say(dgl,"b"+cmd+"b")
            if tagLocation==-1:
                nwstr=what[len(what)-1]+" "
            renpy.say(eval(who),(what[0:begin]+"{fast}"+what[begin:tagLocation])+nwstr)
            
            if tagLocation!=-1:
                fx(cmd) ##Passes string cmd to fx(str) and creates corresponding audiovisual effect before next chunk of text is displayed.
            what=what[0:tagLocation]+what[tagLocation+4:len(what)]
            begin=tagLocation

    def lint_smartline(o):  ##required error catcher
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)
    def fx(s):   ##string s contains the removed tag from string what (in execute), and creates something audiovisual
        ##Audio
        if s=="Z01":
            renpy.play("smack1.ogg")
        elif s =="Z02":
            renpy.play("aha.ogg")
        elif s=="Z03":
            renpy.play("huh.ogg")
        elif s=="Z04":
            renpy.play("ding.ogg")
        elif s=="Z05":
            renpy.play("oops.ogg")
        elif s=="Z06":
            renpy.play("gun1.ogg")
        elif s=="Z07":
            renpy.play("shock1.ogg")
        elif s=="Z08":
            renpy.play("shock2.ogg")
        elif s=="Z09":
            renpy.play("slam.ogg")
        elif s=="Z10":
            renpy.play("stab1.ogg")
        elif s=="Z11":
            renpy.play("stab2.ogg")
        ##Visual
        elif s=="ZFB":   ##"Flashbang" white flash. Doesnt show up too well, especially on low-end systems. ZF2 is snappier. idk why. 
            renpy.show("bgw")
            renpy.pause(.01)
            renpy.hide("bgw")
        elif s=="ZF2":  ##Double white flash. shows up beter than ZFB. why? i dunno.
            renpy.show("bgw")
            renpy.pause(.01)
            renpy.hide("bgw")
            renpy.pause(.01)
            renpy.show("bgw")
            renpy.pause(.01)
            renpy.hide("bgw")           
        elif s=="ZSS":
            #renpy.with_statement(sshake,always=True)  This doesnt work, idk why.
            renpy.exports.transition(sshake)   ##This works, idk why.
        elif s=="ZMS":
            renpy.exports.transition(mshake)
        elif s=="ZLS":
            renpy.exports.transition(lshake)


    renpy.register_statement("l", parse=parse_smartline, execute=execute_smartline, lint=lint_smartline)
    