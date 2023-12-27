# Webscorer to HyTek Importer
Contains a script that can import Webscorer race seed results to a format parsable by HyTek. The script does no error checking, and its output should be transparent to the input. Any errors should come from HyTek. [GitHub link](https://github.com/adamengst/hytek-import).

## Online Usage (no git or Python)
1. Create a [Replit](https://replit.com/) account and get an invite from Adam.
2. Export registrations as a tab-delimited text file from Webscorer and upload to Replit.
3. Open `WebscorerToHytek.py` in the left pane, and enter the following as the **Run Command**: 
   ```
   python WebscorerToHytek.py --webscorer WEBSCORER_EXPORT --hytek OUTPUT_FILE
   ```
   where `WEBSCORER_EXPORT` is the file exported from Webscorer, and `OUTPUT_FILE` is the file that will be created in HyTek format. If `--hytek` isn't specified, the output will be `WEBSCORER_EXPORT_hytek.txt`.

## Command Line Usage (requires git and Python)
```
git clone https://github.com/adamengst/hytek-import; cd hytek-import
python WebscorerToHytek.py --webscorer WEBSCORER_EXPORT --hytek OUTPUT_FILE
```

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
    import will throw an error.

## TODOS
- none right now :-)
