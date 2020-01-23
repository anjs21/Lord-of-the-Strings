import json
import random
import os
def selection(n,k):
    temp = [i for i in range(1,n+1)]
    reserve = [i for i in range(1,k+1)]
    for i in range(k+1,n+1):
        j = random.randint(1,i)-1
        i-=1
        if j<k:
           reserve[j] = temp[i];
    return reserve
def initialise():
    iterations = int(input())
    
    number_of_cops = 74
    number_of_spy = 3

    distance = 25 

    dir_name = 'Configurations'
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    data = {}
    with open('pravega.txt') as json_file:
        data = json.load(json_file) 
    
    page_number = 1

    for i in range(iterations):

        random_number = random.randint(1,9)

        filename = 'config_' + str(page_number) +'.txt'
        page_number+=1
        
        filename_json = open(os.path.join(os.getcwd(),dir_name,filename),'w')
        
        if random_number == 1:
            sel_cops = selection(74,number_of_cops)
            sel_spy = selection(74,number_of_spy)

            position_cops = [75-i for i in sel_cops]
            position_spy = [125+i for i in sel_spy]
             
            cops =[random.choice(data[str(i)]) for i in position_cops]
            spy =[random.choice(data[str(i)]) for i in position_spy]
            
            config = (cops,spy)

            json.dump(config,filename_json)
        else:
            sel_cops = [random.randint(1,74) for _ in range(number_of_cops)]
            sel_spy = [random.randint(1,74) for _ in range(number_of_spy)]

            #print(sel_cops)
            #print(sel_spy)

            position_cops = [75-i for i in sel_cops]
            position_spy = [125+i for i in sel_spy]

            #print(position_cops)
            #print(position_spy)

            freq_cops={}
            freq_spy={}
            for i in position_cops:
                try:
                    freq_cops[i]+=1
                except:
                    freq_cops[i]=1
            for i in position_spy:
                try:
                    freq_spy[i]+=1
                except:
                    freq_spy[i]=1

            #print(freq_cops)
            #print(freq_spy)

            cops =[]
            spy =[]        
            
            for i in freq_cops:
                count = freq_cops[i]
                if count > 1:
                    number=selection(len(data[str(i)]),count)
                    #print(number)
                    for j in number:
                        cops.append(data[str(i)][j-1])
                else:
                    cops.append(random.choice(data[str(i)]))
            
            for i in freq_spy:
                count = freq_spy[i]
                if count >1:
                    number=selection(len(data[str(i)]),count)
                    #print(number)
                    for j in number:
                        spy.append(data[str(i)][j-1])
                else:
                    spy.append(random.choice(data[str(i)]))
            config = (cops , spy)

            json.dump(config,filename_json)

initialise()

