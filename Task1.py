import random
import string


    ######### define DM class #############
    # define a class
class DM:
    size = 0  
    atm = 0
    hyd = 0
    pop = 0
    gov = 0
    def __init__(self, size, atm, hyd, pop, gov):
        self.size = size
        self.atm = atm
        self.hyd = hyd
        self.pop = pop
        self.gov = gov
        
class UPP:
    size = 0  
    atm = 0
    hyd = 0
    pop = 0
    gov = 0
    law_lvl = 0
    tech_lvl = 0
    def __init__(self, size, atm, hyd, pop, gov, law_lvl, tech_lvl):
        self.size = size
        self.atm = atm
        self.hyd = hyd
        self.pop = pop
        self.gov = gov
        self.law_lvl = law_lvl
        self.tech_lvl = tech_lvl
    
upp_dict = {}       

#print("To get the sum of 2 dice:")
 

for i in range(10):
    myd1 = random.randint(1,6)
    myd2 = random.randint(1,6)
    D2 = myd1 + myd2
    #print(f"  D2 is " + f"{D2}".rjust(2))
    
    #2A find startport type:
    if D2 in [2,3,4]:
        starport = "A"
    elif D2 in [5,6]:  
        starport = 'B'
    elif D2 in [7,9]:  
        starport = 'C'
    elif D2 in [9]:  
        starport = 'D'
    elif D2 in [10,11]:  
        starport = 'E'
    else: 
        starport = 'X'
        
    #print(f"  startport is " + f"{starport}".rjust(2))   
    
     #2B find naval base:
    if D2 in [2,3,4,5,6,7]:
        naval_base= "no"
    else: 
        naval_base = 'yes'
        
    #print(f"  naval_base is " + f"{naval_base}".rjust(2))   
    
    #2c find scout type:
    if D2 in [2,3,4,5,6]:
        scout_base = "no"
    else:
        scout_base = 'yes'
        
    #print(f"  scout_base is " + f"{scout_base}".rjust(2))  
    

    
    #2d find gas giant type:
    if D2 in [2,3,4,5,6,7,8,9]:
        gas_giant = "yes"
    else: 
        gas_giant = 'no'
        
    #print(f"  gas giant is " + f"{gas_giant}".rjust(2))  
          
    #2e find planetoids type:
    if D2 in [2,3,4,5,6]:
        planetoids = "yes"
    else: 
        planetoids = 'no'
        
    #print(f" planetoids is " + f"{planetoids}".rjust(2))  
    
    #3 generate a random name for the main world
    #step1 generate random integer between 1 and 999 
    mainworldname = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(6)])
    #print(f" mainworldname is " + f"{mainworldname}".rjust(2))  
    
    ############# build a dictionary for DMs ############
    
    dm0 = DM(2, 1, 0, 0, 1)
    dm1 = DM(2, 1, 0, 1, 0)
    dm2 = DM(1, 1, 0, 1, 0)
    dm3 = DM(1, 1, 0, 1, 0)
    dm4 = DM(1, 0, 0, 1, 0)
    dm5 = DM(0, 0, 0, 1, 1)
    dm6 = DM(0, 0, 0, 0, 0)
    dm7 = DM(0, 0, 0, 0, 0)
    dm8 = DM(0, 0, 0, 0, 0)
    dm9 = DM(0, 0, 1, 2, 0)
    dm10 = DM(0, 1, 2, 4, 0)
    dm11 = DM(0, 1, 0, 0, 0)
    dm12 = DM(0, 1, 0, 0, 0)
    dm13 = DM(0, 0, 1, 0, -2)
    dm14 = DM(0, 1, 0, 0, 0)
    dm15 = DM(0, 0, 0, 0, 0)
    dm16 = DM(-4, 0, 0, 0, 0)
    
    DM_dict = {
        0: dm0, 
        1: dm1,
        2: dm2, 
        3: dm3,
        4: dm4,
        5: dm5,
        6: dm6,
        7: dm7,
        8: dm8,
        9: dm9,
        10: dm10,
        11: dm11,
        12: dm12,
        13: dm13,
        14: dm14,
        15: dm15,
        16: dm16
    }
    
    # 5B main work size 2D-2
    size_b4 = D2-2
    #print(f" size before DM is " + f"{size_b4}".rjust(2)) 
    if (size_b4 in range(16)):
        dm_size = getattr(DM_dict.get(size_b4), "size")
    else:
        dm_size = 0
    #print(f" dm_size is " + f"{dm_size}".rjust(2)) 
    size = size_b4 + dm_size
    #print(f" size after DM is " + f"{size}".rjust(2)) 
    
    # 5C atmosphere 2D-7, if size = 0 then atm = 0
    if (size == 0):
        atm = 0
    else:
        atm_b4 = D2 - 7 + size
        
        #print(f" atm before DM is " + f"{atm_b4}".rjust(2)) 
        if (atm_b4 in range(16)):
            dm_atm = getattr(DM_dict.get(atm_b4), "atm")
        else:    
            dm_atm = 0
        #print(f" dm_atm is " + f"{dm_atm}".rjust(2)) 
        atm = atm_b4 + dm_atm
        #print(f" atm after DM is " + f"{atm}".rjust(2)) 
        

    # 5D hydrographics
    hydro_b4 = D2 - 7 + size
    #print(f" hydro before DM is " + f"{hydro_b4}".rjust(2)) 
    if size == -1:
        hydro = 0
    elif (atm ==-1) or (atm == 10): 
        hydro = hydro_b4 + (-4)
    else :
        if (hydro_b4 in range(16)):
            dm_hydro = getattr(DM_dict.get(hydro_b4), "hyd")
        else :
            dm_hydro = 0    
        #print(f" dm_hydro is " + f"{dm_hydro}".rjust(2)) 
        hydro = hydro_b4 + dm_hydro
        #print(f" hydro after DM is " + f"{hydro}".rjust(2)) 
        
    
    if hydro < 0: 
        hydro = 0   
    if hydro > 10: 
        hydro = 10      
                
    # 5E population
    pop_b4 = D2-2
    #print(f" gov before DM is " + f"{pop_b4}".rjust(2)) 
    if (pop_b4 in range(16)):
        dm_pop = getattr(DM_dict.get(pop_b4), "pop")
    else:
        dm_pop = 0   
    #print(f" dm_pop is " + f"{dm_pop}".rjust(2)) 
    pop = pop_b4 + dm_pop
    #print(f" pop after DM is " + f"{pop}".rjust(2)) 
    
    # 5F government
    gov_b4 = D2-7 + pop
    #print(f" gov before DM is " + f"{gov_b4}".rjust(2)) 
    if (gov_b4 in range(16)):
        dm_gov = getattr(DM_dict.get(gov_b4), "gov")
    else:
        dm_gov = 0    
    #print(f" dm_gov is " + f"{dm_gov}".rjust(2)) 
    gov = gov_b4 + dm_gov
    #print(f" gov after DM is " + f"{gov}".rjust(2)) 
    
    # 5G law level
    law_level = D2-7 + gov 
    #print(f" law_level is " + f"{law_level}".rjust(2)) 
    
    # 5H tech level
    dm_size = getattr(DM_dict.get(myd1), "size")
    dm_atm = getattr(DM_dict.get(myd1), "atm")
    dm_hyd = getattr(DM_dict.get(myd1), "hyd")
    dm_pop = getattr(DM_dict.get(myd1), "pop")
    dm_gov = getattr(DM_dict.get(myd1), "gov")
    tech_level = myd1 + dm_size + dm_atm + dm_hyd + dm_pop + dm_gov
    #print(f" tech_level is " + f"{tech_level}".rjust(2)) 
    
    # construct object of class UPP 
    upp = UPP(size, atm, hydro, pop, gov, law_level, tech_level)
    
    # add object upp to dictionary
    upp_dict[mainworldname] = upp

print ("=================================================")    
    
for key, value in zip(upp_dict.keys(), upp_dict.values()):
        print(f" main word name " + f"{key}" )
        my_upp = value
        print ("                        size: " + str(getattr(my_upp, 'size')))
        ######### atm, hyd, pop, gov, law_lvl, tech_lvl)
        print ("                        atm: " + str(getattr(my_upp, 'atm')))
        print ("                        hyd: " + str(getattr(my_upp, 'hyd')))
        print ("                        pop: " + str(getattr(my_upp, 'pop')))
        print ("                        gov: " + str(getattr(my_upp, 'gov')))
        print ("                        law_lvl: " + str(getattr(my_upp, 'law_lvl')))
        print ("                        tech_lvl: " + str(getattr(my_upp, 'tech_lvl')))
        
        
        