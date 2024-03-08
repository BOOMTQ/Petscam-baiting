# PetScam-baiting
An Automated Response System for Disrupting Online Pet Scamming

## Project overview
The online pet scam is an increasingly sophisticated threat that can cause emotional and financial distress to victims. To aid the public in identifying and avoiding such pet scams, this project aims to develop an automated response system that wastes scammers' time and resources. Using web scraping, fake profiles, data analysis and visualization technologies, this system will leave contact information on various pet scam websites' contact pages, and engage scammers in prolonged conversations based on different scam-baiting templates. According to the statistical analysis of quantity, conversation, and time metrics as three types of quantitative metrics, we can reveal and optimize the most effective scam-baiting strategies. Ultimately, by reducing scammers' return on investment, the system can mitigate these harmful frauds and protect potential victims.

## Pet scam websites
On https://petscams.com/, which have listed known pet scam and delivery scam websites, is still in real-time updates.

## Four different personalities (generated by gpt-3.5 prompt)
1. Newbies with no experience in pet adoption and trading
2. Bargainers
3. The Curious Investigator
4. The Impatient Enthusiast

## Project execution process
The complete execution process of the entire project is as follows:
1. To get pet scam websites: run ./crawler/petscams/petscam_crawl.py, then run ./crawler/petscams/contactpage-crawler.py
2. To automatedly fill in the contact form: run ./crawler/formfill_crawler.py 
3. Waiting for the scam emails from pet scammers...
4. Fetching the received scam emails and automatedly sending bait emails: run ./corn.py
5. According to the email conversations of each repliers saved in ./emails/archive. Count the difference in timestamp and comparatively analyse the time wasted by scammers at different repliers.

## Essential resources
1. Github Student Developer Pack on https://education.github.com/pack, in order to use tools like name.com and mailgun for free:
  - mailgun by PATHWIRE: APIs that enable you to send, receive and track 20,000 free emails and get 100 free email validations every month for up to 12 months.
  - name.com: Apply a domain name.
2. Three months API access of gpt-3.5-turbo-0125 model, provided by UoB. 

