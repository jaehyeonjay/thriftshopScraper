def get_seed_input():
    keyword = input("SEARCH FOR:\n")
    nitems_to_scrape = input("NUMBER OF ITEMS TO COMPARE:\n")
    #TODO: how to select filters on each website?
    return [keyword, nitems_to_scrape]


def get_task_input():
    while True:
        task = input("WHAT WOULD YOU LIKE TO KNOW? ENTER A NUMBER:\n"
                             "0. QUIT\n"
                             "1. AVERAGE PRICE\n"
                             "2. CHEAPEST ITEMS\n"
                             "3. MOST EXPENSIVE ITEMS\n")
        if not task.isdigit(): #TODO: what if user enters like 10000
            print("ENTER A NUMBER. (EX: 1)")
        else:
            return int(task)


def get_task_details(nitems_scraped):
    while True:
        num_requested = input("UP TO HOW MANY ITEMS WOULD YOU LIKE TO CHECK?\n")
        if not num_requested.isdigit():
            print("ENTER A SINGLE NUMBER. (EX: 10)\n")
            continue
        elif int(num_requested) > nitems_scraped:
            print("ENTER A NUMBER LESS THAN " + str(nitems_scraped) + "\n")
            continue
        else:
            return int(num_requested)