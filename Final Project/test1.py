__author__ = "Tian Jin, Yitian Zhang, Bokai Zhuang"
import random

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
            sen = 10
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
                        less += 1
                    elif k > c_list[i]:
                        greater +=1
                    else:
                        equal +=1
            elif op_parity == "Even":
                for k in op_even:
                    if k <=c_list[i]:
                        less += 1
                    elif k > c_list[i]:
                        greater +=1
                    else:
                       equal +=1
            else:
                for k in j:
                    if k < c_list[i]:
                        less += 1
                    elif k > c_list[i]:
                        greater +=1
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

#print count_rate([1,2,3,4,5,6,7,8,9],[[1,2,3,4,5,6,7,8,9]],"Odd")
#print "this is sen:",'\n',count_sensibility([1,2,3,4,5,6,7,8,9],[[1,2,3,4,5,6,7,8,9]],"Odd")
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
            if tmp_num != []:
                if len(tmp_num) == 1:
                    op = tmp_clean
                    op.sort()
                    if op not in new_possible:
                            new_possible.append(op)
                elif len(tmp_num) == 3:
                    for k in tmp_num:
                        op = tmp_clean + tmp_num
                        op.remove(k)
                        op.sort()
                        print op
                        if op not in new_possible:
                            new_possible.append(op)
                else:
                    for k in tmp_num:
                        op = tmp_clean+[k]
                        op.sort()
                        if op not in new_possible:
                            new_possible.append(op)
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
            if tmp_num != []:
                if len(tmp_num) == 1:
                    op = tmp_clean
                    op.sort()
                    if op not in new_possible:
                            new_possible.append(op)
                elif len(tmp_num) == 3:
                    for k in tmp_num:
                        op = tmp_clean + tmp_num
                        op.remove(k)
                        op.sort()
                        if op not in new_possible:
                            new_possible.append(op)
                else:
                    for k in tmp_num:
                        op = tmp_clean+[k]
                        op.sort()
                        if op not in new_possible:
                            new_possible.append(op)
        return new_possible
    else:
        for i in op_possible:
            if y_card in i:
                i.remove(y_card)
                i.sort()
                if i not in new_possible:
                    new_possible.append(i)
        return  new_possible

def score(rate,sen):
    score_list = []
    for i in range(0,len(rate)):
        score_list.append(rate[i] * sen[i])
    return score_list


def AI(c_list,op_possible,op_parity = None):
    win_rate = count_rate(c_list,op_possible,op_parity)
    sen_rate = count_sensibility(c_list,op_possible,op_parity)
    score_list = score(win_rate,sen_rate)
    #print "c_list",c_list
    #print "win_rate",win_rate
    #print "sen_rate",sen_rate
    #print "Score:",score_list
    for i in range(0,len(c_list)):
        if score_list[i] == max(score_list):
            return c_list[i],parity(c_list[i])



def op_random(c_list):
    #print "@@@@@",c_list
    #print "this card you have now:",c_list
    re_num = random.randint(0,len(c_list)-1)
    num = c_list[re_num]
    op_parity = parity(num)
    #c_list.remove(num)
    #re_num = raw_input("Please draw a card:")
    #op_parity = parity(int(re_num))
    c_list.remove(num)
    return num,op_parity,c_list

def reverse(player):
    '''
    :param player:
    :return: the oppoiste player
    '''
    if player == "Opponent":
        c_player = "You"
        return c_player
    else:
        c_player = "Opponent"
        return c_player


def black_white():
    print '*'*22,"Start Game",'*'*22,'\n'
    y_card_list = [1,2,3,4,5,6,7,8,9]
    op_card_list = [1,2,3,4,5,6,7,8,9]
    op_possible = [[1,2,3,4,5,6,7,8,9]]
    player = "Opponent"
    player_s = 0
    op_s = 0
    for i in range(1,10):
        print '*'*20,"Round",i,"Start",'*'*20,'\n'
        print player,"go first."
        print "The current score:",player_s,':',op_s,'(you:opponent)'

        #########################################
        y_even,y_odd = seprate_list(y_card_list)
        op_even,op_odd = seprate_list(op_card_list)
        #########################################

        print "The card you have now:"
        print "Odd:",y_odd,"Even:",y_even,'\n'

        print "The number of cards opponent has:"
        print "Odd:",len(op_odd),"Even:",len(op_even)

        #print "op cards:",op_card_list
        if player == "Opponent":
            op_card,op_parity,op_card_list = op_random(op_card_list)
            print "The opponent draw a card:",op_parity,"card"
            y_card,y_parity = AI(y_card_list,op_possible,op_parity)
            print "You draw a card:",y_parity,"card ",y_card
        else:
            y_card,y_parity = AI(y_card_list,op_possible,op_parity = None)
            print "!!!!!!!!!!!!!",y_parity
            print "You draw a card first."
            print "You draw a card:",y_parity,"card ",y_card
            op_card,op_parity,op_card_list = op_random(op_card_list)
            print "The opponent draw a card:",op_parity,"card",op_card

        y_card_list.remove(y_card)
        if y_card > op_card:
            result = "win"
            print "You win this round."
            player_s += 1
        elif y_card < op_card:
            print "Opponent wins this round."
            result = "lose"
            op_s += 1
        else:
            print "This round is tie."
            result = "tie"
            player_s += 1
            op_s += 1

        op_possible = update(op_possible,y_card,op_parity,result)
        print "!!!!!!!!",op_possible
        print '*'*20,"Round",i,"End",'*'*20,'\n'
        player = reverse(player)

        if player_s > op_s and player_s == 5:
            print "Congratulations! You won! "
            print '*'*20,"The Game is End!",'*'*20,'\n'
            return "AI"
        elif op_s > player_s and op_s == 5:
            print "Congratulations! Opponent won!"
            print '*'*20,"The Game is End!",'*'*20,'\n'
            return "OP"
        elif player_s == op_s and player_s == 5:
            print "This game is tie."
            print '*'*20,"The Game is End!",'*'*20,'\n'
            return "TIE"

P_AI = 0
P_OP = 0
tie = 0
for i in range(0,100):

    result = black_white()
    if result == "AI":
        P_AI += 1
    elif result == "OP":
        P_OP += 1
    else:
        tie +=1
print "AI:",P_AI
print "OP:",P_OP
print "TIE:",tie





#if __name__ == '__main__':
