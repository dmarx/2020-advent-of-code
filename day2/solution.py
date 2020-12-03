import click
import re

def validate(line):
    return False

@click.command()
@click.argument("infile", default="input.txt", type=click.File("rb"))
def cli(infile):
    valid = []
    for line in infile:
        is_valid = validate(line)
        if is_valid:
            valid.append(line)
       
    click.echo(len(valid))


if __name__ =='__main__':
    cli()