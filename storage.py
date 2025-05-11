"""
Saves the voting records and loads the records to the CSV File
"""

import csv
from typing import List, Tuple

def save_vote(VoterName: str, CandidateID: int, CandidateName: str) -> None:

    """

    :param VoterName: Name of the person thats voting
    :param CandidateID: ID of the voted person
    :param CandidateName:Name of the voted Candidate
    :return:None
    """


    try:
        with open("votes.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([VoterName, CandidateID, CandidateName])
    except IOError as e:
        raise RuntimeError("Could not save vote.") from e



def load_all_votes() -> List[Tuple[str, int, str]]:

    """

    :return: List out the tuples that contain(VoterName,CandidateID,CandidateName)
    """
    "This is where I used AI I couldn't really I got stuck and ask to list out ways and I decided on tuple since it seemed the simplest bc it showed me some code similar to below"


    try:
        with open("votes.csv", "r", newline='') as file:
            reader = csv.reader(file)
            return [(row[0], int(row[1]), row[2]) for row in reader if row]
    except FileNotFoundError:
        return []
    except Exception as e:
        raise RuntimeError("Couldn't Load Votes") from e


