import pandas as pd
import inputHandler


def print_output(sorted_df, nitems_requested):
    for i in range(0, nitems_requested):
        print("#" + str(i + 1) + ":\n" +
              "PRICE: " + str(int(sorted_df['PRICE'].values[i])) + "원\n" +
              "ITEM NAME: " + sorted_df['NAME'].values[i] + "\n" +
              "WEBSITE: " + sorted_df['SHOP'].values[i] + "\n")


def calculate_average(df):
    average = int(df['PRICE'].mean())
    print("The average price is: " + str(average) + "원")


def calculate_lowest(df, nitems_requested):
    lowest = df.sort_values(by='PRICE').head(nitems_requested)
    print_output(lowest, nitems_requested)


def calculate_highest(df, nitems_requested):
    highest = df.sort_values(by='PRICE', ascending=False).head(nitems_requested)
    print_output(highest, nitems_requested)


def task_handler(filename, nitems_scraped):
    df = pd.read_csv(filename, delimiter="\t")
    task = inputHandler.get_task_input()
    if task == 0:
        return False
    if task == 1:
        calculate_average(df)
    if task == 2:
        nitems_requested = inputHandler.get_task_details(nitems_scraped)
        calculate_lowest(df, nitems_requested)
    if task == 3:
        nitems_requested = inputHandler.get_task_details(nitems_scraped)
        calculate_highest(df, nitems_requested)
    return True


def test(filename):
    df = pd.read_csv(filename, delimiter="\t")
    print(df)