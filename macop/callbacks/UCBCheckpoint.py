"""UCB policy Checkpoint class implementation
"""

# main imports
import os
import logging
import numpy as np
import pkgutil

# module imports
from .Callback import Callback
from ..utils.color import macop_text, macop_line


class UCBCheckpoint(Callback):
    """
    UCB checkpoint is used for loading previous UCB data and start again after loading checkpoint
    Need to be the same operators used during previous run

    Attributes:
        algo: {Algorithm} -- main algorithm instance reference
        every: {int} -- checkpoint frequency used (based on number of evaluations)
        filepath: {str} -- file path where checkpoints will be saved
    """
    def run(self):
        """
        Check if necessary to do backup based on `every` variable
        """
        # get current population
        currentEvaluation = self.algo.getGlobalEvaluation()

        # backup if necessary
        if currentEvaluation % self.every == 0:

            logging.info("UCB Checkpoint is done into " + self.filepath)

            with open(self.filepath, 'w') as f:

                rewardsLine = ''

                for i, r in enumerate(self.algo.policy.rewards):
                    rewardsLine += str(r)

                    if i != len(self.algo.policy.rewards) - 1:
                        rewardsLine += ';'

                f.write(rewardsLine + '\n')

                occurrencesLine = ''

                for i, o in enumerate(self.algo.policy.occurrences):
                    occurrencesLine += str(o)

                    if i != len(self.algo.policy.occurrences) - 1:
                        occurrencesLine += ';'

                f.write(occurrencesLine + '\n')

    def load(self):
        """
        Load backup lines as rewards and occurrences for UCB
        """
        if os.path.exists(self.filepath):

            logging.info('Load UCB data')
            with open(self.filepath) as f:

                lines = f.readlines()
                # read data for each line
                rewardsLine = lines[0].replace('\n', '')
                occurrencesLine = lines[1].replace('\n', '')

                self.algo.policy.rewards = [
                    float(f) for f in rewardsLine.split(';')
                ]
                self.algo.policy.occurrences = [
                    float(f) for f in occurrencesLine.split(';')
                ]

            print(
                macop_text(
                    'Load of available UCB policy data from `{}`'.format(
                        self.filepath)))

        else:
            print(macop_text('No UCB data found, use default UCB policy'))
            logging.info("No UCB data found...")

        print(macop_line())
