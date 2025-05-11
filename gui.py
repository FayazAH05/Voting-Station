"""
Graphical User Interface for the voting station app used PyQT6
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QApplication, QHBoxLayout
from logic import Candidate
from logic import VoteManager
from storage import save_vote, load_all_votes
import matplotlib.pyplot as plt
import sys

class MainWindow(QWidget):

    """
    Main place for the voting window interface
    """

    def __init__(self) -> None:

        """
        :return: None
        """

        super().__init__()
        self.setWindowTitle("Voting Station")

        # Candidate Data
        self.candidates: list[Candidate] = [
            Candidate(1, "Bianca"),
            Candidate(2, "Edward"),
            Candidate(3, "Felicia")
        ]
        self.vote_manager = VoteManager(self.candidates)

        self.format = QVBoxLayout()

        # Voter Name Input
        self.NameLabel = QLabel("Input Name:")
        self.format.addWidget(self.NameLabel)
        self.NameInput = QLineEdit()
        self.format.addWidget(self.NameInput)

        # Instruction Label
        self.InstructionLabel = QLabel("Input your name, Choose a candidate, then proceed to 'Submit Vote'.")
        self.format.addWidget(self.InstructionLabel)

        # Vote Buttons
        self.VoteButtons = []
        self.SelectedCandidateID = None

        # Candidate Buttons
        for candidate in self.candidates:
            button = QPushButton(f"Select {candidate.name}")
            button.clicked.connect(lambda _, c=candidate: self.SelectCandidate(c.id))
            self.format.addWidget(button)
            self.VoteButtons.append(button)

        # Submit Vote Button
        self.SubmitButton = QPushButton("Submit Vote")
        self.SubmitButton.setEnabled(False)  # Disabled initially
        self.SubmitButton.clicked.connect(self.CastVote)
        self.format.addWidget(self.SubmitButton)

        # Clear Name Button
        self.ClearButton = QPushButton("Clear Name")
        self.ClearButton.clicked.connect(self.ClearName)
        self.format.addWidget(self.ClearButton)

        # Show Results Button
        ResultButton = QPushButton("Bar Graph Results")
        ResultButton.clicked.connect(self.ShowResults)
        self.format.addWidget(ResultButton)

        # Exit Button
        ExitButton = QPushButton("Exit")
        ExitButton.clicked.connect(self.close)
        self.format.addWidget(ExitButton)

        self.setLayout(self.format)

    def SelectCandidate(self, CandidateID: int) -> None:

        """
        This is where it chooses a candidate off the id provided

        :param CandidateID: Chosen by the voter
        :return:none
        """

        self.SelectedCandidateID = CandidateID
        VoterName = self.NameInput.text().strip()

        if VoterName:
            self.SubmitButton.setEnabled(True)

        self.InstructionLabel.setText(f"Chosen ID: {CandidateID}")

    def CastVote(self) -> None:

        """
        This is where the vote is being put in after its determined valid
        :exception: Used for just in case some error occurs in some way
        :return:none
        """

        VoterName = self.NameInput.text().strip()

        if not VoterName:
            QMessageBox.warning(self, "Invalid Input", "Input a name before moving further.")


        if self.SelectedCandidateID is None:
            QMessageBox.warning(self, "No Selection", "Choose a candidate before moving further.")
            return

        try:
            CandidateName = next(c.name for c in self.candidates if c.id == self.SelectedCandidateID)
            self.vote_manager.vote(self.SelectedCandidateID)
            save_vote(VoterName, self.SelectedCandidateID, CandidateName)

            self.InstructionLabel.setText("Vote recorded Click 'Clear Name' for next person.")
            self.SubmitButton.setEnabled(False)  # Disable after vote
            self.SelectedCandidateID = None

        except Exception as e:
            QMessageBox.critical(self, "Error has occurred", str(e))

    def ClearName(self) -> None:

        """
        This part I used essentially to just get a clear start and the buttons to be returned to original state I was having trouble with this so I used AI for this and turns out I was using the enable incorrectly
        :return:None
        """

        self.NameInput.clear()
        self.SelectedCandidateID = None
        self.InstructionLabel.setText("Input your name, Choose a candidate, then proceed to 'Submit Vote'.")
        self.SubmitButton.setEnabled(False)

    def ShowResults(self) -> None:
        """
        This takes the data that I have stored and then makes it visible by transforming it to a barchart and I got this idea from an old lab in CS1
        :exception: If for some reason chart fails I put a error message
        :return:None
        """
        try:
            vote_data = load_all_votes()
            result_counts = {c.name: 0 for c in self.candidates}

            for _, _, CandidateName in vote_data:
                if CandidateName in result_counts:
                    result_counts[CandidateName] += 1

            names = list(result_counts.keys())
            counts = list(result_counts.values())

            plt.figure(figsize=(8, 10))
            plt.bar(names, counts, color='blue')
            plt.xlabel("Candidates")
            plt.ylabel("Number of Votes")
            plt.title("Voting Results")
            plt.tight_layout()
            plt.show()

        except Exception as e:
            QMessageBox.critical(self, "Error displaying results", str(e))

