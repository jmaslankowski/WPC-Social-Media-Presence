# WP2-Social-Media-Presence
Development stage of application for WP2 purposes.
<br/><br/>
General Overview of the 4 steps:<br/>
<b>(1) Collecting Social Media links</b><br/>
WP2_SocialMediaPresence_Dev<br/>
<b>(2) Collecting Tweets for training and testing purposes<br/>
WP2_Step2a_CollectingTweetsByKeyword</b><br/>
WP2_Step2b_CollectingTweetsByEnterprise<br/>
<b>(3) Training and testing a dataset</b><br/>
WP2_Step3_PurposeOfSocialMediaPresence<br/>
<b>(4) Apply the data to check enterprise main purpose of SMP</b><br/>
WP2_Step4_PurposeOfSocialMediaPresence<br/>
<br/><br/>
The application is used to scrape all the links related to social media from websites that are put in:<br/>
url.txt<br/>
file that should have the list of URLs in the following format:<br/>
maslankowski.pl<br/>
http://stat.gov.pl<br/>
www.ug.edu.pl
<br/><br/>
The output of the application are two files:
<b>wp2_social.csv</b>
and
<b>wp2_social_YYYYMMDDHHMMSSnnnnnnn.json</b>
<br/><br/>
The file <b>wp2_social.csv</b> is updated with its content. 
<br/><br/>
The json file is created every time of the application running.
<br/><br/>
To start using the software, you should download Python source file and execute like this:<br/>
<b>python3 WP2_SocialMediaPresence_Dev.py</b><br/>
or in selected MS Windows environment<br/>
<b>py WP2_SocialMediaPresence_Dev.py</b>
<br/><br/>
IMPORTANT! Libraries <b>bs4</b> and <b>requests</b> are necessary. Depending on your Python environment try to install them that way:<br/>
easy_install bs4<br/>
easy_install requests<br/>
OR<br/>
pip3 install bs4<br/>
pip3 install requests<br/>
OR<br/>
pip install bs4<br/>
pip install requests<br/>
