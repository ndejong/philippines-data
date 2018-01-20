# Philippines Data Mashup

Philippine Statistics Authority (PSA) have several reasonable articles about the 
2015 census:-
 - http://psa.gov.ph/content/philippine-population-density-based-2015-census-population
 - Population growth is strong, in 2000 there were 225 people per sq/km, and by 
   2015 there were now 337 people sq/km which works out to a (linear) 2.73% 
   population growth year on year.
 - the article above links to a MS Excel spreadsheet [2015 Population Density_web.xlsx](http://psa.gov.ph/sites/default/files/attachments/hsd/pressrelease/2015%20Population%20Density_web.xlsx) 
   with population data per City/Municipality unfortunately the spreadsheet is 
   not well arranged to make easy use of the data (multiple values in single 
   cells etc), so a fair bit of manual massaging of the dataset is required to 
   get it into shape.
 - after [wrangling](https://github.com/ndejong/philippines-data/blob/master/tools/csvtojson.py) with the data we now have it available in a nice clean JSON 
   formatted structure [2015 Population Density_web_clean-columns.json](https://github.com/ndejong/philippines-data/blob/master/data/2015%20Population%20Density_web_clean-columns.json)
 - using the [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro) 
   service we are able to easily lookup the lat/long for all expressed 
   City/Municipality names in the original 2015 census data which we fold into
   the wrangled JSON formatted data using [insertgeocode.py](https://github.com/ndejong/philippines-data/blob/master/tools/insertgeocode.py)
 - the combination of the PSA 2015 Census data and the Google Maps Geocode 
   lookups is now quite useful [2015-population-density-w-google-geocode_20171218.json](https://github.com/ndejong/philippines-data/raw/master/data/2015%20Population%20Density_web_clean-columns.json)
   because we can use it to generate a nice interactive heatmap.
   
Also worth a mention is the PSA Openstat facility here:-
 - http://openstat.psa.gov.ph/
