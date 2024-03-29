class Individual:
    def __init__(self, genes):
        self.genes = genes
        self.fitness_function(genes)
      
    # calculates fitness of each individual
    def fitness_function(self, genes):
        score = 0
        for gene in genes:
            if gene == 1:
                score += 1
        self.fitness = score
    
class Population:
    def __init__(self, individuals):
        self.individuals = individuals
        
    def crossover(self, parent_1, parent_2, cross_value=3):
        offspring_1 = parent_1
        offspring_2 = parent_2
        
        # exchange genes below crossover point
        for i in range(cross_value-1):
            gen = offspring_1.genes[i]
            offspring_1.genes[i] = offspring_2.genes[i]
            offspring_2.genes[i] = gen
            
        return [offspring_1, offspring_2]

def genetic_algorithm():
    generation = 1
    population = Population([
        Individual([0, 1, 0, 1, 0]), Individual([1, 1, 0, 0, 0]),
        Individual([0, 1, 1, 1, 0]), Individual([0, 0, 0, 1, 1]),
        Individual([1, 0, 0, 0, 1]), Individual([1, 0, 1, 1, 0])])
    
    while population.get_fittest().fitness < 5:
        # selection
        parent_1 = population.get_fittest()
        parent_2 = population.get_fittest()
    
        # crossover
        offspring = population.crossover(parent_1, parent_2)
    
        # mutation
        offspring = population.mutate(offspring)
    
        # add offspring, remove weakest individuals
        population.grow(offspring)
        population.kill_weakest()
        generation += 1
    
    print(f'The population converged after {generation} generations')