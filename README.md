# Bitsquat

Simple script that prints _valid unregistered_ bitsquat domains. Also prints _valid registered_ and counts _invalid_ bitsquat domains. 

## Usage 
Edit `domain_name = "mydomain.foo"`  
`python bitsquat.py`

## Dependencies
`pip install -r requirements.txt`

## Domains
List of valid top-level domains maintained by [IANA](https://www.icann.org/resources/pages/tlds-2012-02-25-en)

# Acknowledgement

Thanks to [anderbw](https://github.com/anderbw) for showing the [2011 Blackhat whitepaper on bitsquatting](http://media.blackhat.com/bh-us-11/Dinaburg/BH_US_11_Dinaburg_Bitsquatting_WP.pdf) 
also described by Artem Dinaburg on his [webpage](http://dinaburg.org/bitsquatting.html). Thanks to [thepacketgeek](https://gist.github.com/thepacketgeek/6928674#file-10-dns-query-py) for the DNS query. 
