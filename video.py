class Cache:
    def __init__(self, video, max_size, cache_time):
        self.video = video
        self.max_size = max_size
        self.cache_time = cache_time

class EndPoint:
    cache = []

    def __init__(self, req, time):
        self.req = req
        self.time = time

class Request:
    def __init__(self, count, v_id, endpoint):
        self.count = count
        self.v_id = v_id
        self.endpoint = endpoint

class Video:
    def __init__(self, v_id, size):
        self.v_id = v_id
        self.size = size
