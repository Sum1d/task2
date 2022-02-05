from dirsync import sync
import time
import datetime


def folderSynchronization(source_path, target_path, t):
    f = open('log.txt', 'a')
    while True:
        sync(source_path, target_path, 'sync', purge=True)
        now = datetime.datetime.now()
        f.write("Source: " + source_path + '\n' + "Target: " + target_path + '\n' +
                "Time: " + now.strftime("%d-%m-%Y %H:%M:%S")+'\n\n')
        time.sleep(t)
    f.close()


# if __name__ == '__main__':
#     folderSynchronization('C:/source', 'C:/replica', 20)
