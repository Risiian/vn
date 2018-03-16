python early:

    def parse_smartline(lex):
        who = lex.simple_expression()
        what = lex.rest()
        return (who, what)

    def execute_smartline2(o): ###DEFUNCT
        who, what = o
        finalstr = "SDFDSF"
        begin = 0           
        itr=0
        tagLocation=what.find(" ZFB",begin,len(what))
        if tagLocation == -1:
            renpy.say(det,what)
        while tagLocation != -1:
            if begin !=0:
                tagLocation=what.find(" ZFB",begin,len(what))
                renpy.say(dglu,"tagloc "+str(tagLocation)+" begin "+str(begin)+" finalstr " + finalstr + " ITR" +str(itr))
                finalstr=(what[0:begin-4]+what[begin:tagLocation])
                
                renpy.say(det,finalstr[0:begin-4]+"{fast}"+what[begin:tagLocation]+"{nw}")       
                begin=tagLocation+4
                
            if begin ==0:
                renpy.say(det,what[begin:tagLocation]+"{nw}")
                begin=tagLocation+4
            
            #renpy.say(det,what)
            #renpy.say(det,str(tagLocation)+"{w=.3}{nw}")
            smack()
            #renpy.say(dglu,"tagloc "+str(tagLocation)+" begin "+str(begin))
            itr+=1
        
    def execute_smartline(o):
        who, what = o
        begin = 0           
        itr=0
        nwstr="{nw}"
        tagLocation=what.find(" Z",0,len(what))
        if tagLocation ==-1:
            renpy.say(eval(who),what)
        while tagLocation !=-1:
            tagLocation=what.find(" Z",begin,len(what))
            cmd=what[tagLocation+1:tagLocation+4]
            #renpy.say(dgl,"b"+cmd+"b")
            if tagLocation==-1:
                nwstr=" "
            renpy.say(eval(who),(what[0:begin]+"{fast}"+what[begin:tagLocation])+nwstr)
            if tagLocation!=-1:
                fx(cmd)
            
            what=what[0:tagLocation]+what[tagLocation+4:len(what)]
            
            begin=tagLocation
            
            
        
        
    def lint_smartline(o):
        who, what = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)
    def smack():
        renpy.play("smack1.ogg")
    def fx(s): 
        if s=="ZFB":
            renpy.play("smack1.ogg")
        else:
            renpy.play("huh.ogg")
    renpy.register_statement("line", parse=parse_smartline, execute=execute_smartline, lint=lint_smartline)
    