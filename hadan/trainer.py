from hadan.chatbot import chatbot
import subprocess
import time

tmp_path = './'
#files = 'gs://hadan-data/data.tar.xz'
furl = 'gs://hadan-data/data14.tar.xz'
#or use wget : https://storage.googleapis.com/hadan-data/data14.tar.xz
saveurl = 'gs://hadan-data/save-14-1536.tar.xz'
idSample = 0

try:
    import random
    idSample = random.randint(0, 10000)
    subprocess.check_call(['ls', '-hl']  )
except Exception as e:
    pass 


try:
    subprocess.check_call(['gsutil','cp' ,furl ,'.' ])
    pass
except Exception as e:
    pass 

try:
    subprocess.check_call(['tar', '-Jxf' ,'data14.tar.xz'] )
except Exception as e:
    pass 

time.sleep(5)  
try:
    subprocess.check_call(['mkdir', 'save']  )
except Exception as e:
    pass    
 
try:
    subprocess.check_call(['gsutil','cp' ,saveurl ,'.' ])
    pass
except Exception as e:
    pass 

try:
    subprocess.check_call(['tar', '-Jxf' ,'save-14-1536.tar.xz'] )
except Exception as e:
    pass 

time.sleep(5)  
'''    
try:
    #subprocess.check_call(['tar', 'xf' , 'save.tar'] )
except Exception as e:
    pass 

time.sleep(5)  

try:
    print('saving to backup ')
    subprocess.check_call(['gsutil', 'cp' , '-r', 'gs://hadan-data/save' ,'.' ]  )
    print('saving to backup ok')
except Exception as e:
    pass    
'''
time.sleep(5)


chatbot = chatbot.Chatbot()
chatbot.main()


try:
    subprocess.check_call(['tar', 'cf' , 'save.tar' , 'save'  ]  )
except Exception as e:
    pass 
    
try:
    subprocess.check_call(['xz', '-z' , 'save.tar'] )
except Exception as e:
    pass 
    
   
try:
    subprocess.check_call(['gsutil', 'cp' , 'save.tar.xz' ,'gs://hadan-data/21' ]  )
except Exception as e:
    pass 
    
