#!/usr/bin/env python3

__author__ = 'Tiffany McLean'

import requests


def get_astronauts_info():
    """
    Get a list of the astronatuts currently in space.  Include their names, the spacecraft that they are currently on board, and the total number of astronatuts in space
    """

    r = requests.get('http://api.open-notify.org/astros.json').json()
    number_of_astronauts = r['number']
    astronauts = r['people']

    for hero in astronauts:
        name = hero['name']
        spacecraft = hero['craft']
        print(f'Name: {name}, Spacecraft: {spacecraft}')
    print(f'Total Number of Astronauts: {number_of_astronauts}')


    # return r
get_astronauts_info()


def main():
    pass


if __name__ == '__main__':
    main()
