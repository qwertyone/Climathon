#lidar data extraction

library(raster)
library(rgdal)

setwd(A:\Downloads\earthanalyticswk3)

# open raster data
lidar_dem <- raster(x="BLDR_LeeHill/pre-flood/lidar/pre_DTM.tif")

# plot raster data
plot(lidar_dem, main="Digital Elevation Model - Pre 2013 Flood")

# zoom in to one region of the raster
plot(lidar_dem,
  xlim=c(473000, 473030), # define the x limits
  ylim=c(4434000, 4434030), # define y limits for the plot
     main="Lidar Raster - Zoomed into to one small region")

# view resolution units
crs(lidar_dem)
## CRS arguments:
##  +proj=utm +zone=13 +datum=WGS84 +units=m +no_defs +ellps=WGS84
## +towgs84=0,0,0

# assign crs to an object (class) to use for reprojection and other tasks
myCRS <- crs(lidar_dem)
myCRS
## CRS arguments:
##  +proj=utm +zone=13 +datum=WGS84 +units=m +no_defs +ellps=WGS84
## +towgs84=0,0,0

# what is the x and y resolution for our raster data?
xres(lidar_dem)
## [1] 1
yres(lidar_dem)
## [1] 1

# view coordinate reference system
crs(lidar_dem)
## CRS arguments:
##  +proj=utm +zone=13 +datum=WGS84 +units=m +no_defs +ellps=WGS84
## +towgs84=0,0,0

# plot histogram
hist(lidar_dem,
     main="Distribution of surface elevation values",
     xlab="Elevation (meters)", ylab="Frequency",
     col="springgreen")

# plot histogram
hist(lidar_dem,
     breaks=10000,
     main="Distribution of surface elevation values with breaks",
     xlab="Elevation (meters)", ylab="Frequency",
     col="springgreen")

# plot histogram
hist(lidar_dem,
     main="Distribution of surface elevation values",
     breaks=c(1600, 1800, 2000, 2100),
     xlab="Elevation (meters)", ylab="Frequency",
     col="wheat3")

GDALinfo("BLDR_LeeHill/pre-flood/lidar/pre_DTM.tif")

# view attributes / metadata of raster
# open raster data
lidar_dem <- raster(x="BLDR_LeeHill/pre-flood/lidar/pre_DTM.tif")
# view crs
crs(lidar_dem)
## CRS arguments:
##  +proj=utm +zone=13 +datum=WGS84 +units=m +no_defs +ellps=WGS84
## +towgs84=0,0,0

# view extent via the slot - note that slot names can change so this may not always work.
lidar_dem@extent
## class       : Extent 
## xmin        : 472000 
## xmax        : 476000 
## ymin        : 4434000 
## ymax        : 4436000

lidar_dsm <- raster(x="BLDR_LeeHill/pre-flood/lidar/pre_DSM.tif")

extent_lidar_dsm <- extent(lidar_dsm)
extent_lidar_dem <- extent(lidar_dem)

# Do the two datasets cover the same spatial extents?
if(extent_lidar_dem == extent_lidar_dsm){
  print("Both datasets cover the same spatial extent")
}
## [1] "Both datasets cover the same spatial extent"

compareRaster(lidar_dsm, lidar_dem,
              extent=TRUE)
## [1] TRUE

compareRaster(lidar_dsm, lidar_dem,
              res=TRUE)
## [1] TRUE
nlayers(lidar_dsm)
## [1] 1

plot(lidar_dem,
     main="Lidar Digital Elevation Model (DEM)")

# plot raster data
plot(lidar_dsm,
     main="Lidar Digital Surface Model (DSM)")

# open raster data
lidar_chm <- lidar_dsm - lidar_dem

# plot raster data
plot(lidar_chm,
     main="Lidar Canopy Height Model (CHM)")

plot(lidar_chm,
     breaks = c(0, 2, 10, 20, 30),
     main="Lidar Canopy Height Model",
     col=c("white","brown","springgreen","darkgreen"))

