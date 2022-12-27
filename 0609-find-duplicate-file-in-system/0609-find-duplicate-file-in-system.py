class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_path = defaultdict(set)
        for file in paths:
            files_object = file.split()
            path = files_object[0]
            files = files_object[1:]
            for fl in files:
                fl = fl.split("(")
                fl_name = fl[1][:-1]
                file_path[fl_name].add(path + "/" + fl[0])
                # print((path  + "/"+ fl[0]))
        output = []
        for key in file_path:
            if len(file_path[key]) > 1:
                output.append(list(file_path[key]))
        return output
            