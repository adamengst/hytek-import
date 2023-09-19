"""Script to create a HyTek-formatted .txt file from a WebScorer-created .txt file.
"""
import argparse
import csv

def get_team_code(d):
    first_parens_idx = d["team_name"].index("(")
    last_parens_idx = d["team_name"].index(")")
    return d["team_name"][first_parens_idx+1:last_parens_idx]

def flatten_list(l):
    """Flattens list-of-lists [l] to a list."""
    result = []
    for l_ in l:
        result += l_
    return result

def get_gender(d):
    if d["Gender"] == "Female":
        return "F"
    elif d["Gender"] == "Male":
        return "M"
    else:
        return "M" # Change this when possible

def event_to_measure(event):
    if "metric" in event:
        return "M"
    elif "english" in event:
        return "E"
    else:
        raise ValueError("Event names must contain either 'metric' or 'english' to indicate their measure")

def get_mark(d, event):
    if "time" in event:
        return d[event]
    elif "distance" in event:
        return d[event]
    else:
        print(event)
        raise ValueError("Event names must contain either 'time' or 'distance' to indicate what kind of mark they should have")

def event_to_code(event):
    underscore_idxs = [idx for idx,c in enumerate(event) if c == "_"]
    third_underscore_idx = underscore_idxs[2]
    return event[third_underscore_idx+1:]

def to_information_record(d):
    result = dict(
        type="I",
        last_name=d["Last name"],
        first_name=d["First name"],
        initial="",
        gender=get_gender(d),
        birth_date="",
        team_code=get_team_code(d),
        team_name=d["team_name"],
        age=d["Age"],
    )
    return result

def to_individual_record(d, event_name):
    result = dict(
        type="D",
        last_name=d["Last name"],
        first_name=d["First name"],
        initial="",
        gender=get_gender(d),
        birth_date="",
        team_code=get_team_code(d),
        team_name=d["team_name"],
        age=d["Age"],
        school_year="",
        event_code=event_to_code(event_name),
        entry_mark=get_mark(d, event_name),
        event_measure=event_to_measure(event_name),
        event_division="",
        competitor_number="",
        finish_place="",
        declaration_status="",
        entry_note="",
        not_in_use="",
        alternate="",
    )

    # Apply value character limits
    result = result
    return result

def to_hytek(result):
    """Returns
    
    Args:
    result
    """
    return [to_individual_record(result, k) for k in result.keys() if k.startswith("event_")]    

if __name__ == "__main__":
    P = argparse.ArgumentParser()
    P.add_argument("--webscorer", required=True,
        help="Webscorer export to be converted")
    P.add_argument("--hytek",
        help="File to write output to. Defaults to INFILE_hytek.txt")
    args = P.parse_args()

    # Creates a [results], a list where each entry is a dictionary whose keys are the
    # column names in the WebScorer file.
    with open(args.infile, "r+", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter="\t")
        results = [row for row in reader]

    # Manipulate [results] into a form we can easily write to the HyTek file.
    hytek_results = [[to_individual_record(r, k) for k,v in r.items() if k.startswith("event_") and not v == ""] for r in results]
    hytek_results = flatten_list(hytek_results)
    hytek_results += [to_information_record(r) for r in results]
    hytek_results = [[v for v in h.values()] for h in hytek_results]

    outfile = f"{args.infile}".replace(".txt", "_hytek.txt") if args.outfile is None else args.outfile
    with open(outfile, "w+", newline="\r\n") as f:
        writer = csv.writer(f, delimiter=";")
        for row in hytek_results:
            writer.writerow(row)



    
