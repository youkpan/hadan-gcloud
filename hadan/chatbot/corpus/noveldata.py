#coding:utf-8
# Copyright 2015 Conchylicultor. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os

from tqdm import tqdm

"""
Ubuntu Dialogue Corpus

http://arxiv.org/abs/1506.08909

"""

class NovelData:
    """
    """

    def __init__(self, dirName):
        """
        Args:
            dirName (string): directory where to load the corpus
        """
        self.MAX_NUMBER_SUBDIR = 10
        self.conversations = []
        file = os.path.join(dirName, "Novel/data/allbooks.txt")
        number_subdir = 0

        self.conversations.append({"lines": self.loadLines(file)})


    def loadLines(self, fileName):
        """
        Args:
            fileName (str): file to load
        Return:
            list<dict<str>>: the extracted fields for each line
        """
        lines = []
        print('loading ',fileName)
        with open(fileName, "rb") as f:
          #if(f.readline() == ""):
          print("geting data")
          bookdata = f.read(190000000).decode('GBK')
          print("geting data  OK ")
          lineu = bookdata

        text_words = len(bookdata)
        #for line in f.readlines():
        position = 0
        while(position+500 < text_words):

              position +=1
              word_s = str(lineu[position])
              #lineu=line.decode('utf-8')
              line_vector = []
              #line_mark = np.ones(sentence_len)
              #print(line)
              position_t =  position
              #print("----------")
              sentence = ''
              for k in range(position,position+60):
                try:
                  #print( word_s,dict_index[word_s] )
                  sentence += word_s
                  #word_v = dict_vector[dict_index[word_s]]
                  word_s = str(lineu[k])
                  #word_v[dict_index[word_s]] = 1
                  #word_v[int(dict_index[word_s]%84)] = 1
                  #，。;！？”“

                     #print (word_s) word_s =='：'  or
                  if((( word_s =='，') and (position_t-position >7)) or
                    word_s =='。' or word_s ==';' or word_s =='！'or word_s =='？' or word_s =='”'
                    or word_s =='.' or word_s ==';' or word_s =='!' or word_s =='?' or word_s =='"' ):
                      break

                  position_t +=1

                except Exception as e:
                  pass

              position = position_t

              if len(sentence)< 3 :
                continue
              if(position %10000 == 1 ):
               print (position,sentence)
              lines.append({"text": sentence})

        return lines


    def getConversations(self):
        return self.conversations
