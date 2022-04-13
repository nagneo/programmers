# programmers 
# exercise for coding test
# recommend new id
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = ''
    # 1
    prosessingId = step1(new_id)
    
    # 2
    prosessingId = step2(prosessingId)
    
    # 3
    prosessingId = step3(prosessingId)
    
    # 4
    prosessingId = step4(prosessingId)
    
    # 5
    prosessingId = step5(prosessingId)
    
    # 6
    prosessingId = step6(prosessingId)

    # 7
    answer = step7(prosessingId)
    
    return answer

def step1(new_id):
    return new_id.lower();
    
def step2(new_id):
    result = re.sub('[^a-z0-9-_.]', "", new_id)
    return result
    
def step3(new_id):
    result = re.sub(r'\.+', '.', new_id)
    return result 
    
def step4(new_id):
    return new_id.strip('.')
    
def step5(new_id):
    if not new_id:
        new_id = 'a'
    return new_id

def step6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        
    return new_id.strip('.')

def step7(new_id):
    if len(new_id) > 0 and len(new_id) <= 2:
        last = new_id[-1]
        while(len(new_id) < 3):
            new_id += last
        
    return new_id

#result = solution('z-+.^.')
#result = solution('=.=')
#result = solution('123_.def')
#result = solution('abcdefghijklmn.p')
#print(result)