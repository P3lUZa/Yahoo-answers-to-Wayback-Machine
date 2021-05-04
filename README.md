# Yahoo-answers-to-Wayback-Machine



Now that Yahoo! will close the answers site i created this program that takes a list of Yahoo answers 

.. code-block:: bash

   $ python3 main.py

Links should be in text file named "yahoo_links.txt" with the links in a list:    
 
https://answers.yahoo.com/question/index?qid=[something]  
https://answers.yahoo.com/question/index?qid=[something_2]  
https://answers.yahoo.com/question/index?qid=[something_3] 
  
  
   
Then, the program will take each page and save it to the Wayback Machine of the Internet Archive

The program will save the errors (not saved links) in wayback_errors.txt and and the wayback machine links in wayback.txt
 
The program is specially useful if you have saved links from Pocket, Wallabag or any site agreggator
 
#### The program uses the powerfull library savepagenow from pastpages
