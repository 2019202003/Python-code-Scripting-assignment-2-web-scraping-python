import random



io_bat={}
io_bowl={}
io_wicket={}
io_all={}
overs_bat={}
overs_bowl={}
overs_wicket={}
overs_all={}
len_i_bat=0
len_i_ball=0
len_i_wk=0
len_i_al=0

with open('dataset.txt') as f:
    z = f.readlines()
z.sort(reverse = True,key = lambda x:x.split(':')[3])
a = []
l = []
for i in z:
    t = i.split(':')[0]
    if t not in l:
        a.append(i)
        l.append(t)
with open('sorted_ipl_auctions_dataset.txt','w') as f:
    for i in a:
        f.write(i)
f.close()

file = open("sorted_ipl_auctions_dataset.txt","r")
for line in file:
    fields = line.split(":")
    name = fields[0]
    country = fields[1]
    role = fields[2]
    price = fields[3]
    price = price.rstrip('\n')
   
    if(role=='Batsman'):
            lis=[role,price,country]
            io_bat[name]=lis
    elif(role=='Bowler'):
             lis=[role,price,country]
             io_bowl[name]=lis
    elif(role=='Wicket Keeper'):
             lis=[role,price,country]
             io_wicket[name]=lis
    elif(role=='All-Rounder'):
             lis=[role,price,country]
             io_all[name]=lis
    elif(country!='India'):
        if(role=='Batsman'):
            bm=[country,price,role]
            overs_bat[name]=bm
        elif(role=='Bowler'):
            bm=[country,price,role]
            overs_bat[name]=bm
        elif(role=='Wicket Keeper'):
            bm=[country,price,role]
            overs_bat[name]=bm
        elif(role=='All-Rounder'):
            bm=[country,price,role]
            overs_bat[name]=bm


print(io_wicket)
f= open("Chennai Super Kings.txt","w+")
f.write("Team: Chennai Super Kings\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     """
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]"""
                        
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                '''
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                   
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
            """                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")"""
             
        n=n-1
        f.write("\n")
f.close()

f= open("Delhi Capitals.txt","w+")
f.write("Team: Delhi Capitals\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     """
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]"""
                        
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                '''
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                   
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
            """                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")"""
             
        n=n-1
        f.write("\n")
f.close()
f= open("Kings XI Punjab.txt","w+")
f.write("Team: Kings XI Punjab\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     """
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]"""
                        
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                '''
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                   
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
            """                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")"""
             
        n=n-1
        f.write("\n")
f.close()
f= open("Kolkata Knight Riders.txt","w+")
f.write("Team: Kolkata Knight Riders\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            '''
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]'''
                     
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]"""
                        
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
            '''      
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            '''
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]'''
                                    
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")
             
        n=n-1
        f.write("\n")
f.close()




f= open("Mumbai Indians.txt","w+")
f.write("Team: Mumbai Indians\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                      
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                 
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                                    
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")
             
        n=n-1
        f.write("\n")
f.close()

print('RAJASTHAN')
f= open("Rajasthan Royals.txt","w+")
f.write("Team: Rajasthan Royals\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
#print(io_bat)
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]"""
                     
                        
            if(country=='India'):
                     #continue
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        #print('bat'+str(i))
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                       
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        print(i)
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            '''
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                 
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print('jjj')
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                '''
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]'''
                                    
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")
             
        n=n-1
        f.write("\n")
f.close()


f= open("Royal Challengers Bangalore.txt","w+")
f.write("Team: Royal Challengers Bangalore\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
#print(io_bat)
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]"""
                     
                        
            if(country=='India'):
                     #continue
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        print('bat'+str(i))
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                       
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        print(i)
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            '''
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                 
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print('jjj')
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                '''
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]'''
                                    
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")
             
        n=n-1
        f.write("\n")
f.close()

print('sunrise')
print(io_bat)



f= open("Sunrisers Hyderabad.txt","w+")
f.write("Team: Sunrisers Hyderabad\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
#print(io_bat)
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     """
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            """
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]"""
                        
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                '''
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                   
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                                     
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")
             
        n=n-1
        f.write("\n")
f.close()











"""

f= open("Rajasthan Royals.txt","w+")
f.write("Team: Rajasthan Royals\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            '''
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]'''
                     
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                        
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
            '''      
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            '''
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]'''
                                    
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")
             
        n=n-1
        f.write("\n")
f.close()
"""
"""
f= open("Royal Challengers Bangalore.txt","w+")
f.write("Team: Royal Challengers Bangalore\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                        
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                '''
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                   
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                        
            
        m=m-1
        f.write("\n")
        print(i)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                                   
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")
             
        n=n-1
        f.write("\n")
f.close()"""




