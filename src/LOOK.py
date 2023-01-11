from diskUtil import DiskSchd


class LOOK(DiskSchd):
    """LOOK Disk Scheduling Algorithm"""

    def __init__(self):
        super().__init__(direction=True)

    def scheduleRequest(self):
        DIREC = self.getDirec
        DISK_SIZE = self.getDiskSize()

        left, right = [], []
        for req in self.requests:
            left.append(req) if req < self.head else right.append(req)

        left.sort(reverse=True)
        right.sort()

        def addTrack(track: int) -> None:
            self._req_seq.append(track)
            self._seek_time += abs(self.head - track)
            self.head = track

        run = 2
        while run:
            if DIREC == 'L':
                for req in left:
                    addTrack(req)
                DIREC = 'R'
            elif DIREC == 'R':
                for req in right:
                    addTrack(req)
                DIREC = 'L'
            run -= 1


if __name__ == '__main__':
    print('----LOOK Disk Scheduling----')

    algo = LOOK()

    algo.scheduleRequest()
    algo.getStats()
    algo.getPlot(algo.__class__.__name__, algo.dsize)