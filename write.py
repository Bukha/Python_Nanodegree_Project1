"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import helpers


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    with open(filename, 'w', newline='') as csv_out:
        filtered_writer = csv.writer(csv_out)
        filtered_writer.writerow(fieldnames)
        for line in results:
            filtered_writer.writerow([line.time,
                                      line.distance,
                                      line.velocity,
                                      line.neo.designation,
                                      line.neo.name,
                                      line.neo.diameter,
                                      line.neo.hazardous])


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    res = []

    for line in results:
        res.append({
            "datetime_utc": helpers.datetime_to_str(line.time),
            "distance_au": line.distance,
            "velocity_km_s": line.velocity,
            "neo": {
                "designation": line.neo.designation,
                "name": line.neo.name,
                "diameter_km": line.neo.diameter,
                "potentially_hazardous": line.neo.hazardous
            }

        })

    with open(filename, 'w') as json_out:
        json.dump(res, json_out, indent=2)
