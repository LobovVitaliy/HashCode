import video


class DataCenter:

    videos = []
    caches = []
    end_points = []

    def __init__(self, arg_list):
        self.videos_count = arg_list[0]
        self.end_count = arg_list[1]
        self.request_count = arg_list[2]
        self.cache_count = arg_list[3]
        self.cache_size = arg_list[4]

    @staticmethod
    def ParseFromFile(path):
        file = open(path, "wr+")
        dataCenter = DataCenter(file.readline())
        videos_info = file.readline().split(" ")
        for i in range(dataCenter.videos_count):
            dataCenter.videos.append(Video(i, videos_info[i]))

