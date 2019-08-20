import shutil
import os
import random


folder_out = os.getcwd() + "/trainingdata"
os.chdir(folder_out)
files = os.listdir(folder_out)
txtFiles = [f for f in files if f.endswith(".txt")]
# random.shuffle(txtFiles)
#
# for i in range(395):
#     print(txtFiles[i])
#     shutil.move(txtFiles[i],'/home/riley/Documents/Github/Dissertation-2019/trainingdata395')
#     shutil.move(txtFiles[i].replace('.txt','.pdf'), '/home/riley/Documents/Github/Dissertation-2019/trainingdata395')




for txtFile in txtFiles:

    count = 0
    textsize = round(os.path.getsize(txtFile)/float(1024), 2)
    # print(textsize)
    with open(txtFile, 'r') as f:
        dictResult = {}

        # Find the letters each line
        for line in f.readlines():
            listMatch = re.findall('[0-9]+', line)

            # Count
            for eachLetter in listMatch:
                eachLetterCount = len(re.findall(eachLetter, line))
                count += eachLetterCount
