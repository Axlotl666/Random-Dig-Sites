#randomizes JWE dinosaur selection, skins and genes.

#add toggle for canon skins?

import random
import sys

mode='R'
num=int(sys.argv[1])
try: 
    mode=sys.argv[2] #if none, only adds random defaults to balanced.
except:
    mode='Balanced'
#num=200
#print(num)

cap=num

if cap>103:
    cap=103

tierdistro=[10,12,17,19,19,16,10] #UPDATE WITH NEW DLC
tiertally=[1,0,0,0,0,0,0]

#List that decides dinosaur tiers in park by number of total species desired.
#tls=[0,1,2,3,4,5,3,4,2,5,1,3,4,5,2,3,4,3,2,1,2,4,3,5,1,3,2,4,5,0,3,1,2,4,5,3,3,1,4,4,5,4,3,2,1,0,1,2,3,4,5,4,3,2,1,0,1,2,3,4,5,4,3,2,1,0,1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,3,4,5,4,3,5,3,5,3,5,3,5,3,5,3]
tls=[0,1,2,3,4,5,6]
tls2=[0,1,2,3,4,5,6]
while len(tls)<cap:
    tls=tls+tls2
#traditional type distro based on JP novel/film and a bit of JWorld
#tradition=['LC','ceratopsian','sauropod','Orn','SH','SC','SC','pterosaur','stegosaurid','Orn','small','small','MC','ankylosaurid','SC','small','MC','Aq','SH','SH','medium','large','ceratopsian','pterosaur','LC','sauropod','ceratopsian','SC','SC','ceratopsian','LC','ceratopsian','sauropod','Orn','SH','SC','SC','SC','pterosaur','stegosaurid','Orn','small','small','MC','small','ankylosaurid','MC','Aq','SH','SH','medium','large','ceratopsian','pterosaur','LC','sauropod','ceratopsian','SC','SC','ceratopsian']
tradition=['LC','ceratopsian','sauropod','Orn','SC','SH','SC','pterosaur','stegosaurid','MC','small','medium','small','Orn','SM','ankylosaurid','SC','ceratopsian','Aq','SH','pterosaur','LC','MC','sauropod','medium','small','large','SH','SC','Orn','LC','ceratopsian','sauropod','Orn','SC','SH','SC','pterosaur','stegosaurid','MC','small','medium','small','Orn','SM','ankylosaurid','SC','ceratopsian','Aq','SH','pterosaur','LC','MC','sauropod','medium','small','large','SH','SC','Orn']
#roster by dino types in game
balance=['pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','pliosaurid','primitive','ornithomimid','pachy','ornithopod','raptor','spinosaurid','mosasaurid','ceratosaurid','hybrid','ichthyosaurid','pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','pterosaur','sauropod','ceratopsian','pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','plesiosaurid','primitive','ornithomimid','pachy','pterosaur','sauropod','ceratopsian','carnosaur','ankylosaurid','coelurosaur','hadrosaur','stegosaurid','pliosaurid','primitive','ornithomimid','pachy','ornithopod','raptor','spinosaurid','mosasaurid','ceratosaurid','hybrid']

skins=['SD','DV','GSD','CV','SH','LR','QM','YR','Sv','AR','MF','GRB']
patterns=['Ra','Ch','Li','Pu','Pa','Pe']

#check tls numbers
#n0=0
#n1=0
#n2=0
#n3=0
#n4=0
#n5=0
#for i in tls:
#    if i == 0:
#        n0+=1
#    elif i == 1:
#        n1+=1
#    elif i == 2:
#        n2+=1
#    elif i == 3:
#        n3+=1
#    elif i == 4:
#        n4+=1
#    elif i == 5:
#        n5+=1
#print(n0,n1,n2,n3,n4,n5)

#alphabet mode base
alphabet={}

#store dino data here
dinodict={}

#open csv file with raw data, add to list for now
templist=[]
f=open('JWEstats.csv')
for line in f.readlines():
    #print(line)
    templist.append(line.split('\n')[0].split(','))
f.close()

#open config

