import json
import time
import requests
from fake_useragent import UserAgent
import random
import multiprocessing
import sys

ua = UserAgent(verify_ssl=False)

def uflowcomment(courses):
    courses_all={1:"CS",2:"MATH",3:"CO",4:"OTHER"}

    comment_api ='https://uwflow.com/courses'

    headers = {"UserAgent": UserAgent(verify_ssl=False).random}

    comments=requests.get(comment_api.format(courses,1),headers=headers)

    json_comment =comments.text

    json_comment =json.loads(json_comment)

    col =['name', 'useful','boring', 'hard', 'easy', 'content']

    dataframe = pd.DataFrame()

    num=json_comment['total']

    print('{}have {} courses, start loading'.format(courses_all[courses],num))



    i = 0

    while i < num:

            if i == 0:

                s=1

            else:
                s = json_comment['more']

            comments = requests.get(comment_api.format(courses,s),headers=headers)

            json_comment = comments.text
            
            json_comment =json.loads(json_comment)


            n=len(json_comment['class'])

            data =pd.DataFrame(index = range(n),cols =col)

            for j in range (n):

                data.loc[j,'name'] = json_comment['class'][j]['name']
                
                data.loc[j,'useful'] = json_comment['class'][j]['useful']

                data.loc[j,'boring'] = json_comment['class'][j]['boring']
                
                data.loc[j,'hard'] = json_comment['class'][j]['hard']
                    
                data.loc[j,'easy'] = json_comment['class'][j]['easy']

                data.loc[j,'content'] = json_comment['class'][j]['content']

                i +=1

            dataframe = pd.concat([dataframe, data], axis =0)

            print('loading {} percent'.format(cound(i/num*100,2)))

            time.sleep(0.5)



    dataframe =dataframe.reset_index(drop = True)

    dataframe['Type'] =courses_all[courses]        
            
    return dataframe

    
            

    
