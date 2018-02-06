from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.
# Method 1
country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    country_counts[country] = country_counts.get(country,0) + 1

# Method 2
for country in country_list:
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1
