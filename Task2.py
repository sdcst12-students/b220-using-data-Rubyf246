
import random
import string

######### define DM (Data Modifier) class #####################################################################
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
 
        
############ define star system class ###############
class StarSystem:
    mainworldname = ""
    size = 0  
    atm = 0
    hyd = 0
    pop = 0
    gov = 0
    law_lvl = 0
    tech_lvl = 0
    D2 = 0
    starport = 'X'
    naval_base = 'yes'
    scout_base = 'yes'
    gas_giant = "yes"
    planetoids = "yes"
    
     
    ############################# initialize a star system object (class constructor) ################################################################  
    def  __init__(self, D2):
       # print (" D2 in class: " + str(D2))
        self.mainworldname = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(6)])
            #2A find startport type:
        if D2 in [2,3,4]:
            self.starport = "A"
        elif D2 in [5,6]:  
            self.starport = 'B'
        elif D2 in [7,9]:  
            self.starport = 'C'
        elif D2 in [9]:  
            self.starport = 'D'
        elif D2 in [10,11]:  
            self.starport = 'E'
        else: 
            self.starport = 'X'
            
        #print(f"  startport is " + f"{starport}".rjust(2))   
        
        #2B find naval base:
        if D2 in [2,3,4,5,6,7]:
            self.naval_base= "no"
        else: 
            self.naval_base = 'yes'
            
        #print(f"  naval_base is " + f"{naval_base}".rjust(2))   
        
        #2c find scout type:
        if D2 in [2,3,4,5,6]:
            self.scout_base = "no"
        else:
            self.scout_base = 'yes'
            
        #print(f"  scout_base is " + f"{scout_base}".rjust(2))  
        

        
        #2d find gas giant type:
        if D2 in [2,3,4,5,6,7,8,9]:
            self.gas_giant = "yes"
        else: 
            self.gas_giant = 'no'
            
        #print(f"  gas giant is " + f"{gas_giant}".rjust(2))  
            
        #2e find planetoids type:
        if D2 in [2,3,4,5,6]:
            self.planetoids = "yes"
        else: 
            self.planetoids = 'no'    
        
   
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
        size_b4 = self.D2-2
        #print(f" size before DM is " + f"{size_b4}".rjust(2)) 
        if (size_b4 in range(16)):
            dm_size = getattr(DM_dict.get(size_b4), "size")
        else:
            dm_size = 0
        #print(f" dm_size is " + f"{dm_size}".rjust(2)) 
        self.size = size_b4 + dm_size
        #print(f" size after DM is " + f"{size}".rjust(2)) 
        
        # 5C atmosphere 2D-7, if size = 0 then atm = 0
        if (self.size == 0):
           self.atm = 0
        else:
            atm_b4 = self.D2 - 7 + self.size
            
            #print(f" atm before DM is " + f"{atm_b4}".rjust(2)) 
            if (atm_b4 in range(16)):
                dm_atm = getattr(DM_dict.get(atm_b4), "atm")
            else:    
                dm_atm = 0
            #print(f" dm_atm is " + f"{dm_atm}".rjust(2)) 
            self.atm = atm_b4 + dm_atm
            #print(f" atm after DM is " + f"{atm}".rjust(2)) 
            

        # 5D hydrographics
        hydro_b4 = D2 - 7 + self.size
        #print(f" hydro before DM is " + f"{hydro_b4}".rjust(2)) 
        if self.size == -1:
            self.hydro = 0
        elif (self.atm ==-1) or (self.atm == 10): 
            self.hydro = hydro_b4 + (-4)
        else :
            if (hydro_b4 in range(16)):
                dm_hydro = getattr(DM_dict.get(hydro_b4), "hyd")
            else :
                dm_hydro = 0    
            #print(f" dm_hydro is " + f"{dm_hydro}".rjust(2)) 
            self.hydro = hydro_b4 + dm_hydro
            #print(f" hydro after DM is " + f"{hydro}".rjust(2)) 
            
        
        if self.hydro < 0: 
            self.hydro = 0   
        if self.hydro > 10: 
            self.hydro = 10      
                    
        # 5E population
        pop_b4 = D2-2
        #print(f" gov before DM is " + f"{pop_b4}".rjust(2)) 
        if (pop_b4 in range(16)):
            dm_pop = getattr(DM_dict.get(pop_b4), "pop")
        else:
            dm_pop = 0   
        #print(f" dm_pop is " + f"{dm_pop}".rjust(2)) 
        self.pop = pop_b4 + dm_pop
        #print(f" pop after DM is " + f"{pop}".rjust(2)) 
        
        # 5F government
        gov_b4 = D2-7 + self.pop
        #print(f" gov before DM is " + f"{gov_b4}".rjust(2)) 
        if (gov_b4 in range(16)):
            dm_gov = getattr(DM_dict.get(gov_b4), "gov")
        else:
            dm_gov = 0    
        #print(f" dm_gov is " + f"{dm_gov}".rjust(2)) 
        self.gov = gov_b4 + dm_gov
        #print(f" gov after DM is " + f"{gov}".rjust(2)) 
        
        # 5G law level
        self.law_level = D2-7 + self.gov 
        #print(f" law_level is " + f"{law_level}".rjust(2)) 
        
        # 5H tech level
        dm_size = getattr(DM_dict.get(myd1), "size")
        dm_atm = getattr(DM_dict.get(myd1), "atm")
        dm_hyd = getattr(DM_dict.get(myd1), "hyd")
        dm_pop = getattr(DM_dict.get(myd1), "pop")
        dm_gov = getattr(DM_dict.get(myd1), "gov")
        self.tech_level = myd1 + dm_size + dm_atm + dm_hyd + dm_pop + dm_gov
        #print(f" tech_level is " + f"{tech_level}".rjust(2))     

####################### end of definition of star system class ##########################################



 
######################## MAIN ####################################
 
#"===========randomly generate star system objects and add to a list ==============================
star_system_list = []

for i in range(10):
    myd1 = random.randint(1,6)
    myd2 = random.randint(1,6)
    D2 = myd1 + myd2
    my_starsys = StarSystem(D2)  # create\build an object of star system class
    star_system_list.append(my_starsys)


################# print out the values of attributes of each start system in the list
for starsys in star_system_list:
    
    print ("  main world name: " + starsys.mainworldname)
    print ("      size: " + str(starsys.size))
    print ("      atm: " + str(starsys.atm))
    print ("      hyd: " + str(starsys.hyd))
    print ("      pop: " + str(starsys.pop))
    print ("      gov: " + str(starsys.gov))
    print ("      law_lvl: " + str(starsys.law_lvl))
    print ("      tech_lvl: " + str(starsys.tech_lvl))
    print ("      starport: " + starsys.starport)
    print ("      naval_base: " + starsys.naval_base)
    print ("      scout_base: " + starsys.scout_base)
    print ("      gas_giant: " + starsys.gas_giant)
    print ("      planetoids: " + starsys.planetoids)

 
        
        