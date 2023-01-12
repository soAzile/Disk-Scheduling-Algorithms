from diskUtil import DiskSchd


class C_LOOK(DiskSchd):

    def __init__(self):
        super().__init__(direction=True)

    def scheduleRequest(self):
        DIREC = self.getDirec
        DISK_SIZE = self.getDiskSize()

        left, right = [], []
        for req in self.requests:
            left.append(req) if req < self.head else right.append(req)

        left.sort()
        right.sort()

        def addTrack(track: int) -> None:
            self._req_seq.append(track)
            self._seek_time += abs(track - self.head)
            self.head = track

        if DIREC == 'L':
            for req in reversed(left):
                addTrack(req)

            self._seek_time += abs(self.head - right[-1])
            self.head = right[-1]

            for req in reversed(right):
                addTrack(req)

        elif DIREC == 'R':
            for req in right:
                addTrack(req)

            self._seek_time += abs(self.head - left[0])
            self.head = left[0]

            for req in left:
                addTrack(req)


if __name__ == '__main__':
    print('----Circular LOOK Disk Scheduling----')

    algo = C_LOOK()

    algo.scheduleRequest()
    algo.getStats()
    algo.getPlot(algo.__class__.__name__, algo.dsize)
