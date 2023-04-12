from txtfileOperations import txtop

def app():
    a = txtop()
    #a.countWord()
    #a.StartingAlphaCount()
    #a.fiterWords()
    a.DBTablecreate()
    a.Zip_store()
    #a.fetch_db_data()



if __name__ == "__main__" :
    app()