# check to see if an output directory exists
dir.exists("data/week3/outputs")
## [1] TRUE

# if the output directory doesn't exist, create it
if (dir.exists("data/week3/outputs")) {
  print("the directory exists!")
  } else {
    # if the directory doesn't exist, create it
    # recursive tells R to create the entire directory path (data/week3/outputs)
    dir.create("data/week3/outputs", recursive=TRUE)
  }
## [1] "the directory exists!"

# export CHM object to new GeotIFF
writeRaster(lidar_chm, "data/week3/outputs/lidar_chm.tiff",
            format="GTiff",  # output format = GeoTIFF
            overwrite=TRUE) # CAUTION: if this is true, it will overwrite an existing file

# plot histogram of data
hist(lidar_chm,
     main="Distribution of raster cell values in the DTM difference data",
     xlab="Height (m)", ylab="Number of Pixels",
     col="springgreen")

# zoom in on x and y axis
hist(lidar_chm,
     xlim=c(2,25),
     ylim=c(0,4000),
     main="Histogram of canopy height model differences \nZoomed in to -2 to 2 on the x axis",
     col="springgreen")

# see how R is breaking up the data
histinfo <- hist(lidar_chm)

histinfo$counts
##  [1] 79610  5988  4513  3709  2758  1716   965   452   202    64    17
## [12]     4     2
histinfo$breaks
##  [1]  0  2  4  6  8 10 12 14 16 18 20 22 24 26

# zoom in on x and y axis
hist(lidar_chm,
     xlim=c(2,25),
     ylim=c(0,1000),
     breaks=100,
     main="Histogram of canopy height model differences \nZoomed in to -2 to 2 on the x axis",
     col="springgreen",
     xlab="Pixel value")

# create classification matrix
reclass_df <- c(0, 2, NA,
              2, 4, 1,
             4, 7, 2,
             7, Inf, 3)
reclass_df
##  [1]   0   2  NA   2   4   1   4   7   2   7 Inf   3

# reshape the object into a matrix with columns and rows
reclass_m <- matrix(reclass_df,
                ncol=3,
                byrow=TRUE)
reclass_m

# reclassify the raster using the reclass object - reclass_m
chm_classified <- reclassify(lidar_chm,
                     reclass_m)

# view reclassified data
barplot(chm_classified,
        main="Number of pixels in each class")

# assign all pixels that equal 0 to NA or no data value
chm_classified[chm_classified==0] <- NA

# plot reclassified data
plot(chm_classified,
     col=c("red", "blue", "green"))

# plot reclassified data
plot(chm_classified,
     legend=F,
     col=c("red", "blue", "green"), axes=F,
     main="Classified Canopy Height Model \n short, medium, tall trees")

legend("topright",
       legend = c("short trees", "medium trees", "tall trees"),
       fill = c("red", "blue", "green"),
       border = F,
       bty="n") # turn off legend border

# create color object with nice new colors!
chm_colors <- c("palegoldenrod", "palegreen2", "palegreen4")

# plot reclassified data
plot(chm_classified,
     legend=F,
     col=chm_colors,
     axes=F,
     main="Classified Canopy Height Model \n short, medium, tall trees")

legend("topright",
       legend = c("short trees", "medium trees", "tall trees"),
       fill = chm_colors,
       border = F,
       bty="n")

# import the vector boundary
crop_extent <- readOGR("BLDR_LeeHill",
                       "clip-extent")
## OGR data source with driver: ESRI Shapefile 
## Source: "data/week3/BLDR_LeeHill", layer: "clip-extent"
## with 1 features
## It has 1 fields
## Integer64 fields read as strings:  id

# plot imported shapefile
# notice that we use add=T to add a layer on top of an existing plot in R.
plot(crop_extent,
     main="Shapefile imported into R - crop extent",
     axes=T,
     border="blue")

# crop the lidar raster using the vector extent
lidar_chm_crop <- crop(lidar_chm, crop_extent)
plot(lidar_chm_crop, main="Cropped lidar chm")

# add shapefile on top of the existing raster
plot(crop_extent, add=T)

