from src.diskUtil.diskPlot import plot
from abc import ABC, abstractmethod


class DiskSchd(ABC):
    """Abstract class for Disk Scheduling Algorithm"""

    _seek_time = 0
    _ini_head = None

    _req_seq = []

    def __init__(self, direction: bool = False):

        self.dsize = None
        valid_ = ('L', 'R')

        self.requests = [int(x) for x in input('Enter Requests: ').split()]
        self.head = int(input('Enter Initial Head: '))

        # If direction is required in algo
        if direction:
            self.direc = input('Enter Rotation direction (L/R): ').upper()
            if self.direc not in valid_:
                print('Invalid direction notation!')
                exit(0)

        self._ini_head = self.head

    @property
    def getDirec(self) -> str:
        """Returns direction of disk rotation."""

        return self.direc

    @abstractmethod
    def scheduleRequest(self):
        """Computes the sequence in which requests are serviced"""

        pass

    def getPlot(self, algo: str, dsize: int = None):
        """Plots the request sequence"""

        plot(self._req_seq, self._seek_time, self._ini_head, algo, dsize)

    def getStats(self):
        """Displays Request sequence and Seek time"""

        print('\n[STATS]')
        print(f'Seek Sequence: {self._req_seq}')
        print(f'Seek Time: {self._seek_time}')

    def getDiskSize(self):
        """User input for Disk Size"""

        self.dsize = int(input('Enter Disk Size: '))
        return self.dsize