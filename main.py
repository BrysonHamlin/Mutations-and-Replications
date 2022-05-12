from matplotlib import pyplot as plt
import random
#This concept is from Primer. I am using his concept from his video "Mutations and the First Replicators," all code is by me. I use his parameters and use the same algorithm by him, however.
xAxis = [i for i in range(120)]
yAxisBlue = []
yAxisGreen = []
yAxisBlueExpect = []
yAxisGreenExpect = []

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
    mutation = 0

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
                    elif random.randint(1, blue.mutationRed) = 2
                        red.organisms+=1
                    else:
                        blue.organisms+=1
            
            death(blue)
            

            if green.organisms > 0:
                for i in range(green.organisms):
                    if random.randint(1, green.replication) == 1:
                        green.organisms+=1
                        
                death(green)
        #E = B1 + (R1(1 - M1) - D1) * O1
        expectedChangeBlue = 1 + (0.5 * (1 - 0.1) - 0.1) * blue.organisms
        #E = B2 + (R2 - D2) * O2 + R1*M1*O1
        expectedChangeGreen = 0 + (0.5 - 0.1) * green.organisms + (1*0.1*blue.organisms)

        yAxisBlue.append(blue.organisms)
        yAxisGreen.append(green.organisms)
        yAxisBlueExpect.append(expectedChangeBlue)
        yAxisGreenExpect.append(expectedChangeGreen)
#graphing the results
simulation()
plt.subplot(1,2,1)
plt.plot(xAxis, yAxisBlue, color='blue')
plt.plot(xAxis, yAxisGreen, color='green')
plt.xlabel('Generations')
plt.ylabel('Number of Organisms')

#predictions
plt.subplot(1,2,2)
plt.plot(xAxis, yAxisBlueExpect, color = 'blue')
plt.plot(xAxis, yAxisGreenExpect, color = 'green')
plt.show()
        
                