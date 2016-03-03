
codelist={'1':'d','2':'f','3':'t','4':'p','5':'w','6':'r','7':'q','8':'b','9':'x','0':'z','d':'1','f':'2','t':'3','p':'4','w':'5','r':'6','q':'7','b':'8','x':'9','z':'0'}
word=raw_input("enter numbers or letters to translate (enter '.' to quit):")
import sys
if word==".":
    sys.exit()
def translate_code(word):
    output=""
    finished=False
    while finished==False:
        for char in word:
            for key in codelist:
                if char==key:
                    x=codelist[char]
                    output+=x
        print ""
        print output
        print ""
        word=raw_input("enter MLS code or letters to translate:")
        if word==".":
            sys.exit()
        translate_code(word)
translate_code(word)
                    

