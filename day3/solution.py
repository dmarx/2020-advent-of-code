import click
import numpy as np

class ToroidalWorld:
    def __init__(self, worldmap):
        self.worldmap = worldmap
        
        self._matrix = self.worldmap2matrix(self.worldmap)
        self._flat = self.worldmap2flat(self.worldmap)
    
    def worldmap2matrix(self, worldmap):
        arrayified = [[0 if c=='.' else 1 for c in line] for line in worldmap.split()]
        return np.array(arrayified)
        
    def worldmap2flat(self, worldmap):
        return [0 if c=='.' else 1 for line in worldmap.split() for c in line]
    
    def ntrees_along_path(self, 
                  init_pos = (0,0),
                  right = 3,
                  down = 1):
        def pos_to_step(a,b):
            return a + b*self._matrix.shape[1]
        
        step = pos_to_step(right, down)
        init_pos = step + pos_to_step(*init_pos)
        
        ### DEBUG ###
        click.echo(self._matrix.shape)
        click.echo(("step, initpos:", step, init_pos))
        
        #path = []
        ntrees = 0
        ntrees2 = 0
        pos = init_pos
        #i = 0
        i=down
        #while pos <= len(self._flat):
        while i < self._matrix.shape[0]:
            #path.append(pos)
            
            ### DEBUG ###
            #i+=1
            #j= pos % self._matrix.shape[1]
            j= pos % self._matrix.shape[1]
            #click.echo((self._flat[pos], pos, i, j))
            
            #ntrees += self._flat[pos]
            ntrees2 += self._matrix[i,j]
            pos += step
            #i+=1
            i+=down
            
        #click.echo(("hmm...", ntrees, ntrees2))
        return ntrees2


def dothething(infile,
               #init_pos = (0,0),
               right = 3,
               down = 1):
    world = ToroidalWorld(infile.read().decode())
    
    ### DEBUG ###
    click.echo(world.ntrees_along_path())
    click.echo(world._matrix.shape)
    click.echo(len(world._flat))
    click.echo(world.worldmap)
    click.echo(world._matrix)
    click.echo(world._flat)
    
    return world.ntrees_along_path(right=right, down=down)

@click.command()
@click.argument("infile", default="input.txt", type=click.File("rb"))
@click.option("--right", default=3)
@click.option("--down", default=1)
def cli(infile, right, down):
    outv = dothething(infile, right=right, down=down)
    click.echo(outv)
    
    

if __name__ =='__main__':
    cli()