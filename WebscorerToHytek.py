"""Script to create a HyTek-formatted .txt file from a WebScorer-created .txt file.
"""
import argparse
import csv

def get_team_code(team_name):
    """Returns the team code from [team_name]."""
    try:
        first_parens_idx = team_name.index("(")
        last_parens_idx = team_name.index(")")
        return team_name[first_parens_idx+1:last_parens_idx]
    except:
        return None

def remove_team_code_from_team_name(team_name):
    """Returns team name [team_name] without the team code parenthetical."""
    team_code = get_team_code(team_name)
    if team_code is None:
        return team_name
    else:
        return team_name.replace(f"({get_team_code(team_name)})", "").strip()

def flatten_list(l):
    """Flattens list-of-lists [l] to a list."""
    result = []
    for l_ in l:
        result += l_
    return result

def get_gender_abbreviation(gender):
    """Returns the gender abbreviation for [gender]."""
    if gender == "Female":
        return "F"
    elif gender == "Male":
        return "M"
    else:
        return "M" # Change this when possible

def event_to_measure(event):
    """Returns the gender abbreviation for [gender]."""
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
        gender=get_gender_abbreviation(d["Gender"]),
        birth_date="",
        team_code=get_team_code(d["team_name"]),
        team_name=remove_team_code_from_team_name(d["team_name"]),
        age=d["Age"],
    )
    return result

def to_individual_record(d, event_name):
    result = dict(
        type="D",
        last_name=d["Last name"],
        first_name=d["First name"],
        initial="",
        gender=get_gender_abbreviation(d["Gender"]),
        birth_date="",
        team_code=get_team_code(d["team_name"]),
        team_name=remove_team_code_from_team_name(d["team_name"]),
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

if __name__ == "__main__":
    P = argparse.ArgumentParser()
    P.add_argument("--webscorer", required=True,
        help="Webscorer export to be converted")
    P.add_argument("--hytek",
        help="File to write output to. Defaults to webscorer_hytek.txt")
    args = P.parse_args()

    # Creates a [results], a list where each entry is a dictionary whose keys are the
    # column names in the WebScorer file.
    with open(args.webscorer, "r+", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter="\t")
        results = [row for row in reader]

    # Manipulate [results] into a form we can easily write to the HyTek file.
    hytek_results = [[to_individual_record(r, k) for k,v in r.items() if k.startswith("event_") and not v == ""] for r in results]
    hytek_results = flatten_list(hytek_results)
    hytek_results += [to_information_record(r) for r in results]
    hytek_results = [[v for v in h.values()] for h in hytek_results]

    hytek = f"{args.webscorer}".replace(".txt", "_hytek.txt") if args.hytek is None else args.hytek
    with open(hytek, "w+", newline="\r\n") as f:
        writer = csv.writer(f, delimiter=";")
        for row in hytek_results:
            writer.writerow(row)



    
