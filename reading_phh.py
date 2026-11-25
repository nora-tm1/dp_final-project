import tomllib

import pandas as pd


def main():
    read_phh("phua-xuan-2019.phh")
    read_phhs("test.phhs")
    phhs_to_csv("test.phhs", "test.csv")


def read_phh(filename):
    pokergames = pd.DataFrame(columns=[
        'antes', 'blinds_or_straddles', 'bring_in', 'small_bet', 'big_bet',
        'min_bet', 'starting_stacks', 'actions', 'author', 'event',
        'url', 'venue', 'address', 'city', 'region', 'postal_code',
        'country', 'time', 'time_zone', 'time_zone_abbreviation',
        'day', 'month', 'year', 'hand', 'level', 'seats', 'seat_count',
        'table', 'players', 'finishing_stacks', 'winnings', 'currency',
        'currency_symbol', 'ante_trimming_status', 'time_limit', 'time_banks'])


    with open(filename, "rb") as f:
        raw = tomllib.load(f)
        data = pd.DataFrame([raw])
        pokergames = pd.concat([pokergames, data])

    return pokergames

def read_phhs(filename):
    pokergames = pd.DataFrame(columns=[
        'antes', 'blinds_or_straddles', 'bring_in', 'small_bet', 'big_bet',
        'min_bet', 'starting_stacks', 'actions', 'author', 'event',
        'url', 'venue', 'address', 'city', 'region', 'postal_code',
        'country', 'time', 'time_zone', 'time_zone_abbreviation',
        'day', 'month', 'year', 'hand', 'level', 'seats', 'seat_count',
        'table', 'players', 'finishing_stacks', 'winnings', 'currency',
        'currency_symbol', 'ante_trimming_status', 'time_limit', 'time_banks'])

    with open(filename, "rb") as f:
        raw = tomllib.load(f)
        df = pd.DataFrame.from_dict(raw, orient="index")
        pokergames = pd.concat([pokergames, df])

    return pokergames

def phhs_to_csv(filename, csv_name):
    df = read_phhs(filename)
    csv_file = df.to_csv(csv_name)

    return csv_file



if __name__ == "__main__":
    main()
