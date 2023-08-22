import sys
import click
from getstoken.parserkube import print_contexts,get_token

@click.group()
@click.version_option("1.0.0")
def main():
    """A token fetcher CLI for GKE Cluster"""
    pass


@main.command()
@click.argument('file_path', required=False)
def printContext(**kwargs):
    print_contexts(kwargs.get("keyword"))
    

@main.command()
@click.argument('name', required=False)
def getToken(**kwargs):
    get_token()

    # click.echo(f'CVE-ID \n\n{details["cve-id"]}\n')
    # click.echo(f'Description \n\n{details["description"]}\n')
    # click.echo(f'References \n\n{details["references"]}\n')
    # click.echo(f'Assigning CNA \n\n{details["assigning cna"]}\n')
    # click.echo(f'Date Entry \n\n{details["date entry created"]}')


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Get Token")
    main()