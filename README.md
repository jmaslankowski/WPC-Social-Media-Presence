# WPC-Social-Media-Presence STARTER KITT
GUIDELINES HOW TO START TO WORK WITH APPLICATION<br/>
<br/>

1. QUICK START OF THE APPLICATION<br/>

1.1. STANDALONE VERSION<br/>
<b>SocialMediaCollectorApp.py<br/>
which is a standalone application that can be used by the following command in command line interface:<br/>
<b>python SocialMediaCollectorApp.py<br/></b>
or just double-click on application in Graphical User Interface mode.<br/>
<br/>

1.2. PYTHON LIBRARY VERSION<br/>
The file to clone is:<br/>
<b>SocialMediaCollector.py<br/></b>
which is a library that can be used by the following code in Python:<br/>
To use in your own application - please import this way:<br/>
<br/>
  <b>import SocialMediaPresenceCollector as smpc<br/></b>
<br/>
then start the application this way<br/>
<br/>
<b>smpsk=smpc.SocialMediaPresenceStarterKitt()<br/></b>
<br/>
<b>smpsk.start()<br/></b>
<br/><br/>

2. INPUT FILES<br/>
The application is used to scrape all the links related to social media from websites that are put in:<br/>
url.txt<br/>
file that should have the list of URLs in the following format:<br/>
maslankowski.pl<br/>
http://stat.gov.pl<br/>
www.ug.edu.pl
<br/><br/>

3. OUTPUT FILES<br/>
The output of the application are two files:
<b>wpc_social.csv</b>
and
<b>wpc_social_YYYYMMDDHHMMSSnnnnnnn.json</b>
<br/><br/>
The file <b>wpc_social.csv</b> is updated with its content. 
<br/><br/>
The json file is created every time of the application running.
<br/><br/>
To start using the software, you should download Python source file and execute like this:<br/>
<b>python3 SocialMediaCollectorApp.py</b><br/>
or in selected MS Windows environment<br/>
<b>py SocialMediaCollectorApp.py</b>
<br/><br/>

4. PREREQUISITES - HOW TO SET UP THE PYTHON ENVIRONMENT<br/>
<br/>
Both the library as well as the application are using Python 3. You can install Python 3 from the following location: http://python.org, however recommended version is to install Anaconda environment that is available here: http://www.anaconda.com.<br/><br/>
Remember to use only Python version 3 - on Python 2 the application will not work.
<br/><br/>

<font color="red">IMPORTANT! Libraries <b>bs4</b> and <b>requests</b> are necessary. Depending on your Python environment try to install them that way:<br/>
easy_install bs4<br/>
easy_install requests<br/>
OR<br/>
pip3 install bs4<br/>
pip3 install requests<br/>
OR<br/>
pip install bs4<br/>
pip install requests<br/>
OR<br/>
python -m pip install bs4<br/>
python -m pip install requests<br/>
OR<br/>
python3 -m pip install bs4<br/>
python3 -m pip install requests<br/>
OR<br/>
conda install bs4<br/>
conda install requests<br/>
</font>
<br/>
<br/><br/>
General Overview of the 4 steps:<br/>
<b>(1) Collecting Social Media links</b><br/>
SocialMediaCollectorApp<br/>
<b>(2) Collecting Tweets for training and testing purposes</b><br/>
WP2_Step2a_CollectingTweetsByKeyword<br/>
WP2_Step2b_CollectingTweetsByEnterprise<br/>
<b>(3) Training and testing a dataset</b><br/>
WP2_Step3_PurposeOfSocialMediaPresence<br/>
<b>(4) Apply the data to check enterprise main purpose of SMP</b><br/>
WP2_Step4_PurposeOfSocialMediaPresence<br/>
<br/><br/>
