from diskUtil import DiskSchd


class C_SCAN(DiskSchd):
    """Circular SCAN Disk Scheduling Algorithm"""

    def __init__(self):
        super().__init__(direction=True)

    def scheduleRequest(self):

        DIREC = self.getDirec
        DISK_SIZE = self.getDiskSize()

        left, right = [], []
        for req in self.requests:
            left.append(req) if req < self.head else right.append(req)

        left.append(0)
        right.append(DISK_SIZE - 1)

        def addTrack(track: int) -> None:
            self._req_seq.append(track)
            self._seek_time += abs(self.head - track)
            self.head = req

        left.sort()
        right.sort()

        if DIREC == 'L':
            for req in reversed(left):
                addTrack(req)

            self.head = right[-1]
            self._seek_time += DISK_SIZE - 1

            for req in reversed(right):
                addTrack(req)

        elif DIREC == 'R':
            for req in right:
                addTrack(req)

            self.head = left[0]
            self._seek_time += DISK_SIZE - 1

            for req in left:
                addTrack(req)


if __name__ == '__main__':
    print('----Circular SCAN Disk Scheduling----')

    algo = C_SCAN()

    algo.scheduleRequest()
    algo.getStats()
    algo.getPlot(algo.__class__.__name__, algo.dsize)