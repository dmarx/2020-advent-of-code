import click

def str2dict(fields_str):
    d = {}
    for field in fields_str.split():
        k,v = field.split(':')
        d[k] = v
    return d 
    
def read_passports(infile):
    text = infile.read().decode()
    raw_passports = [s.strip() for s in text.split('\n\n')]
    dict_passports = [str2dict(s) for s in raw_passports]
    return dict_passports
    
def is_valid_passport(passport):
    #return all_fields_present(passport) or only_field_missing_is_cid(passport)
    return only_field_missing_is_cid(passport) # logically equivalent to above
    
def all_fields_present(passport):
    reqd_fields = ('byr','iyr','eyr','hgt','hcl','ecl','pid','cid')
    return all(f in passport for f in reqd_fields)
    
def only_field_missing_is_cid(passport):
    reqd_fields = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
    return all(f in passport for f in reqd_fields)

def dothething(infile):
    passports = read_passports(infile)
    return sum([is_valid_passport(p) for p in passports])

@click.command()
@click.argument("infile", default="input.txt", type=click.File("rb"))
def cli(infile):
    outv = dothething(infile)
    click.echo(outv)

if __name__ =='__main__':
    cli()