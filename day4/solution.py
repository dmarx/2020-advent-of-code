import click
import re
import pandas as pd

def str2dict(fields_str):
    d = {}
    for field in fields_str.split():
        k,v = field.split(':')
        d[k] = str(v)
    return d 
    
def read_passports(infile):
    text = infile.read().decode()
    raw_passports = [s.strip() for s in text.split('\n\n')]
    dict_passports = [str2dict(s) for s in raw_passports]
    return dict_passports
    
def all_fields_present(passport):
    reqd_fields = ('byr','iyr','eyr','hgt','hcl','ecl','pid','cid')
    return all(f in passport for f in reqd_fields)
    
def only_field_missing_is_cid(passport):
    reqd_fields = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
    return all(f in passport for f in reqd_fields)
    
##########################3

def is_valid_passport(passport):
    #return all_fields_present(passport) or only_field_missing_is_cid(passport)
    #return only_field_missing_is_cid(passport) # logically equivalent to above
    return validate_field_contents(passport)

def validate_height(height):
    #if not isinstance(height, str):
    #    click.echo(("funky height: ", height))
    #height = str(height)
    height = height.strip()
    if height.endswith('cm'):
        return (len(height) == 5) and (150 <= int(height[:-2]) <= 193)
    elif height.endswith('in'):
        return (len(height) == 4) and (59 <= int(height[:-2]) <= 76)
    else:
        return False
    


def validate_field_contents(passport):
    validators_reqd = {
        'byr': lambda year: (len(year) == 4) and (1920 <= int(year) <= 2002),
        'iyr': lambda year: (len(year) == 4) and (2010 <= int(year) <= 2020),
        'eyr': lambda year: (len(year) == 4) and (2020 <= int(year) <= 2030),
        'hgt': validate_height,
        'hcl': lambda code: (len(code) == 7) and re.match("#[0-9a-f]{6}", code),
        'ecl': lambda color: color in ('amb','blu','brn','gry','grn','hzl','oth'),
        #'pid': lambda pid: re.match("[0-9]{9}", str(pid))
        'pid': lambda pid: re.match("[0-9]{9}", pid)
    }
    #click.echo(passport)
    for field, validator in validators_reqd.items():
        #if not validator(passport.get(field, False)):
        if field not in passport:
            click.echo(('field not present',field))
            return False
        if not validator(passport[field]):
            click.echo(('field not valid',field))
            return False
    #click.echo(passport)
    return True
    

    
    

def dothething(infile):
    passports = read_passports(infile)
    #return sum([is_valid_passport(p) for p in passports])
    nvalid = 0
    validated = []
    for p in passports:
        test = is_valid_passport(p)
        click.echo(p)
        click.echo(test)
        click.echo()
        if test:
            nvalid+=1
        p['is_valid'] = test
        validated.append(p)
    df = pd.DataFrame(validated)
    #click.echo(df[df['is_valid']])
    #df[df['is_valid']].to_csv('valid_passports.csv')
    return nvalid
    

@click.command()
@click.argument("infile", default="input.txt", type=click.File("rb"))
def cli(infile):
    outv = dothething(infile)
    click.echo(outv)

if __name__ =='__main__':
    cli()