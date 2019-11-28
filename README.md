# Data Engineer - Take Home Test

Please fork this repository and send the link to anup.saund@gmail.com

# Overview 
This test has been designed to give candidates an opportunity to demonstrate their knowledge of ETL, SQL and Data Warehousing.

## Technology agnostic
Feel free to use any language or technology you are most comfortable with.


## Tasks
Please save SQL files to `SQL`, exports to `EXPORT` and scripts to `SCRIPTS`.

1. Design and create a SQL schema to store the `amazon-cell-phone` files.
 
2. Write a script to load the `.csv` data into the tables created in step 1.
  
3. Write a script to export the table data into the `EXPORT` folder in `.csv` format.

4. Write a script to search Amazon for an ASIN and then update the fields in the items table.

5. Download GSMARENA database from https://www.kaggle.com/arwinneil/gsmarena-phone-dataset

6. Write an ETL script to:
    1. Find a match on items.title with a GSMArena Model. 
    1. Save 4 additonal meta fields into `items` from the GSMArena data.
    1. Transform the `network_technology` field into a `;` delimited string and save this into a new field in `items`

7. Write a SQL statement which to display the following;

    ASIN, TITLE, Count of reviews from  `reviews` table.

8. Using the data from step 7, generate a Pie chart in gsheets to show the top 10 products with the highest number of reviews.

9. Write up in this readme - a strategy for creating an automation for step 6 that runs hourly, 7 days a week. (Please include technology arangement, alternatives, reasons why and pricing)

Write up
--------


