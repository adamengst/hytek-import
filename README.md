# Webscorer to HyTek Importer
Contains a script that can import Webscorer race seed results to a format parsable by HyTek. The script does no error checking and its output should be transparent to the input. Any errors should come from HyTek.

## Usage
```
python RaceResultsManipulation.py --infile WEBSCORER_EXPORT --outfile OUTPUT_FILE
```

## Python
This script requires Python 3.8 or later. If you need to install Python, use Miniconda.

## WEBSCORER FORMAT RULES:
1. Required keys are:
    - `Last name`
    - `First name`
    - `Gender`—only `Male` and `Female` are options 😠
    - `Team Name`—defaults to `Unattached`
    - `Team Code`—at most four characters, defaults to `UNA`
    - `Age`
    - `Email`
2. In Webscorer, event titles must be of the form
    `event_time/distance_metric/english_EVENTNAME`, eg. `event_time_metric_100m` or
    `event_time_english_1MILE` or `event_distance_english_LJ`.
3. `EVENTNAME` must be a valid event in HyTek. If this isn't the case, the HyTek
    import will throw some kind of error.
4. ~Event seed times must of the form `MM:SS`. Any number of characters before the first
    colon are interpreted as a number of minutes, and up to the next two characters
    after the first colon are interpreted as a number of seconds.~

## TODOS
- Add value character limits
- Add documentation