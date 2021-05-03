import savepagenow

from savepagenow.exceptions import WaybackRuntimeError

yahoo_urls = open('yahoo_links.txt', 'r')
linksx = yahoo_urls.readlines()

#The file to store links
wayback = open('wayback.txt', 'a')

#File for missing links
wayback_errors = open('wayback_errors.txt', 'a')

for line in linksx:
    #This is to remove the \n at the end of each line (since we are using a text file)
    l = len(line)
    y_url = line[:l-1]

    #Try to catch errors
    try:
        k = savepagenow.capture_or_cache(y_url)
        print(k[0])
        r = k[0]
        wayback.write(r+'\n')
    #This will handle wayback errors
    except WaybackRuntimeError as error:
        print(error)
        wayback_errors.write(line)
        wayback_errors.write('\n')
        print("error en: "+line+'\n')
