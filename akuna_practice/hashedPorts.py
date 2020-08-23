#!/usr/bin/env python3

import time
from collections import deque

class Solution:

    def sentTimes(self, numberOfPorts:int , transmissionTime:int, packetIds: list):
        ans, t = [], 1
        avail = [0] * numberOfPorts
        queue = deque()
        for pid in packetIds:
            # pop from queue if the port is available
            while queue and avail[queue[0]] <= t:
                queue.popleft()

            # if no ports available, wait until there is one available
            if len(queue) == numberOfPorts:
                t = avail[queue.popleft()]

            # try port until find one available
            port = pid % numberOfPorts
            while avail[port] > t:
                port = (port + 1) % numberOfPorts
                
            # send packet, update available time for the port
            avail[port] = t + transmissionTime
            queue.append(port)
            ans.append(port)
            t += 1
        return ans




if __name__ == "__main__":
    start_time = time.time()
    s = Solution()
    print(s.sentTimes(5, 10, [1,2,3,4,5,6]))
    print(s.sentTimes(5, 2, [5,1,6,2,7,3]))
    print("--- %.8f seconds ---" % (time.time() - start_time))