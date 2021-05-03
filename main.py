from requests.exceptions import ConnectionError, TooManyRedirects
from savepagenow.exceptions import WaybackRuntimeError
import savepagenow

yahoo_urls = open('yahoo_links.txt', 'r')
linksx = yahoo_urls.readlines()

# The file to store links
wayback = open('wayback.txt', 'a')

# File for missing links
wayback_errors = open('wayback_errors.txt', 'a')

for line in linksx:
    # This is to remove the \n at the end of each line (since we are using a text file)
    l = len(line)
    y_url = line[:l - 1]

    # Try to catch errors
    x = 0
    for x in range(4):
        try:
            k = savepagenow.capture_or_cache(y_url)
            print(k[0])
            r = k[0]
            wayback.write(r + '\n')
            break
        # This will handle wayback errors
        except WaybackRuntimeError as error:
            print(error)
            wayback_errors.write(line)
            wayback_errors.write('\n')
            print("error in: " + line + '\n')
            break
        except ConnectionError:
            wayback_errors.write("connection error in: " + line + '\n')
            print("conection error in: " + line + '\n')
            x = x + 1
        except TooManyRedirects:
            wayback_errors.write("too_many_redirects error in: " + line + '\n')
            print("too_many_red error in: " + line + '\n')
            x = x + 1
