import click
import numpy as np

def subset_sum_binary(targetvalue, candidates):
    complements = []
    for i, v in enumerate(candidates):
        c = targetvalue - v
        if v in complements:
            return c, v
        else: 
            complements.append(c)
    raise Exception("No solution found")

@click.command()
@click.argument("infile", default="input.txt", type=click.File("rb"))
@click.option("--targetvalue", default=2020, help="What the output values should sum to.")
@click.option("--k", default=2, help="The number of inputs that will be used to sum to the targetvalue.")
def cli(infile, targetvalue, k):
    candidates = [int(line.strip()) for line in infile]
    
    f = subset_sum_binary
    if k != 2:
        raise NotImplementedError
    outv =  f(targetvalue, candidates)    
    click.echo(np.prod(outv))
    
    
if __name__ =='__main__':
    cli()