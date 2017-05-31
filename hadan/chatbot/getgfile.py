from tensorflow import gfile
from tensorflow import logging
import tensorflow as tf

  
def getfile(data_pattern):

    files = gfile.Glob(data_pattern)
    num_epochs = 1
    num_readers = 1
    for k in range(len(files)):
    	with open(files[k], "rb") as f:
    		bookdata = f.read(190000000)	
	    	print(bookdata)
    return

    
a=getfile('gs://telfordpan-hadan1-train/hadan1_20170531_132003/4ba89044aaf1c174f26bd22c530fb921dfe0431a1b2c2f9f61109fdfc239a70e/hadan-chatbot-0.0.0.tar.gz')
print(a)