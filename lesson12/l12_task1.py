from lesson12 import City

street_amount = 10
build_range_end = 20
people_range_start = 1
people_range_end = 100

city = City.City('UA_City', street_amount, build_range_end,
                 people_range_start, people_range_end)
print(city.population())
city.print_table()