ban=[]
force=[]
#cap=15
name='run1.txt'
f=open('config.txt')
blank=False
for line in f.readlines():
    if line[0] != '#' and line != '\n':
        l2=line.split(':')
        #print(l2)
        if l2[0] == 'MODE':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                mode=l2[1].split('\n')[0]
        if l2[0] == 'NAME':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                name=l2[1].split('\n')[0]+'.txt'
        if l2[0] == 'TARGET':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                #cap=int(l2[1].split('\n')[0])
        if l2[0] == 'BANLIST':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                l2a=l2[1].split('\n')[0]
                l3=l2a.split(',')
                ban=l3
        if l2[0] == 'FORCED':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                l2a=l2[1].split('\n')[0]
                l3=l2a.split(',')
                force=l3
        if l2[0] == 'BLANK':
            if len(l2[1])>0:
                if l2[1][0]==' ':
                    l2[1]=l2[1][1:]
                if l2[1] == 'True' or l2[1] == 'true' or l2[1] == 'True\n' or l2[1] == 'true\n':
                    blank=True                  
f.close()

if ban == ['']:
    ban =[]

if blank: #if blank pattern has been allowed, add to pattern list
    patterns.append('Bl')
    
#extract data header
headers=templist[0]
templist.pop(0)
#print(headers)

inspec=[]
inspec2=[]

#make and populate dictionary
list2=[]
for entry in templist:
    list2.append(entry)
for entry in templist:
    for banned in ban: #do banned here, or perform on dict?
        #print(banned)
        if banned in entry:
            z=0
            for forced in force:
                if forced in entry and forced != '':
                    z=1
            if z == 0:
                list2.remove(entry)
for entry in list2: 
    dinodict[entry[0]]={}
    if entry[0][0] not in alphabet:
        alphabet[entry[0][0]]=0
    for x in range(len(headers)):
        dinodict[entry[0]][headers[x]]=entry[x]  

for keys in list2:
    key=keys[0]
    canons=dinodict[key]['CANONICITY'].split(';')
    #print(canons)
    for banned in ban:
        if banned in canons:
            z=0
            for forced in force:
                if forced in canons and forced != '':
                    z=1
            if z == 0:
                try:
                    del dinodict[key]
                except:
                    nope='already removed'
                    
for key in dinodict:
    #print(key)
    gen=[]
    nums=int(dinodict[key]['GENES'])
    #print(key,nums)
    genb2=[0,0,0,0,0,0,0,0,0,0]
    for j in range(nums):
        k=random.randint(0,9)
        if genb2[k] < 3:
            genb2[k]+=1
        else:
            l=0
            while l == 0:
                k2=random.randint(0,9)
                if genb2[k2] < 3:
                    genb2[k2]+=1
                    l=1
    for gene in genb2:
        if gene == 0:
            gen.append('A')
        elif gene == 1:
            gen.append('C')
        elif gene == 2:
            gen.append('G')
        elif gene == 3:
            gen.append('T')
    #print(gen)
    geni=('').join(gen)
    dinodict[key]['GENOME']=geni[0:4]+' '+geni[4:7]+' '+geni[7:10]
    skin2=[]
    pat=random.choice(patterns)
    for sk in skins:
        if sk != '':
            skin2.append(sk+'/'+pat)
    for sk in dinodict[key]['SKINS'].split(';'):
        if sk != '':
            skin2.append(sk)
    dinodict[key]['COSMETIC']=random.choice(skin2)

#print(dinodict)      
keys2=(list(dinodict))       

random.shuffle(keys2)
#print(keys)

keys=[]
for key in keys2:
    if dinodict[key]['CLASS']!='hybrid':
        keys.append(key)

# generate species list with F species
species=[]
#for tier in tls[0:cap]:
#    for key in keys:
#        if int(dinodict[key]['TIER'])==tier and key not in species:
#            species.append(key)
#            break
##print(species)

#filter these further based on banlist and forced
bal2=balance[0:cap]
trad2=tradition[0:cap]

def reroll(currenttier,ti):
                if ti == 0:
                    R=random.randint(0,2)
                    #print(R)
                elif ti == 1:
                    R=random.randint(-1,2)
                    #print(R)
                elif ti == 6:
                    R=random.randint(-2,0)
                    #print(R)
                elif ti == 5:
                    R=random.randint(-2,1)
                    #print(R)
                else:
                    R=random.randint(-2,2)
                    #print(R)
                if ti == 4:
                    if tiertally[6] < tierdistro[6]:
                        R=2
                if ti == 2:
                    if tiertally[0] < tierdistro[0]:
                        R=-2
                newtier=currenttier+R
                return newtier

