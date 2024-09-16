

## 1. Self-replication
each creature:
location;
genome = genetic information. dna/rna = chemical storage medium
neuralnet brain;

## 2. Blueprint

everycreature must be constructed using some blueprint.


## 3. Inherit
when creating a new child, we use some genome from one parent and some from another

## 4. Mutation
has to go occasional mutation.

## 5. Selection
who gets to reproduce and who doesn't




Genome length: 4 genes
52562f78 3c398812 4989b501 039c5fbd

4 genes make 4 neural connections.

differnt creature has differnt genomes with differnt brain and differnt in how they behave

4 neurons:
LPf = sensory input, population forward, senses the population density in their forwared direction of movement
MvE = ouput, move east
Mrn = output, move random
N0 = internal neuron

# GENETIC ALGORITHM

Another effort at mimicking biology or evolution.
naive attemps to mimic naive evolution.

when each creature is born. Right now say 4 genes. 4 gene defines 4 neural connection. the connection can be with any neuron. determined by genes itself.
sometimes the neuron can go to internal neuron but the internal neuron might not go anywhere. in that case the connections are completely useless.
connections are either positive or negative.
connection go from sensory neuron to action neuron, sensory to internal neuron or internal neuron to action output neuron, or inner neuron to inner neuron or to itself.

inputs neuronproduce 0.0 to 1.0 multiplied by
connection weights -4.0 to 4.0

neural output = tanh(sum(inputs)) = -1.0 to 1.0
f ajf

action neurons = tanh(sum(inputs)) = -1.0 to 1.0

if the sum of the inputs after passing through the hyperbolic tangent function is positive i.e. 0 to 1 it is treated as a probability during that simulator step of it actually being activated.

## Sensory inputs

Slr = pheromone gradient left-right
Sfd = pheronome gradient forward
Sg = pheromone density
Age = Age
Rnd = random input
Blr = blockage left-right
Osc = oscillator # 20 or 30 simulator cycles
Bfd = blockage forward
Plr = population gradient left-right
Pop = population density # sensitive to population density in the immediate neighborhood
Pfd = population gradient forward # sensity not just to population density but also to population gradient in the forward direction

Lpf = population long-range forward
LMy = last movement Y
LBf = blockage long-range forward
LMx = last movement X
BDy = north/south border distance
Gen = genetic similarity of fwd neighbor ## measure of genetic compatibility
BDx = east/west border distance
Lx = east/west world location # x,y location of the creature
BD = nearest border distance
Ly = notrh/south world location

## Action outputs

LPD = set long-probe distance
Kill = kill forward neighbor
OSC = set oscillator period
SG = emit pheromone
Res = set responsiveness ## when it is not driven it means the creature has avg level of reactivity to its input stimuli, but if it is driven then it causes the creature to be more nervous, more reactive like it is on caffeine. when less driven, it is lazy.

Mfd = move forward ## forward is defined as whatever the last direction of movement was
Mrn = move random
Mrv = move reverse
MRL = move left/right (+/-)
MX = move east/west (+/-)
MY = move north/south (+/-)
