"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    res=[]
    with open(neo_csv_path) as csv_file:
        load_neo = csv.DictReader(csv_file)
        for each_line in load_neo :
            res.append(NearEarthObject(designation = each_line['pdes'],name=each_line['name']  , hazardous=each_line['pha'] , diameter =each_line['diameter']))
    

    return res


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    res = []
    with open(cad_json_path) as json_file:
        load_approache = json.load(json_file)
        load_approache = [dict(zip(load_approache["fields"], data)) for data in load_approache["data"]]
        for each_line in load_approache:
            res.append(CloseApproach(designation=each_line['des'], time=each_line['cd'], distance=each_line['dist'], velocity=each_line['v_rel']))


    return res
