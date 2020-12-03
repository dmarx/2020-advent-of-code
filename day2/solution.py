import click
import re

def parse(line):
    rule_lhs, rule_rhs, pwd= line.split(' ')
    nmin, nmax = rule_lhs.split('-')
    reqd_string = rule_rhs[:-1]
    return nmin, nmax, reqd_string, pwd
    

def validate(line):
    nmin, nmax, reqd_string, pwd = parse(line)
    pat = f".*{reqd_string}{{{nmin},{nmax}}}.*"
    return re.match(pat, pwd)

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