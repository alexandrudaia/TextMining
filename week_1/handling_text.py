#sentences/input  strings
#words  or tokens 
#Characters 
#Document,larger  files
#this  are primitives
text1='Ethics are build right into the ideal andobjectives of the united   Nations   '
print(len(text1))
#the  tokens  from text1  are the  words 
text2=text1.split(' ')
print(text2)
print(len(text2))

################Finding  Specific words#########################

#example 1  :  words  that are  most  then  3 letters  long
long_words=[w for  w  in  text2 if len(w)>3]
print(long_words)
#example 2 : capitalize words
print([w for w in text2  if w.istitle()])
#example 3:  words   that  end with   s
print([w for  w in text2  if  w.endswith('s')])
################Finding  unique   words#######################
text3='to be or not to  be'
text4=text3.split(' ')
print(len(set(text4)))
print(len(set([w.lower() for  w in text4])))
#s.startswith()
#s.endswith()
#t in s
#s.isupper() ;  s.islower(); s.istitle()
#s.isalpha() ;  s.isdigit() ; s.isalnum()
#s.split(t)
#s.splitlines()
#s.join(t)
#s.strip()  ;   s.rstrip()
#s.find() ; s.rfind()
#s.replace(u,v)
#example :

text5='ouagadougou'
text6=text5.split('ou')
print(text5)
print(text6)

'ou'.join(text6)
text8=' A  quick  brown fox  jumped  over the  lazy dog. '
print(text8.rstrip())
print(text8.split(' '))

print(text8.find('o'))

print(text8.replace('o','O'))