starter=0
for ti in [0,6,1,5,2,4,3]:
    for key in keys:
        if key not in ['ScorpiosRex', 'Scorpios Rex', 'Indominus Rex', 'IndominusRex', 'Indoraptor']:
            currenttier=int(dinodict[key]['TIER2'])
            if currenttier < 8:
                if currenttier == ti:
                    if ti == 0 and starter == 0: #force tier 0 starter
                        starter = 1
                        species.append(key)
                        dinodict[key]['TIER3']=0
                        inspec.append(dinodict[key]['CLASS'])
                        inspec2.append(dinodict[key]['CLASS2'])
                    else:
                        newtier=reroll(currenttier,ti)
                        #print(key)
                        #print(newtier)
                        if tiertally[newtier] < tierdistro[newtier]:
                           tiertally[newtier]+=1
                           dinodict[key]['TIER3']=newtier
                        else:
                            checkr=0
                            while checkr == 0:
                                 newtier = reroll(currenttier,ti)
                                 if tiertally[newtier] < tierdistro[newtier]:
                                     #print(key,newtier)
                                     tiertally[newtier]+=1
                                     dinodict[key]['TIER3']=newtier
                                     checkr=1
                                     #print(tiertally)
                 
#for t in [0,1,2,3,4,5,6]:
#    for key in keys:
#        if dinodict[key]['TIER3'] == t:
#            print(key,dinodict[key]['TIER3'])
specdist1=['aquatic','pterosaur','primitive','dromaeosaurid','coelurosaur','carnosaur','tyrannosaurid','ornithomimid','ceratopsian','hadrosaur','ornithopod','stegosaurid','pachy','sauropod','ankylosaurid']
specdist2=['pliosaurid','plesiosaurid','mosasaurid','ichthyosaurid','pteranodontid','tapejarid','macronychoptera','ceratosaurid','spinosaurid','primitive','dromaeosaurid','coelurosaur','carnosaur','tyrannosaurid','ornithomimid','chasmosaurine','centrosaurine','saurolophine','lambeosaurine','ornithopod','stegosaurid','huayangosaurid','pachy','diplodocid','macronarian','ankylosaurid','nodosaurid']


sizes={}
sizes['large']=0
sizes['medium']=0
sizes['small']=0
sizes['scavenger']=0
                               
if mode == 'random' or mode == 'Random' or mode == 'RANDOM' or cap < 15:
    while len(species) < cap+1:
        for tier in tls[1:]:
            for key in keys:
                if int(dinodict[key]['TIER3'])==tier and key not in species:
                    species.append(key)
                    break
                if len(species) > cap-1:
                    break
            if len(species) > cap-1:
                break
        break

elif 14 < cap < 22:
     while len(species) < cap+1:
        for tier in tls[1:]:
            for key in keys:
                if int(dinodict[key]['TIER3'])==tier and key not in species:
                    if dinodict[key]['CLASS'] in specdist1 and dinodict[key]['CLASS'] not in inspec:
                        if dinodict[key]['CLASS'] in ['primitive','dromaeosaurid','coelurosaur','carnosaur','tyrannosaurid']:
                            if dinodict[key]['DIET'] ==  'meat' or dinodict[key]['DIET'] ==  'omni':
                                sizes[dinodict[key]['SIZE']]=1
                            species.append(key)
                            inspec.append(dinodict[key]['CLASS'])
                            break
                        else:
                            species.append(key)
                            inspec.append(dinodict[key]['CLASS'])
                            break
                if len(species) > cap-1:
                    break
            if len(species) > cap-1:
                break
        break   
    
else:
     while len(species) < cap+1:
        for tier in tls[1:]:
            for key in keys:
                #print(dinodict[key])
                if int(dinodict[key]['TIER3'])==tier and key not in species:
                    if dinodict[key]['CLASS2'] in specdist2 and dinodict[key]['CLASS2'] not in inspec2:
                        if dinodict[key]['CLASS'] in ['primitive','dromaeosaurid','coelurosaur','carnosaur','tyrannosaurid']:
                            if dinodict[key]['DIET'] ==  'meat' or dinodict[key]['DIET'] ==  'omni':
                                sizes[dinodict[key]['SIZE']]=1
                            species.append(key)
                            inspec2.append(dinodict[key]['CLASS2'])
                            break
                        else:
                            species.append(key)
                            inspec2.append(dinodict[key]['CLASS2'])
                            break
                if len(species) > cap-1:
                    break
            if len(species) > cap-1:
                break
        break   

