# sqlite3_UCIdata-Project

Dataset : https://archive.ics.uci.edu/ml/datasets/bag+of+words
    
1. Try to find count of each of every word in the respective file. return : [(word1, count1), (word2,count2)....]
2. Try to perform a reduce operation to get a count of all the words starting with same alphabet
    sample ex : [(a, 56), (b, 67)...]
3. Try to filter out all the words from the dataset
    example : 
             .001.abstract --> abstract
             =.002 = delete --> delete
4. Create a tuple set of all the records available in all the 5 files and then store it in sqlite DB
    example : (aah, >=, fdsf, wer, ttt)
