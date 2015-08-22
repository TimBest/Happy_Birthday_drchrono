import os
import csv

from timezones.models import State


states_csv = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'data/states.csv'))

states = ['state', 'timezone']
file_fields = ['state', 'timezone']


def run():
    for row in csv.reader(open(states_csv),delimiter=','):
        state, created = State.objects.update_or_create(
            state=row[0],
            defaults= {
                'timezone': row[1],
            },
        )
