Fetch Earthquake Data 
====================
  We need enough data and related earthquake event information to prepare machine learning label sets. <br>
  Here we use following two-step workflow to fetch data: <br>
  ## Make queries from [ISC Bulletin](http://isc-mirror.iris.washington.edu/iscbulletin/search/bulletin/interactive/)<br>
  `International Seismological Centre` Bulletin data contains all catalog from both reviewed(before 2017.03.01) and unreviewed events(after 2017.03.01 at present),
  it includes:<br>
  * hypocentres - both the prime (preferred) origin and secondary estimates;
  * focal mechanism solutions;
  * magnitudes;
  * phase/arrival data.<br>
  
  You can complete a search with the [interactive interface](http://isc-mirror.iris.washington.edu/iscbulletin/search/bulletin/interactive/), or use the standard [search page](http://isc-mirror.iris.washington.edu/iscbulletin/search/bulletin/).<br>
  Here I show a rectangle region in western Canada to output ISC reviewed catalog:<br>
  ![pic](ISCSelectRegion.png?picture=ture)<br>
  
  Click Output and you can get the information you requested:<br>
  ![pic2](ISCQuery.jpg?picture=ture)<br>
  
