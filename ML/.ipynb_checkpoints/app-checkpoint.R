#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(stringr)
library(shiny)
library(stringi)
library(lubridate)
source('query.R')
library("leaflet")
library("data.table")
library("sp")
library("rgdal")
# library("maptools")
library("KernSmooth")
library("raster")

library(DBI)

con <- dbConnect(RSQLite::SQLite(), "airbnb.db",timeout = 10)

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("A Covid Vacation"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            selectInput(
                "room_type",
                "Room type",
                c("ALL","Entire home/apt","Private room")
            ),
            dateInput("date_selection", "Start Date",value = "2021-08-01", format = "yyyy-mm-dd",min = "2015-01-01",max = "2021-09-01"),
            selectInput(
                "timerange",
                "Time Range",
                c("day","week","month")
            ),
            actionButton("refresh", "refresh"),
            
        ),

        # Show a plot of the generated distribution
        mainPanel(
            headerPanel("Airbnb Listings in Melbourne"),
            
            leafletOutput("myMap")
            
        )
    )
)

#Goal: Create a slider that changes the heatmap over melbourne. 

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    observeEvent(input$refresh,{
        #get reviews that happened in this month:
        time = strptime(input$date_selection, "%Y-%m-%d")
        if (input$timerange=="day"){
            timerange = 1
            } else if (input$timerange=="week"){
            timerange = 7
            } else if (input$timerange=="month"){
                timerange = 30
            } else {
                timerange = 365
            }
        
        #print(timerange,input$date_selection)
        dat<-get_listings(con,input$date_selection,input$date_selection+timerange,input$room_type)
        output$myMap <- renderLeaflet({
            #dat = get_listings(con,'2020-10-01','2020-12-31','Entire home/apt')
            
            ## Create kernel density output
            kde <- bkde2D(dat[ , c('longitude', 'latitude')],
                          bandwidth=c(.0045, .0068), gridsize = c(500,500))
            # Create Raster from Kernel Density output
            KernelDensityRaster <- raster(list(x=kde$x1 ,y=kde$x2 ,z = kde$fhat))
            
            #create pal function for coloring the raster
            palRaster <- colorNumeric("Spectral", domain = KernelDensityRaster@data@values)
            
            #set low density cells as NA so we can make them transparent with the colorNumeric function
            KernelDensityRaster@data@values[which(KernelDensityRaster@data@values < 1)] <- NA
            
            #create pal function for coloring the raster
            palRaster <- colorNumeric("Spectral", domain = KernelDensityRaster@data@values, na.color = "transparent")
            
            ## Redraw the map
            leaflet() %>% addTiles() %>% 
                addRasterImage(KernelDensityRaster, 
                               colors = palRaster, 
                               opacity = .8) %>%
                addLegend(pal = palRaster, 
                          values = KernelDensityRaster@data@values, 
                          bins = c(100,200,300,400,500,600),
                          title = "Airbnb Bookings in Timeframe")
            
            
            
        })
        
    })
    

    
    
}

# Run the application 
shinyApp(ui = ui, server = server)
