def solution(s):
    answer = s
    # sol1 : string to string (not int)
    answer = answer.replace('zero', '0')
    answer = answer.replace('one', '1')
    answer = answer.replace('two', '2')
    answer = answer.replace('three', '3')
    answer = answer.replace('four', '4')
    answer = answer.replace('five', '5')
    answer = answer.replace('six', '6')
    answer = answer.replace('seven', '7')
    answer = answer.replace('eight', '8')
    answer = answer.replace('nine', '9')

    # sol2
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for item in num_dict.items():
        answer = answer.replace(item[0], str(item[1]))
    return int(answer)


# 예주
def solution(s):

    s = re.sub('zero', '0', s)
    s = re.sub('one', '1', s)
    s = re.sub('two', '2', s)
    s = re.sub('three', '3', s)
    s = re.sub('four', '4', s)
    s = re.sub('five', '5', s)
    s = re.sub('six', '6', s)
    s = re.sub('seven', '7', s)
    s = re.sub('eight', '8', s)
    s = re.sub('nine', '9', s)

    return int(s)


'''
other solution
'''

''''
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

'''