for s in sizes:
    #print(s)
    nnn=0
    if sizes[s] == 0:
        r=random.randint(0,6)
        for tier in tls[r:]:
            for key in keys:
                if len(species) < cap and int(dinodict[key]['TIER3'])==tier and key not in species and dinodict[key]['SIZE'] == s and dinodict[key]['CLASS'] in ['primitive','dromaeosaurid','coelurosaur','carnosaur','tyrannosaurid'] and nnn == 0:
                    species.append(key)
                    nnn=1

while len(species) < cap+1:
    r=random.randint(0,6)
    for tier in tls[r:]:
        for key in keys:
            if int(dinodict[key]['TIER3'])==tier and key not in species:
                species.append(key)
                break
            if len(species) > cap-1:
                break
        if len(species) > cap-1:
            break
    break
    
#print(inspec)
#print(inspec2)
#print(sizes)
    
species2=[]

for s in species:
    if dinodict[s]['TIER3'] == 0:
        species2.append(s)

for s in species:
    if dinodict[s]['TIER3'] == 1:
        species2.append(s)

for s in species:
    if dinodict[s]['TIER3'] == 2:
        species2.append(s)

for s in species:
    if dinodict[s]['TIER3'] == 3:
        species2.append(s)

for s in species:
    if dinodict[s]['TIER3'] == 4:
        species2.append(s)

for s in species:
    if dinodict[s]['TIER3'] == 5:
        species2.append(s)

for s in species:
    if dinodict[s]['TIER3'] == 6:
        species2.append(s)

import time
t=time.time()
f=open('skins_genes_'+str(t)+'.txt','w+')
for s in species2:
    flip=0
    if 'variant' in dinodict[s]['CANONICITY'].split(';'):
        flip=random.randint(0,1)
    if flip == 0:    
        f.write(s+' '+str(dinodict[s]['TIER3']/2)+' '+dinodict[s]['GENOME']+' '+dinodict[s]['COSMETIC']+'\n')
    else:
        f.write(s+' Variant'+' '+str(dinodict[s]['TIER3']/2)+' '+dinodict[s]['GENOME']+' '+dinodict[s]['COSMETIC']+'\n')
        
for s in dinodict:
    if dinodict[s]['CLASS']=='hybrid':
        f.write(s+' '+dinodict[s]['GENOME']+' '+dinodict[s]['COSMETIC']+' '+'\n')
f.close()

tag1=['1','2','3','4','5','6','7']
tag2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
tag1pos=-1
tag2pos=0
saver=-1
f1=open('techtrees.trees.herbivores1techtree.lua','w')
f1.write('-- params : ...\n')
f1.write('-- function num : 0 , upvalues : _ENV\n')
f1.write('local global = _G\n')
f1.write('local api = global.api\n')
f1.write('local Herbivores1TechTree = module(...)\n')
f1.write('Herbivores1TechTree.TechTree = {name = "Herbivores1", uiCategory = "Herbivores1", \n')
f1.write('nodes = {\n')
for spec in species2: 
    if dinodict[spec]['TREE']=='h1':
        if dinodict[spec]['TIER3'] == saver:
            tag2pos+=1
        else:
            tag1pos+=1
            tag2pos=0
        #print(spec,tag1pos,tag2pos)
        f1.write('N'+tag1[tag1pos]+tag2[tag2pos]+' = {icon = "icons.dinosaurSpecies.diplodocus", dinosaurImage = "Diplodocus", \n')
        f1.write('conditions = {\n')
        f1.write('{preset = "Rating", Target = "'+str(dinodict[spec]['TIER3']/2)+'"}\n')
        f1.write('}\n')
        f1.write(', \n')
        f1.write('rewards = {\n')
        if dinodict[spec]['DLC'] != '':
            f1.write('{id = "TechTree_'+spec+'", dlc = (api.content).DLC_'+dinodict[spec]['DLC']+'}\n')
        else:
            f1.write('{id = "TechTree_'+spec+'"}\n')
        f1.write('}\n')
        f1.write('}\n')
        f1.write(', \n')
        saver=dinodict[spec]['TIER3']
        
f1.write('}\n')
f1.write('}\n')
        
