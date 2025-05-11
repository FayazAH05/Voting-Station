"""
This py is for how choosing the candidates and keeping track of the votes and how they will abide
"""

class Candidate:
    """
    Represents(Reps) a candidate in the voting station.
    """
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


    """
    :param id: This is the number associated with the candidate
    :param name: The actual name of the candidate
    
    """

class VoteManager:
    """
    This takes in account of the votes for the listed candidates
    """
    def __init__(self, candidates: list[Candidate]) -> None:
        self.candidates = {c.id: c for c in candidates}
        self.VoteCounts = {c.id: 0 for c in candidates}

        """
        :param candidates: list of candidates objects to initialize the manager with  
        
        """

    def vote(self, CandidateID: int) -> None:
        if CandidateID not in self.VoteCounts:
            raise ValueError("Invalid candidate ID.")
        self.VoteCounts[CandidateID] += 1

        """
        This is where it actually takes place where the vote is registered for a candidate
        
        :param CandidateID: ID number for the one that being voted for
        :return: None
        
        """
