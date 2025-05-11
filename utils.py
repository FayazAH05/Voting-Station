def validate_candidate_id(CandidateId: int, ValidIds: list[int]) -> bool:

    """
    This essentially is here to functions for the validation.
    I used ChatGPT for this because I wanted it be in a separate file so that it's easier to call on
    :param CandidateId: Takes ID for Validation
    :param ValidIds: List of Valid ID's
    :return:True if CandidateId exists in ValidIds, else False
    """

    return CandidateId in ValidIds
