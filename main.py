from matplotlib import pyplot as plt
import random
#This concept is from Primer. I am using his concept from his video "Mutations and the First Replicators," all code is by me. I use his parameters and use the same algorithm by him, however.
xAxis = [i for i in range(120)]
yAxisBlue = []
yAxisGreen = []
yAxisRed = []
yAxisBlueExpect = []
yAxisGreenExpect = []
yAxisRedExpect = []

class blue:
    organisms = 1
    birth = 1
    death = 10
    replication = 20
    mutationGreen = 10
    mutationRed = 10

    birthChance = 100
    deathChance = 10
    replicationChance = 5
    mutationChance = 10

class green:
    organisms = 0
    birth = 0
    death = 10
    replication = 20
    mutation = 0

class red:
    organisms = 0
    birth = 0
    death = 20
    replication = 20
    mutation = 5

class orange:
    organisms = 0
    birth = 0
    death = 20
    replication = 10

creatures = [blue, green]

def death(creatureClass):
    for i in range(1, creatureClass.organisms):
        
        if random.randint(1, creatureClass.death) == 1:
            creatureClass.organisms-=1


def simulation():
    #This is mega innefficient but I don't care too much right now.
    for i in range(120):
        #replicatin and mutation
        if blue.organisms > 0:
            blue.organisms+=1
            
            for i in range(blue.organisms):
                if random.randint(1, blue.replication) == 1:
                    if random.randint(1, blue.mutationGreen) == 1:
                        green.organisms+=1
                        
                    elif random.randint(1, blue.mutationRed) == 2:
                        red.organisms+=1
                        
                    else:
                        blue.organisms+=1
            
            death(blue)
            

            
                        
            if green.organisms > 0:
                for i in range(1, green.organisms):
                    if random.randint(1, green.replication) == 1:
                        green.organisms+=1
                death(green)

            if red.organisms > 0:
                for i in range(1, red.organisms):
                    
                    if random.randint(1, red.replication) == 1:
                        if random.randint(1, red.mutation) == 1:
                            orange.organisms+=1
                        else:
                            red.organisms+=1
                death(red)

            
                
        #E = B1 + (R1(1 - M1) - D1) * O1
        expectedChangeBlue = 1 + (0.5 * (1 - 0.1) - 0.1) * blue.organisms
        
        #E = B2 + (R2 - D2) * O2 + R1*M1*O1
        expectedChangeGreen = 0 + (0.5 - 0.1) * green.organisms + (1*0.1*blue.organisms)
        expectedChangeRed = 0 + (0.5 - 0.5) * red.organisms + (1*0.1*blue.organisms)

        yAxisBlue.append(blue.organisms)
        yAxisGreen.append(green.organisms)
        yAxisRed.append(red.organisms)
        yAxisBlueExpect.append(expectedChangeBlue)
        yAxisGreenExpect.append(expectedChangeGreen)
        yAxisRedExpect.append(expectedChangeRed)
        
#graphing the results
simulation()
plt.subplot(2,1,1)
plt.plot(xAxis, yAxisBlue, color = 'blue')
plt.plot(xAxis, yAxisGreen, color = 'green')
plt.plot(xAxis, yAxisRed, color = 'red')
plt.xlabel('Generations')
plt.ylabel('Number of Organisms')

#predictions
plt.subplot(2,1,2)
plt.plot(xAxis, yAxisBlueExpect, color = 'blue')
plt.plot(xAxis, yAxisGreenExpect, color = 'green')
plt.plot(xAxis, yAxisRedExpect, color = 'red')
plt.xlabel('Generations')
plt.ylabel('Predicted Organisms')
plt.show()
        
                