f2=open('techtrees.trees.herbivores2techtree.lua','w')
tag1pos=-1
tag2pos=0
saver=-1
f2.write('-- params : ...\n')
f2.write('-- function num : 0 , upvalues : _ENV\n')
f2.write('local global = _G\n')
f2.write('local api = global.api\n')
f2.write('local Herbivores2TechTree = module(...)\n')
f2.write('Herbivores2TechTree.TechTree = {name = "Herbivores2", uiCategory = "Herbivores2", \n')
f2.write('nodes = {\n')
for spec in species2: 
    if dinodict[spec]['TREE']=='h2':
        if dinodict[spec]['TIER3'] == saver:
            tag2pos+=1
        else:
            tag1pos+=1
            tag2pos=0
        #print(spec,tag1pos,tag2pos)
        f2.write('N'+tag1[tag1pos]+tag2[tag2pos]+' = {icon = "icons.dinosaurSpecies.gallimimus", dinosaurImage = "Gallimimus", \n')
        f2.write('conditions = {\n')
        f2.write('{preset = "Rating", Target = "'+str(dinodict[spec]['TIER3']/2)+'"}\n')
        f2.write('}\n')
        f2.write(', \n')
        f2.write('rewards = {\n')
        if dinodict[spec]['DLC'] != '':
            f2.write('{id = "TechTree_'+spec+'", dlc = (api.content).DLC_'+dinodict[spec]['DLC']+'}\n')
        else:
            f2.write('{id = "TechTree_'+spec+'"}\n')
        f2.write('}\n')
        f2.write('}\n')
        f2.write(', \n')
        saver=dinodict[spec]['TIER3']
        
f2.write('}\n')
f2.write('}\n')
            
f3=open('techtrees.trees.herbivores3techtree.lua','w')
tag1pos=-1
tag2pos=0
saver=-1
f3.write('-- params : ...\n')
f3.write('-- function num : 0 , upvalues : _ENV\n')
f3.write('local global = _G\n')
f3.write('local api = global.api\n')
f3.write('local Herbivores3TechTree = module(...)\n')
f3.write('Herbivores3TechTree.TechTree = {name = "Herbivores3", uiCategory = "Herbivores3", \n')
f3.write('nodes = {\n')
for spec in species2: 
    if dinodict[spec]['TREE']=='h3':
        if dinodict[spec]['TIER3'] == saver:
            tag2pos+=1
        else:
            tag1pos+=1
            tag2pos=0
        #print(spec,tag1pos,tag2pos)
        f3.write('N'+tag1[tag1pos]+tag2[tag2pos]+' = {icon = "icons.dinosaurSpecies.triceratops", dinosaurImage = "Triceratops", \n')
        f3.write('conditions = {\n')
        f3.write('{preset = "Rating", Target = "'+str(dinodict[spec]['TIER3']/2)+'"}\n')
        f3.write('}\n')
        f3.write(', \n')
        f3.write('rewards = {\n')
        if dinodict[spec]['DLC'] != '':
            f3.write('{id = "TechTree_'+spec+'", dlc = (api.content).DLC_'+dinodict[spec]['DLC']+'}\n')
        else:
            f3.write('{id = "TechTree_'+spec+'"}\n')
        f3.write('}\n')
        f3.write('}\n')
        f3.write(', \n')
        saver=dinodict[spec]['TIER3']
        
f3.write('}\n')
f3.write('}\n')
            
f4=open('techtrees.trees.carnivorestechtree.lua','w')
tag1pos=-1
tag2pos=0
saver=-1
f4.write('-- params : ...\n')
f4.write('-- function num : 0 , upvalues : _ENV\n')
f4.write('local global = _G\n')
f4.write('local api = global.api\n')
f4.write('local CarnivoresTechTree = module(...)\n')
f4.write('CarnivoresTechTree.TechTree = {name = "Carnivores", uiCategory = "Carnivores", \n')
f4.write('nodes = {\n')
for spec in species2: 
    if dinodict[spec]['TREE']=='c':
        if dinodict[spec]['TIER3'] == saver:
            tag2pos+=1
        else:
            tag1pos+=1
            tag2pos=0
        #print(spec,tag1pos,tag2pos)
        f4.write('N'+tag1[tag1pos]+tag2[tag2pos]+' = {icon = "icons.dinosaurSpecies.tyrannosaurusRex", dinosaurImage = "TyrannosaurusRex", \n')
        f4.write('conditions = {\n')
        f4.write('{preset = "Rating", Target = "'+str(dinodict[spec]['TIER3']/2)+'"}\n')
        f4.write('}\n')
        f4.write(', \n')
        f4.write('rewards = {\n')
        if dinodict[spec]['DLC'] != '':
            f4.write('{id = "TechTree_'+spec+'", dlc = (api.content).DLC_'+dinodict[spec]['DLC']+'}\n')
        else:
            f4.write('{id = "TechTree_'+spec+'"}\n')
        f4.write('}\n')
        f4.write('}\n')
        f4.write(', \n')
        saver=dinodict[spec]['TIER3']

