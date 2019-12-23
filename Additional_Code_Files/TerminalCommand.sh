#Loop command to automate python code and data consolidation

#Loop command to merge all file with same year to one
for((fname=1874;fname<1902;fname++)); do  cat /Users/myriam/tac/venv/data/txt/Lkn_$fname*.txt > /Users/myriam/tac/module3/Lkn$fname.txt;done

# Command to check emptyness of file and delete them
find . -type f -empty -delete

# Loops to apply filter.py on each yearly file + wordcloud creation
for((fname=1903;fname<1980;fname++)); do  /Users/myriam/tac/venv/bin/python3.7 /Users/myriam/tac/module3/filter.py $fname;done
for((fname=1874;fname<1902;fname++)); do wordcloud_cli --text module3/${fname}Lkn_keywords.txt --imagefile module3/Lkn${fname}.png --width 2000 --height 1000; done

#Loop to apply NER.py on each yearly file and second, add tag ORG to CSV file produced
for((fname=1847;fname<1849;fname++)); do/Users/myriam/tac/venv/bin/python3.7 /Users/myriam/tac/module3/ner.py search ORG $fname;done 
for((fname=1849;fname<1980;fname++)); do awk -F"," 'BEGIN { OFS = "," } ; {$3=« ORG » OFS $3; print}' ORG$fname.csv >$fnameORG.csv ; done

#loop on each yearly file to count word frequency and merge all yearly file to a unique one
for((fname=1847;fname<1905;fname++));do /Users/myriam/tac/venv/bin/python3.7 /Users/myriam/tac/module2/freq.py $fname;done
cat *WordsFreq1.csv > WordsFreqAll.csv

#for all files produced and merge to the unique one, delete
for((fname=1849;fname<1980;fname++)); do rm -f ${fname}LOC.csv ;done
