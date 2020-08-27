import shelve

db = shelve.open('flaskr.db', writeback=True)

try: 
    def addEntry(key, ttl, txt):
        db[key] = {
            'title': ttl,
            'text': txt
        }
    def getTitle(i):
        t = db[i]['title']
        return t

    def getText(i):
        tx = db[i]['text']
        return  tx
    
    def setTitle(i, temp) :
        db[i]['title'] = temp


    def setText(i, temp) :
        db[i]['text']

    def getKeys() :
        l = list(db.keys())
        return l

    def isKey(i) :
        flag = i in db
        return flag
finally:
    db.close()