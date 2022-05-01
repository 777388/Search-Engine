# Search-Engine
Iterates over all IPv4 addresses, subdomain enumerates over hostname, then grabs all urls from each subdomain and saves each to file. Multithreading set to 255. May want to go through Sublist3r and delete all the error notifications

Requires Sublist3r and GAU

https://github.com/aboul3la/Sublist3r

https://github.com/lc/gau

Usage: python3 ipaddresses.py

Be sure to move the ipaddresses file within the folder that contains the Sublist3r folder as it uses Sublist3r/sublist3r.py for the targetting.
