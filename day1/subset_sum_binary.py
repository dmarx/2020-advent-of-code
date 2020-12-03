import click
from itertools import accumulate
from itertools import product as crossproduct
import operator

def product(*args):
    for v in accumulate(*args, func=operator.mul):
        continue
    return v

def subset_sum_binary(targetvalue, candidates, k):
    assert k==2
    complements = []
    for i, v in enumerate(candidates):
        c = targetvalue - v
        if v in complements:
            return c, v
        else: 
            complements.append(c)
    raise Exception("No solution found")

# It's inefficient, but the candidate list is reasonably small so fuck it. 
# Let's brute force this shit and see how bad it is.
def subset_sum_naive(targetvalue, candidates, k):
    for rec in crossproduct(candidates, repeat=k):
        if sum(rec) == targetvalue:
            return rec

@click.command()
@click.argument("infile", default="input.txt", type=click.File("rb"))
@click.option("--targetvalue", default=2020, help="What the output values should sum to.")
@click.option("--k", default=2, help="The number of inputs that will be used to sum to the targetvalue.")
def cli(infile, targetvalue, k):
    candidates = [int(line.strip()) for line in infile]
    
    f = subset_sum_naive
    if k == 2:
        f = subset_sum_binary
    outv =  f(targetvalue, candidates, k)    
    click.echo(product(outv))
    click.echo(outv)
    
    
if __name__ =='__main__':
    cli()