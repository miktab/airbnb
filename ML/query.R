library(DBI)

setwd("/media/user/0690-AF4D/airbnb/ML/Visualiser/")
con <- dbConnect(RSQLite::SQLite(), "airbnb.db",timeout = 10)

get_listings<-function(con,start,end,room_type){
  if (room_type=="ALL"){
    queries<-dbSendQuery(con,
                         "select latitude,longitude,room_type from Reviews left join Listings on Reviews.listing_id = Listings.id where Reviews.date>=$start and Reviews.date<= $end and Listings.room_type =$roomB or Listings.room_type=$roomA;"
    )
    params = list(start= as.character(start),end = as.character(end),roomA = "Entire home/apt",roomB = "Private room" )
    dbBind(queries, params)
  } else{
    queries<-dbSendQuery(con,
                         "select latitude,longitude,room_type from Reviews left join Listings on Reviews.listing_id = Listings.id where Reviews.date>=$start and Reviews.date<= $end and Listings.room_type =$room_type;"
    )
    params = list(start= as.character(start),end = as.character(end),room_type =room_type )
    dbBind(queries, params)
  }
  print(params)
  response<- dbFetch(queries)
  dbClearResult(queries)
  return(response)
}



#date = '2015-01-01'
#get_listings(con,'2015-01-01','2015-05-01','Entire home/apt')
