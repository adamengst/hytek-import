"""Script to create a HyTek-formatted .txt file from a WebScorer-created .txt file.

This script runs with Python 3. Please use Miniconda to run Python so you don't mess
up your system.

WEBSCORER FORMAT RULES:
1. In Webscorer, event titles must be of the form
    'event_time/distance_metric/english_EVENTNAME', eg. 'event_time_metric_100m' or
    'event_time_english_1 mile' or 'event_distance_english_LJ'.
1.1. EVENTNAME must be a valid event in HyTek. If this isn't the case, the HyTek
    import will throw some kind of error.
2. Event seed times must of the form MM:SS. Any number of characters before the first
    colon are interpreted as a number of minutes, and up to the next two characters
    after the first colon are interpreted as a number of seconds.

"""
import argparse
import csv

def to_individual_record(d):
    result = dict()
    
    # Apply value character limits
    result = result
    return result


def to_information_record(d):
    result = dict(
        type="I",
        last_name=d["Last name"],
        first_name=d["First name"],
        initial="",
        gender="Female" if d["Gender"] == "Female" else "M",
        birth_date="",
        team_code=d["Team Name"],
        team_name=d["Team Code"],
        age="",
        school_year="",
        address_line_1="",
        address_line_2="",
        city="",
        state="",
        zip="",
        country="",
        citizen_country="",
        home_phone="",
        office_phone="",
        fax_number="",
        shirt_size="",
        registration_number="",
        competitor_number="",
        email="",
        disabled_classification=""
    )
    # Apply value character limits
    result = result
    return result

def to_hytek(result):
    information_record = to_information_record(result)

    for k,v in result.items():
        if k.startswith("event-"):
            # get individual record
        else:
            # pass
    
    return [

    ]

if __name__ == "__main__":
    P = argparse.ArgumentParser()
    P.add_argument("--infile", required=True,
        help="Webscorer export to be converted")
    P.add_argument("--outfile",
        help="File to write output to. Defaults to INFILE-hytek.txt")
    args = P.parse_args()

    # Creates a [results], a list where each entry is a dictionary whose keys are the
    # column names in the WebScorer file.
    with open(args.infile, "r+", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter="\t")
        results = [row for row in reader]

    # Manipulate [results] into a form we can easily write to the HyTek file.
    hytek_results = []
    for result in results:
        hytek_results += to_hytek(result)


    
    outfile = f"{args.infile}".replace(".txt", "hytek.txt") if args.outfile is None else args.outfile
    with open(outfile, "w+") as f:



    