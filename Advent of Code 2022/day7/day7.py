input = open('day7input.txt')
class File:
    def __init__(self,size,name,parent):
        self.size = size
        self.name = name
        self.parent = parent
        self.type = 'file'
class Directory:
    def __init__(self,size,name,containsfiles,containsdirs,parent):
        self.size = size
        self.name = name
        self.containsfiles = containsfiles
        self.containsdirs = containsdirs
        self.parent = parent
        self.type = 'dir'
filesystem = []
for commands in input:
    if 'dir' in commands:
        fmt = commands.split('dir ')
        name = fmt[1] = fmt[1].replace('\n','')
        filesystem.append(Directory(0,str(name),[],[],''))
    if 'dir' not in commands and '$' not in commands:
        fmt = commands.split(' ')
        name = fmt[1]=fmt[1].replace('\n','')
        size = fmt[0] = int(fmt[0])
        # print(size)
        filesystem.append(File(size,name,''))
for item in filesystem:
    print(item.type, item.name, item.size, item.parent)