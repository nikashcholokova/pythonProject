import datetime
import random


def add_street(current_street_id, build_range_end,
               people_range_start, people_range_end):
    return Street(current_street_id, build_range_end,
                  people_range_start, people_range_end)


class City:
    streets = []

    def __init__(self, name, street_count: int, build_range_end,
                 people_range_start, people_range_end):
        self.name = name
        for current in range(1, street_count + 1):
            self.streets.append(add_street(current, build_range_end,
                                           people_range_start, people_range_end))

    def population(self):
        people_count = 0
        for i in self.__getattribute__('streets'):
            for j in i.__getattribute__('buildings'):
                people_count += j.__getattribute__('people')

        return people_count

    def print_table(self):
        row_to_print = ''
        for i in self.__getattribute__('streets'):
            for j in i.__getattribute__('buildings'):
                row_to_print += str(i.__getattribute__('street_id')) + ' ' \
                                + str(j.__getattribute__('building_id')) + ' ' \
                                + str(j.__getattribute__('people'))
                print(row_to_print)
                row_to_print = ''


class Street:
    buildings = []

    def __init__(self, street_id: int, build_range_end: int,
                 people_range_start: int, people_range_end: int):
        self.street_id = street_id
        for current in range(1, build_range_end + 1):
            self.buildings.append(Building(current, people_range_start, people_range_end))


class Building:
    def __init__(self, building_id: int, people_range_start: int, people_range_end: int):
        self.building_id = building_id
        self.people = random.randrange(people_range_start, people_range_end + 1)
