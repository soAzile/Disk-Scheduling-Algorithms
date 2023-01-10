from diskUtil import DiskSchd


class SSTF(DiskSchd):

    def __init__(self):
        super().__init__()

    def scheduleRequest(self):

        n = len(self.requests)
        visited = [False] * n

        while n:
            minDis = 99999
            pos = None

            for idx, req in enumerate(self.requests):
                if abs(self.head - req) < minDis and not visited[idx]:
                    minDis = abs(self.head - req)
                    pos = idx

            self._seek_time += minDis
            self.head = self.requests[pos]

            visited[pos] = True

            self._req_seq.append(self.requests[pos])
            n -= 1


if __name__ == '__main__':
    print('----SSTF Disk Scheduling----')

    algo = SSTF()

    algo.scheduleRequest()
    algo.getStats()
    algo.getPlot(algo.__class__.__name__)