import re
import signal
import subprocess
import easygui as eg
line_offset = []
offset = 0
count=-1
l=[]
filename=1
src=""
filelist=[]
declaration = re.compile("(int|float|char|long|double).")
base = eg.fileopenbox(msg=None, title=None, default=None)
basefile=base.split('/')[-1]
f = open(basefile, "r")
content=f.read()
f.seek(0, 0)
for line in f:
    line_offset.append(offset)
    offset += len(line)
f.seek(0,0)
content = f.readline();
#print linecache.getline('f.c', 4)
filelist.append(basefile)
def copy_strt():
        global l
        global filename
        global src
        src=str(filename)+".c"
        filelist.append(src)
        f1= open(src, 'w')
        for i in l[:-1]:
                f1.write(i)
                
                
                
                

def copy_end(): 
        global filename
        f.seek(line_offset[count+1])
        line=f.readline()
        while (line):
                f1.write(line)
                line=f.readline()
                    
        f1.write(line)
        f.seek(line_offset[count+1])
        filename=filename+1
        
name=[]
inp=[]
while content:
       #print "read line ",content
        l.append(content)
        count = count+1
        if "main()" in content:
                pass
        
        elif declaration.match(content):
                 typ=content.split(' ', 1)[0]
                 x=content.strip(";\r\n")
                 x=x.split(' ')
                 var=x[1].split(',')
                 for i in var:
                     if '=' in i:
                        name.append([i.split('=')[0],typ])
                     else:
                        name.append([i,typ])
                 #print name  #list of all var declared
        elif "scanf(" in content:
              for i in name:
                if '[' in i[0] and "&"+i[0][:i[0].index('[')+1] in content:
                        inp.append([i[0][:i[0].index('[')+1]+"]",i[1]])
                elif "&"+i[0] in content:
                        inp.append(i)
                
              #print inp #list of all var with datatypes that are scanned
                  
        elif "for(" in content:
                x=content.split('(')
                x=x[1].strip(')\r\n')
                x=x.split(";")
                #print x
                ###
                if '++' in x[2]:
                        st="for("+x[0]+";"+x[1]+';'+x[2].replace('++','--')+')\r\n'
                        copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
                if '--' in x[2]:
                        st="for("+x[0]+";"+x[1]+';'+x[2].replace('--','++')+')\r\n'
                        copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
                if ">=" in x[1]:
			st="for("+x[0]+";"+x[1].replace('>=','>')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
		elif ">" in x[1]:
			st="for("+x[0]+";"+x[1].replace('>','>=')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
			st="for("+x[0]+";"+x[1].replace('>','==')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
			st="for("+x[0]+";"+x[1].replace('>','<=')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
		if "==" in x[1]:
			st="for("+x[0]+";"+x[1].replace('==','>=')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                if "!=" in x[1]:
			st="for("+x[0]+";"+x[1].replace('!=','==')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
		if "<=" in x[1]:
			st="for("+x[0]+";"+x[1].replace('<=','<')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
		elif "<=" in x[1]:
			st="for("+x[0]+";"+x[1].replace('<','<=')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
			st="for("+x[0]+";"+x[1].replace('<','>=')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
			st="for("+x[0]+";"+x[1].replace('<','==')+';'+x[2]+')\r\n'
			copy_strt()
                        f1= open(src, 'a')
                        f1.write(st)
                        copy_end()
                        f1.close()
                        
                
         
        elif "if(" in content or "while(" in content:
		x=content.split("(")
		x =x[1].strip(")\r\n")
		x=x.split(" ")
		st = "if(" if "if(" in content else "while("
		st=st+"1)\r\n"
                copy_strt()
                f1= open(src, 'a')
                f1.write(st)
                copy_end()
                f1.close()
                copy_strt()
                f1= open(src, 'a')
                f1.write(st.replace('1','0'))
                copy_end()
                f1.close()
               	
		
		for i in range(0,len(x)):
			if ">=" in x[i]:
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('>=','>')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
			elif ">" in x[i]:
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('>','>=')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()     
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('>','==')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()     
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('>','<=')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()     

			if "<=" in x[i]:
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('<=','<')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()     

			elif "<" in x[i]:
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('<','<=') 
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()     
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('<','==')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()     
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('<','>=')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()    
			if "==" in x[i]:
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('==','>=')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
                        if "!=" in x[i]:
				st = "if(" if "if(" in content else "while("
				for token in x[:i]:
					st = st+token+" "
				st = st + x[i].replace('!=','==')
				for token in x[i+1:]:
					st = st+token+" "
				st = st + ')\r\n'
				copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
        elif '++' in content and not '=' in content:
                st=content.replace('++','--')
                copy_strt()
                f1= open(src, 'a')
                f1.write(st)
                copy_end()
                f1.close()
        
        elif '++' in content and not '=' in content:
                st=content.replace('--','++')
                copy_strt()
                f1= open(src, 'a')
                f1.write(st)
                copy_end()
                f1.close()
        
                      
        elif ('+' in content or '-' in content or '*' in content or '/' in content or '%' in content) and '=' in content and content.count(";")==1:        
                if "+" in content:
                        indices = [i for i, x in enumerate(content) if x == "+"]
                        #print indices
                        for i in indices:
                                st=content[:i]+'*'+content[i+1:]
                                copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
                if "-" in content:
                        indices = [i for i, x in enumerate(content) if x == "-"]
                        #print indices
                        for i in indices:
                                st=content[:i]+'/'+content[i+1:]
                                copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
                if "/" in content:
                        indices = [i for i, x in enumerate(content) if x == "/"]
                        #print indices
                        for i in indices:
                                st=content[:i]+'-'+content[i+1:]
                                copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
                if "*" in content:
                        indices = [i for i, x in enumerate(content) if x == "*"]
                        #print indices
                        for i in indices:
                                st=content[:i]+'+'+content[i+1:]
                                copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
                if "%" in content:
                        indices = [i for i, x in enumerate(content) if x == "%"]
                        #print indices
                        for i in indices:
                                st=content[:i]+'/'+content[i+1:]
                                copy_strt()
                                f1= open(src, 'a')
                                f1.write(st)
                                copy_end()
                                f1.close()
                
           
                
        content = f.readline() 
