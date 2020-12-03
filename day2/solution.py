import click
import re

def parse(line):
    rule_lhs, rule_rhs, pwd= line.split(' ')
    nmin, nmax = rule_lhs.split('-')
    nmin, nmax = int(nmin), int(nmax)
    reqd_string = rule_rhs[:-1]
    return nmin, nmax, reqd_string, pwd
    

def validate_part1(line):
    nmin, nmax, reqd_string, pwd = parse(line)
    tgts = [v for v in pwd if v == reqd_string]
    return nmin <= len(tgts) <= nmax
    
def validate(line):
    return False

@click.command()
@click.argument("infile", default="input.txt", type=click.File("rb"))
def cli(infile):
    valid = []
    for line in infile:
        line = line.decode().strip()
        is_valid = validate(line)
        if is_valid:
            valid.append(line)
       
    click.echo(len(valid))
    #click.echo(valid[-3:])


if __name__ =='__main__':
    cli()