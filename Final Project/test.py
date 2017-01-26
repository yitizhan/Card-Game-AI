__author__ = "Tian Jin, Yitian Zhang, Bokai Zhuang"
import  random
c_list = []
op_possible = [[1,2,3,4,5,6,7,8,9]]

def seprate_list(c_list):
    even= []
    odd = []
    for i in c_list:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
def parity(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
def get_sen(less,greater,equal,sen):
    if less == greater:
        return (less+greater+equal)*sen
    elif min(less,greater) == 0 and equal== 0:
        return  1
    else:
        return (min(less,greater)+equal)*sen

def count_sensibility(c_list,op_possible,op_parity = None):
    sen_rate = []
    for i in range(0,len(c_list)):
        sen_rate.append(0)
    for i in range(0,len(c_list)):
        if parity(i+1) == op_parity:
            sen = 20
        else:
            sen = 10
        #print "the sen for",i,"is",sen
        for j in op_possible:
            op_even,op_odd = seprate_list(j)
            less = float(0)
            greater = float(0)
            equal = float(0)
            if op_parity == "Odd":
                for k in op_odd:
                    if k < c_list[i]:
                        greater += 1
                    elif k > c_list[i]:
                        less +=1
                    else:
                        equal +=1
            elif op_parity == "Even":
                for k in op_even:
                    if k < c_list[i]:
                        greater += 1
                    elif k > c_list[i]:
                        less +=1
                    else:
                        equal +=1
            else:
                for k in j:
                    if k < c_list[i]:
                        greater += 1
                    elif k > c_list[i]:
                        less +=1
                    else:
                        equal +=1
            sen_rate[i] += get_sen(less,greater,equal,sen)
        sen_rate[i] = sen_rate[i] / len(op_possible)
    return  sen_rate

def count_rate(c_list,op_possible,op_parity = None):
    win_rate = []
    for i in range(0,len(c_list)):
        win_rate.append(0)
    for i in range(0,len(c_list)):
        for j in op_possible:
            op_even,op_odd = seprate_list(j)
            if op_parity == "Even":
                fenmu = float(len(op_even))
                fenzi = float(0)
                for k in op_even:
                    if c_list[i] >= k:
                        fenzi += 1
                rate = fenzi / fenmu
            elif op_parity == "Odd":
                fenmu = float(len(op_odd))
                fenzi = float(0)
                for k in op_odd:
                    if c_list[i] >= k:
                        fenzi += 1
                rate = fenzi / fenmu
            else:
                fenmu = float(len(j))
                fenzi = float(0)
                for k in j:
                    if c_list[i] >= k:
                        fenzi += 1
                rate = fenzi / fenmu
            win_rate[i] += rate
        win_rate[i] = win_rate[i] / len(op_possible)
    return win_rate

###update

def update(op_possible,y_card,op_parity,result):
    new_possible = []
    if result == "win":
        for i in op_possible:
            tmp = i
            tmp_num = []
            tmp_clean = []
            for j in tmp:
                if parity(j) == op_parity and j < y_card:
                    tmp_num.append(j)
                else:
                    tmp_clean.append(j)
            for k in tmp_num:
                new_possible.append(tmp_clean+[k])
        return new_possible
    elif result == "lose":
        for i in op_possible:
            tmp = i
            tmp_num = []
            tmp_clean = []
            for j in tmp:
                if parity(j) == op_parity and j > y_card:
                    tmp_num.append(j)
                else:
                    tmp_clean.append(j)
            for k in tmp_num:
                new_possible.append(tmp_clean+[k])
        return new_possible
    else:
        for i in op_possible:
            i.remove(y_card)
        return  op_possible

def score(rate,sen):
    score_list = []
    for i in rate:
        for j in sen:
            s = i * j
        score_list.append(s)
    return score_list

rate = count_rate([1,2,3,4,5,6,7,8,9],[[1,2,3,4,5,6,7,8,9]],"Odd")
sen = count_sensibility([1,2,3,4,5,6,7,8,9],[[1,2,3,4,5,6,7,8,9]],"Odd")
print "!!",rate
print "!!",sen
print score(rate,sen)

def AI(c_list,op_possible,op_parity = None):
    win_rate = count_rate(c_list,op_possible,op_parity)
    sen_rate = count_sensibility(c_list,op_possible,op_parity)
    score_list = score(win_rate,sen_rate)
    for i in c_list:
        for j in score_list:
            if j == max(score_list):
                return i

print "!!!"
test = [1,2,3,4,5,6,7]
print len(test)
print random.randint(0,2)

print max([0.1,0.2,0.3])

op_possible = update(op_possible,5,"Even","win")
#print op_possible

op_possible = update(op_possible,7,"Odd","tie")
#print op_possible
#test = [1,2,3,4,5,6,7,8]
#print len(test)
#for i in range(0,len(test)):
#    if test[0] < 3:
#        test.remove(test[i])
#    print test


#test = [1,2,3,4,5,6,7,8]
#print len(test)

length = len(test)

#print cmp(3,2)
