import os
class Tool:

    def cleanDir(self, dir, ext, clean= False):
        if clean:
            for folderName, _, filenames in os.walk(dir):
                for filename in filenames:
                    if filename.endswith(ext) == False:
                        os.unlink(folderName + '/'+ filename)
