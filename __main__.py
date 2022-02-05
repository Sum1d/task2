import sys
import click
from main import folderSynchronization as fs


@click.group()
@click.version_option("1.0.0")
def main():
    """Folder synchronization"""
    pass


@main.command()
@click.argument('source')
@click.argument('target')
@click.argument('t')
def synchronization(source, target, t):
    """Browsing the source folder and replica, synchronizes their contents"""
    fs(source, target, int(t))


if __name__ == '__main__':
    args = sys.argv
    main()
