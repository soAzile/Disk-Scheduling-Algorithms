from diskUtil import DiskSchd


class FCFS(DiskSchd):
    """First-Come-First-Serve Disk Scheduling Algorithm"""

    def __init__(self):
        super().__init__()

    def scheduleRequest(self):
        for req in self.requests:
            self._seek_time += abs(req - self.head)
            self._req_seq.append(req)

            self.head = req


if __name__ == '__main__':

    print('----FCFS Disk Scheduling----')

    algo = FCFS()

    algo.scheduleRequest()
    algo.getStats()
    algo.getPlot(algo.__class__.__name__)