f.close()
#print inp

for names in filelist:
	cmd = ["gcc", names, "-o", names[:-2]]
	subprocess.call(cmd)

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm
	
test_suite = []
while(len(filelist)>1):
	inputs = []
	result = []
	killed=[]
	print "Mutants",filelist[1:]
	eg.msgbox(filelist[1:], "Mutants Generated", "OK")
	for inp_var in inp:
		#print "Enter value of varible ",inp_var[0]," of type ",inp_var[1]
		x=eg.enterbox(msg="Enter value of varible "+inp_var[0]+" of type "+inp_var[1], title=' ', default='', strip=True, image=None, root=None)
		inputs.append(x)
	for i,names in enumerate(filelist):
	        process = subprocess.Popen(['./'+names[:-2]], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
		for supply_var in inputs:
			process.stdin.write(supply_var)
		
		signal.signal(signal.SIGALRM, alarm_handler)
                signal.alarm(5)  # 5 sec
                try:
                    print "running"
                    stdoutdata, stderrdata = process.communicate()
                    result.append(stdoutdata)
                    print stdoutdata
                    signal.alarm(0)  # reset the alarm
                except Alarm:
                    print "Oops, taking too long!"
                    result.append("infinite")
        
	for i,n in enumerate(result):
		if result[0]!=n and i>0:
			result[i]="Killed"
			killed.append(filelist[i])
			filelist[i]="Killed"


	test_suite.append([inputs,killed])
	filelist = filter(lambda a: a != "Killed", filelist)
	eg.msgbox(killed, "mutants killed", "OK")
	eg.msgbox("none" if len(filelist[1:])==0 else filelist[1:], "mutants left", "OK")
	print "mutants left",filelist[1:]
	if len(filelist)>1:
		choice =eg.enterbox(msg='do u wish to continue (y/n)...?? ', default='', strip=True, image=None, root=None)
		if choice.lower()=='n':
			break

print test_suite
r=""
for word in test_suite:
	r = r+"\ninput"+str(word[0])+" and Killed "+str(word[1])
if len(filelist)>1:
	r =r+ "\n Alive mutants are "+str(filelist[1:])
eg.msgbox(r, "Test Suite Generated", "OK")