f4.write('N8A = {icon = "icons.dinosaurSpecies.indominusRex", dinosaurImage = "IndominusRex", description = "TechTree_Node_Carnivores_SingleGenome_Description:Genome=[IndominusRex]", \n')
f4.write('conditions = {\n')
f4.write('{preset = "Rating", Target = "3"}\n')
f4.write(', \n')
f4.write('{preset = "SpeciesGenome", Genome = "TyrannosaurusRex", Percentage = "100"}\n')
f4.write(', \n')
f4.write('{preset = "SpeciesGenome", Genome = "Velociraptor", Percentage = "25"}\n')
f4.write(', \n')
f4.write('{preset = "SpeciesGenome", Genome = "Giganotosaurus", Percentage = "25"}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('research = {duration = 500, staffLimit = 4, cost = 10000000, \n')
f4.write('proficiency = {science = 20, construction = 6}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('rewards = {\n')
f4.write('{id = "TechTree_IndominusRex"}\n')
f4.write('}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('N8B = {icon = "icons.dinosaurSpecies.scorpiosRex", dinosaurImage = "ScorpiosRex", description = "TechTree_Node_Carnivores_SingleGenome_Description:Genome=[ScorpiosRex]", \n')
f4.write('conditions = {\n')
f4.write('{preset = "Rating", Target = "3"}\n')
f4.write(', \n')
f4.write('{preset = "SpeciesGenome", Genome = "Carnotaurus", Percentage = "100"}\n')
f4.write(', \n')
f4.write('{preset = "SpeciesGenome", Genome = "TyrannosaurusRex", Percentage = "75"}\n')
f4.write(', \n')
f4.write('{preset = "SpeciesGenome", Genome = "Velociraptor", Percentage = "10"}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('research = {duration = 500, staffLimit = 4, cost = 10000000, \n')
f4.write('proficiency = {science = 20, construction = 6}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('rewards = {\n')
f4.write('{id = "TechTree_ScorpiosRex", dlc = (api.content).DLC_DinoPack2}\n')
f4.write('}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('N8C = {parent = "N8A", icon = "icons.dinosaurSpecies.indoraptor", dinosaurImage = "Indoraptor", description = "TechTree_Node_Carnivores_SingleGenome_Description:Genome=[Indoraptor]", \n')
f4.write('conditions = {\n')
f4.write('{preset = "Rating", Target = "3"}\n')
f4.write(', \n')
f4.write('{preset = "SpeciesGenome", Genome = "Velociraptor", Percentage = "100"}\n')
f4.write(', \n')
f4.write('{preset = "DinosaurReleased", Genome = "IndominusRex"}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('research = {duration = 800, staffLimit = 4, cost = 15000000, \n')
f4.write('proficiency = {welfare = 22, construction = 10}\n')
f4.write('}\n')
f4.write(', \n')
f4.write('rewards = {\n')
f4.write('{id = "TechTree_Indoraptor"}\n')
f4.write('}\n')
f4.write('}\n')
f4.write('}\n')
f4.write('}\n')
        
#f4.write('}\n')
#f4.write('}\n')
            
f5=open('techtrees.trees.flyingtechtree.lua','w')
tag1pos=-1
tag2pos=0
saver=-1
f5.write('-- params : ...\n')
f5.write('-- function num : 0 , upvalues : _ENV\n')
f5.write('local global = _G\n')
f5.write('local api = global.api\n')
f5.write('local FlyingTechTree = module(...)\n')
f5.write('FlyingTechTree.TechTree = {name = "Flying", uiCategory = "Flying", \n')
f5.write('nodes = {\n')
for spec in species2: 
    if dinodict[spec]['TREE']=='f':
        if dinodict[spec]['TIER3'] == saver:
            tag2pos+=1
        else:
            tag1pos+=1
            tag2pos=0
        #print(spec,tag1pos,tag2pos)
        f5.write('N'+tag1[tag1pos]+tag2[tag2pos]+' = {icon = "icons.dinosaurSpecies.pteranodon", dinosaurImage = "Pteranodon", \n')
        f5.write('conditions = {\n')
        f5.write('{preset = "Rating", Target = "'+str(dinodict[spec]['TIER3']/2)+'"}\n')
        f5.write('}\n')
        f5.write(', \n')
        f5.write('rewards = {\n')
        if dinodict[spec]['DLC'] != '':
            f5.write('{id = "TechTree_'+spec+'", dlc = (api.content).DLC_'+dinodict[spec]['DLC']+'}\n')
        else:
            f5.write('{id = "TechTree_'+spec+'"}\n')
        f5.write('}\n')
        f5.write('}\n')
        f5.write(', \n')
        saver=dinodict[spec]['TIER3']
        
f5.write('}\n')
f5.write('}\n')
            
f6=open('techtrees.trees.marinetechtree.lua','w')
tag1pos=-1
tag2pos=0
saver=-1
f6.write('-- params : ...\n')
f6.write('-- function num : 0 , upvalues : _ENV\n')
f6.write('local global = _G\n')
f6.write('local api = global.api\n')
f6.write('local MarineTechTree = module(...)\n')
f6.write('MarineTechTree.TechTree = {name = "Marine", uiCategory = "Marine", \n')
f6.write('nodes = {\n')
for spec in species2: 
    if dinodict[spec]['TREE']=='m':
        if dinodict[spec]['TIER3'] == saver:
            tag2pos+=1
        else:
            tag1pos+=1
            tag2pos=0
        #print(spec,tag1pos,tag2pos)
        f6.write('N'+tag1[tag1pos]+tag2[tag2pos]+' = {icon = "icons.dinosaurSpecies.mosasaurus", dinosaurImage = "Mosasaurus", \n')
        f6.write('conditions = {\n')
        f6.write('{preset = "Rating", Target = "'+str(dinodict[spec]['TIER3']/2)+'"}\n')
        f6.write('}\n')
        f6.write(', \n')
        f6.write('rewards = {\n')
        if dinodict[spec]['DLC'] != '':
            f6.write('{id = "TechTree_'+spec+'", dlc = (api.content).DLC_'+dinodict[spec]['DLC']+'}\n')
        else:
            f6.write('{id = "TechTree_'+spec+'"}\n')
        f6.write('}\n')
        f6.write('}\n')
        f6.write(', \n')
        saver=dinodict[spec]['TIER3']
        
f6.write('}\n')
f6.write('}\n')
    
#icon = "icons.dinosaurSpecies.pteranodon", dinosaurImage = "Pteranodon",    
#icon = "icons.dinosaurSpecies.mosasaurus", dinosaurImage = "Mosasaurus",
#icon = "icons.dinosaurSpecies.edmontosaurus", dinosaurImage = "Edmontosaurus",
#icon = "icons.dinosaurSpecies.diplodocus", dinosaurImage = "Diplodocus",
#icon = "icons.dinosaurSpecies.gallimimus", dinosaurImage = "Gallimimus",
#icon = "icons.dinosaurSpecies.pachycephalosaurus", dinosaurImage = "Pachycephalosaurus",
#icon = "icons.dinosaurSpecies.triceratops", dinosaurImage = "Triceratops",
#icon = "icons.dinosaurSpecies.stegosaurus", dinosaurImage = "Stegosaurus", 
#icon = "icons.dinosaurSpecies.ankylosaurus", dinosaurImage = "Ankylosaurus",
#icon = "icons.dinosaurSpecies.compsognathus", dinosaurImage = "Compsognathus",
#icon = "icons.dinosaurSpecies.velociraptor", dinosaurImage = "Velociraptor", 
#icon = "icons.dinosaurSpecies.tyrannosaurusRex", dinosaurImage = "TyrannosaurusRex", 
#icon = "icons.dinosaurSpecies.carnotaurus", dinosaurImage = "Carnotaurus",
#icon = "icons.dinosaurSpecies.iguanodon", dinosaurImage = "Iguanodon", 
    
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()