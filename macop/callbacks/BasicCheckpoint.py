"""Basic Checkpoint class implementation
"""

# main imports
import os
import logging
import numpy as np

# module imports
from .Callback import Callback
from ..utils.color import macop_text, macop_line


class BasicCheckpoint(Callback):
    """
    BasicCheckpoint is used for loading previous computations and start again after loading checkpoint

    Attributes:
        algo: {Algorithm} -- main algorithm instance reference
        every: {int} -- checkpoint frequency used (based on number of evaluations)
        filepath: {str} -- file path where checkpoints will be saved
    """
    def run(self):
        """
        Check if necessary to do backup based on `every` variable
        """
        # get current best solution
        solution = self.algo.bestSolution

        currentEvaluation = self.algo.getGlobalEvaluation()

        # backup if necessary
        if currentEvaluation % self.every == 0:

            logging.info("Checkpoint is done into " + self.filepath)

            solutionData = ""
            solutionSize = len(solution.data)

            for index, val in enumerate(solution.data):
                solutionData += str(val)

                if index < solutionSize - 1:
                    solutionData += ' '

            line = str(currentEvaluation) + ';' + solutionData + ';' + str(
                solution.fitness()) + ';\n'

            # check if file exists
            if not os.path.exists(self.filepath):
                with open(self.filepath, 'w') as f:
                    f.write(line)
            else:
                with open(self.filepath, 'a') as f:
                    f.write(line)

    def load(self):
        """
        Load last backup line of solution and set algorithm state (best solution and evaluations) at this backup
        """
        if os.path.exists(self.filepath):

            logging.info('Load best solution from last checkpoint')
            with open(self.filepath) as f:

                # get last line and read data
                lastline = f.readlines()[-1]
                data = lastline.split(';')

                # get evaluation  information
                globalEvaluation = int(data[0])

                if self.algo.parent is not None:
                    self.algo.parent.numberOfEvaluations = globalEvaluation
                else:
                    self.algo.numberOfEvaluations = globalEvaluation

                # get best solution data information
                solutionData = list(map(int, data[1].split(' ')))

                if self.algo.bestSolution is None:
                    self.algo.bestSolution = self.algo.initializer()

                self.algo.bestSolution.data = np.array(solutionData)
                self.algo.bestSolution.score = float(data[2])

            print(macop_line())
            print(
                macop_text('Checkpoint found from `{}` file.'.format(
                    self.filepath)))

            print(
                macop_text('Restart algorithm from evaluation {}.'.format(
                    self.algo.numberOfEvaluations)))

        else:
            print(
                macop_text(
                    'No backup found... Start running algorithm from evaluation 0.'
                ))
            logging.info(
                "Can't load backup... Backup filepath not valid in Checkpoint")

        print(macop_line())
