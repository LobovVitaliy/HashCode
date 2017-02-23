import os, sys
class Cache(object):
    def __init__(self, arglist):
        self.number = arglist[0]
        self.latency = arglist[1]
    def __str__(self):
        return self.number + " " + self.latency


class Endpoint(object):
    def __init__(self, arglist):
        self.latency = arglist[0]
        self.count = arglist[1]
        self.caches = [Cache(i) for i in arglist[2]]

file = open("in.in", "r")
video = file.readline()
endpoint = file.readline()
request = file.readline()
caches = file.readline()
size = file.readline()
videos = file.readline().split()
endpoints = []
print (endpoint)
for i in range(int(endpoint)):
    endpoints.append(file.readline().split())
    count = endpoints[i][1]
    endpoints[i].append([file.readline().split() for j in range(int(count))])

print (endpoints)
endpoints_class = Endpoint(endpoints[0])

print ([i.__str__() for i in endpoints_class.caches])