"""

f= open("Delhi Capitals.txt","w+")
f.write("Team: Delhi Capitals\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            '''if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                  '''   
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            ''' if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]'''
                         
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
            '''              
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     #del io_all[name]
            '''              
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     #del io_all[name]
                     f.write("\n")'''
           
        n=n-1
        f.write("\n")
f.close()

f= open("Kings XI Punjab.txt","w+")
f.write("Team: Kings XI Punjab\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            '''if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                  '''   
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            ''' if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]'''
                         
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
            '''              
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]'''
                        
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     #del io_all[name]
            '''              
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     #del io_all[name]
                     f.write("\n")'''
           
        n=n-1
        f.write("\n")
f.close()

f= open("Kolkata Knight Riders.txt","w+")
f.write("Team: Kolkata Knight Riders\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
            '''               
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]'''
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     #del io_wicket[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     #del io_wicket[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     #del io_all[name]
                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     #del io_all[name]
                     f.write("\n")
            
        n=n-1
        f.write("\n")
f.close()

f= open("Mumbai Indians.txt","w+")
f.write("Team: Mumbai Indians\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        print('aa')
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        print('bb')
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            
        m=m-1
        f.write("\n")
        print('cc')
        print(i)
        pp=len(io_all)
        print(io_all)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India' and i<=r_ov):
                #print(name)
                #if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                
            '''            
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     print(name)
                     print('home')
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")'''
            
        n=n-1
        print('good')
        f.write("\n")
f.close()

f= open("Rajasthan Royals.txt","w+")
f.write("Team: Rajasthan Royals\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        print('aa')
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        print('bb')
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            
        m=m-1
        f.write("\n")
        print('cc')
        print(i)
        pp=len(io_all)
        print(io_all)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India' and i<=r_ov):
                #print(name)
                #if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                
            '''            
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     print(name)
                     print('home')
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")'''
            
        n=n-1
        print('good')
        f.write("\n")
f.close()
f= open("Royal Challengers Bangalore.txt","w+")
f.write("Team: Royal Challengers Bangalore\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        print('aa')
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        print('bb')
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            
        m=m-1
        f.write("\n")
        print('cc')
        print(i)
        pp=len(io_all)
        print(io_all)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India' and i<=r_ov):
                #print(name)
                #if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                
                         
            '''            
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     print(name)
                     print('home')
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")'''
            
        n=n-1
        print('good')
        f.write("\n")
f.close()
f= open("Sunrisers Hyderabad.txt","w+")
f.write("Team: Sunrisers Hyderabad\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     
                     del io_bat[name]
                     
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     del io_bat[name]
                         
            
        j=j-1
        f.write("\n")
        print('aa')
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     del io_bowl[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        print('bb')
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print('outside')
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     del io_wicket[name]
                         
            
        m=m-1
        f.write("\n")
        print('cc')
        print(i)
        pp=len(io_all)
        print(io_all)
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India' and i<=r_ov):
                #print(name)
                #if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                
                         
            '''            
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     print(name)
                     print('home')
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     del io_all[name]
                     f.write("\n")'''
            
        n=n-1
        print('good')
        f.write("\n")
f.close()











'''f= open("Chennai Super Kings.txt","w+")
f.write("Team: Chennai Super Kings\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            
        n=n-1
        f.write("\n")
f.close()

f= open("Kolkata Knight.txt","w+")
f.write("Team: Kolkata Knight Riders\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
           
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
                         
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            #print(n)
            name,desc = random.choice(list(io_all.items()))
            print(name)
            salary=desc[1]
            country=desc[2]
            
                #else:
                    #break
                         
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     print('sss')
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            elif(country!='India'):
                #print(i)
                if(i<=r_ov):
                     #print(i)
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     i=i+1
                     print('ppp')
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                else:
                    continue
            
        n=n-1
        print('before')
        f.write("\n")
print('CLOSING')
f.close()

f= open("Kolkata.txt","w+")
f.write("Team: Kolkata Knight Riders\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
           
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
                         
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            #print(n)
            name,desc = random.choice(list(io_all.items()))
            print(name)
            salary=desc[1]
            country=desc[2]
            
                #else:
                    #break
                         
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     print('sss')
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            elif(country!='India'):
                #print(i)
                if(i<=r_ov):
                     #print(i)
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     i=i+1
                     print('ppp')
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                else:
                    continue
            
        n=n-1
        print('before')
        f.write("\n")
print('CLOSING')
f.close()

print('1111111111111111')

f= open("Kolkata Knight Riders.txt","w+")
f.write("Team: Kolkata Knight Riders\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
           
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            
                         
            if(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            
                         
            if(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
            elif(country!='India'):
                
                if(i<=r_ov):
                     
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     i=i+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            #print(n)
            name,desc = random.choice(list(io_all.items()))
            print(name)
            salary=desc[1]
            country=desc[2]
            
                #else:
                    #break
                         
            if(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     print('sss')
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            elif(country!='India'):
                #print(i)
                if(i<=r_ov):
                     #print(i)
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     #print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     i=i+1
                     print('ppp')
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                else:
                    continue
            
        n=n-1
        print('before')
        f.write("\n")
print('CLOSING')
f.close()































#with open('Mumbai Indians.txt') as f:
f= open("Mumbai Indians.txt","w+")
f.write("Team: Mumbai Indians\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            
        n=n-1
        f.write("\n")
f.close()
f.close()

f= open("Rajasthan Royals.txt","w+")
f.write("Team: Rajasthan Royals\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            
        n=n-1
        f.write("\n")
f.close()
print('9999999999999')
f= open("Royal Challengers Bangalore.txt","w+")
f.write("Team: Royal Challengers Bangalore\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            
        n=n-1
        f.write("\n")
f.close()
f= open("Sunrisers Hyderabad.txt","w+")
f.write("Team: Sunrisers Hyderabad\n")
f.write("\n")
over=0
r_ov=random.randint(4,7)
r_bat=random.randint(5,7)
r_bo=random.randint(4,6)
r_wk=random.randint(1,2)
r_all=random.randint(2,4)
tot=0
i=1
j=1
k=1
m=1
n=1
while(tot!=18):
    r_ov=random.randint(4,7)
    r_bat=random.randint(5,7)
    r_bo=random.randint(4,6)
    r_wk=random.randint(1,2)
    r_all=random.randint(2,4)
    tot=r_bat+r_bo+r_wk+r_all
    if(tot==18):
        print(r_ov)
        print(r_bat)
        print(r_bo)
        print(r_wk)
        print(r_all)
        while(j<=r_bat):
            #print("bat"+str(j))
            #f.write("\n")
            name,desc = random.choice(list(io_bat.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Batsman\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     j=j+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        j=j-1
        f.write("\n")
        while(k<=r_bo):
            #print("ball"+str(k))
            #f.write("\n")
            name,desc = random.choice(list(io_bowl.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     #k=k+1
                     salary=int(salary)
                     f.write("Player "+str(j+k))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Bowler\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     k=k+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            #k=k+1
        k=k-1
        f.write("\n")
        while(m<=r_wk):
            #print("wk"+str(m))
            #f.write("\n")
            name,desc = random.choice(list(io_wicket.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     #m=m+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     
                     salary=int(salary)
                     f.write("Player "+str(j+k+m))
                     f.write("\n")
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : Wicket Keeper\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     m=m+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            
        m=m-1
        f.write("\n")
        while(n<=r_all):
            #print("all"+str(n))
            #f.write("\n")
            name,desc = random.choice(list(io_all.items()))
            salary=desc[1]
            country=desc[2]
            if(country!='India'):
                
                if(i<=r_ov):
                     i=i+1
                     salary=int(salary)
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     f.write("Name : "+name)
                     print(name)
                     f.write("\n")
                     f.write("Country "+country)
                     f.write("\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         
            elif(country=='India'):
                     salary=int(salary)
                     
                     f.write("Player "+str(j+k+m+n))
                     f.write("\n")
                     #print(name)
                     f.write("Name : "+name)
                     f.write("\n")
                     f.write("Country : India\n")
                     f.write("Ability : All-Rounder\n")
                     f.write("Fees : "+str(salary))
                     f.write("\n")
                     f.write("\n")
                     n=n+1
                     if name in io_bat:
                         #del io_bat[name]
                     if name in io_bowl:
                         #del io_bowl[name]
            
                     if name in io_wicket:
                         #del io_wicket[name]
            
                     if name in io_all:
                         #del io_all[name]
                         f.write("\n")
            
        n=n-1
        f.write("\n")
f.close()
'''
"""