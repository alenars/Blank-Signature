Kokomo71$year <- as.Date(cut(Kokomo71$date,
                              breaks = "year"))
Kokomo71$month <- as.Date(cut(Kokomo71$date,
                              breaks = "month"))
Kokomo71$week <- as.Date(cut(Kokomo71$date,
                             breaks = "week",
                             start.on.monday = FALSE)) # changes weekly break point to Sunday


Kokomo71$inches <-(Kokomo71$feet*12) #feet x inches
Kokomo71$convin <- (Kokomo71$inches-21) #inches - 21
Kokomo71$cm <- (Kokomo71$convin*2.54) #converted inches x centimeters

cmavmonths <- aggregate(cm ~ month+year, data = Kokomo71, mean) #averages of months & years
cmminmonth <- aggregate(cm ~ month+year, data = Kokomo71, "min") #min of months & years
cmmaxmonth <- aggregate(cm ~ month+year, data = Kokomo71, "max") #max of months & years

cmavweek <- aggregate(cm ~ week+year, data = Kokomo71, mean) #averages of weeks & years

cmavday <- aggregate(cm ~ Jday+year, data = Kokomo71, mean) #averages of day & years
cmavdayweyr <- aggregate(cm ~ Jday+week+year, data = Kokomo71, mean) #averages of day, week, & years
cmav <-aggregate(cm ~ time+Jday+week+month+year, data = Kokomo71, mean) #averages of time, day, week, & years

cmavdaywemoyr <- aggregate(cm ~ Jday+week+month+year, data = Kokomo71, mean) #averages of day, week, month & years

#plot averages of months and years
ggplot(data = cmavmonths, aes(year, cm)) +geom_line(colour="purple")+ ylim(250, -75)
ggplot(data = cmavmonths, aes(year, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavmonths, aes(year, cm)) +geom_count(colour="purple")+ ylim(250, -75)
ggplot(data = cmavmonths, aes(year, cm)) +geom_point(colour="purple")+ ylim(250, -75)
ggplot(data = cmavmonths, aes(year, cm)) +geom_point(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavmonths, aes(year, cm)) +geom_smooth(colour="purple")+ ylim(250, -75)

#plot min of months and years
ggplot(data = cmminmonth, aes(year, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)

#plot max of months and years
ggplot(data = cmmaxmonth, aes(year, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)

#plot average, min, & max of months & years. not completely working
ggplot(data = cmmaxmonth, aes(year, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+geom_line(data = cmminmonth, aes(year, cm)) +geom_line(colour="blue")+geom_smooth(colour="red")+geom_line(data = cmavmonths, aes(year, cm)) +geom_line(colour="pink")+geom_smooth(colour="yellow")+ ylim(250, -75)

#plot averages of weeks & years
ggplot(data = cmavweek, aes(week, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)

#plot averages of days & year ~ 
ggplot(data = cmavday, aes(Jday, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)

#plot averages of Jday, week, & years
ggplot(data = cmavdayweyr, aes(Jday, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdayweyr, aes(week, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdayweyr, aes(year, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)

#plot averages of Jday, week, month, & years as points
ggplot(data = cmavdaywemoyr, aes(year, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdaywemoyr, aes(month, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdaywemoyr, aes(week, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdaywemoyr, aes(Jday, cm)) +geom_jitter(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)

#plot count
ggplot(data = cmavdaywemoyr, aes(week, cm)) +geom_count(colour="purple")
ggplot(data = cmavdaywemoyr, aes(Jday, cm)) +geom_count(colour="purple")
ggplot(data = cmavdaywemoyr, aes(year, cm)) +geom_count(colour="purple")
ggplot(data = cmavdaywemoyr, aes(month, cm)) +geom_count(colour="purple")+ ylim(250, -100)

#plot averages of time, Jday, week, month, & years
ggplot(data = cmav, aes(year, cm)) +geom_count(colour="purple")+ ylim(300, -150)
ggplot(data = cmav, aes(Jday, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(300, -150)
ggplot(data = cmav, aes(month, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(300, -150)
ggplot(data = cmav, aes(year, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(300, -150)
ggplot(data = cmav, aes(week, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(300, -150)
ggplot(data = cmav, aes(time, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(300, -150)



ggplot(data = cmav, aes(Jday)) +geom_density(aes(cm))
ggplot(data = cmav, aes(cm)) +geom_density(aes(year))
ggplot(data = cmav, aes(cm)) +geom_density(aes(month))
ggplot(data = cmav, aes(cm)) +geom_density(aes(Jday))
ggplot(data = cmav, aes(cm)) +geom_density(aes(time))


a <- ggplot(data = cmavdaywemoyr, aes(year, cm)) +geom_jitter(aes (colour=year))+ ylim(300, -150)
a + geom_quantile(colour = "red",size = 2, alpha = 0.5, method="rqss", lambda=0.1)

ggplot(data=cmav, aes(year, cm))+stat_summary(geom="bar", aes(fill=year))
ggplot(data=cmav, aes(cm, month))+stat_summary(geom="bar", aes(fill=month))

#plot 3d
attach(cmav)
plot3d(year, week, cm, col="purple", size=3)+ylim(300, -150)
plot3d(week, year, cm, col="purple", size=3)+ylim(300, -150)
plot3d(year, month, cm, col="purple", size=3)+ylim(300, -150)

scatterplot3d(year, week, cm, main="3D", pch=16, highlight.3d=TRUE,type="h")
scatterplot3d(year, month, cm, main="3D", pch=16, highlight.3d=TRUE,type="h")

#plot hexbin
bincmy<-hexbin(cm,year)
plot(bincmy, main="Year")
binycm<-hexbin(year,cm)
plot(binycm, main="Year")
binmocm<-hexbin(month,cm)
plot(binmocm, main="Month")
binjdcm<-hexbin(Jday,cm)
plot(binjdcm, main="J Day")

#plot scatterplot matrices
scatterplotMatrix(~cm+Jday+week+month+year|cm, data=cmav, main="CMAV")

#plot dotplot
ggplot(data=cmav, aes(x=cm, fill=factor(year)))+geom_dotplot()
ggplot(data=cmav, aes(x=cm, fill=factor(month)))+geom_dotplot(stackdir = "center")
ggplot(data=cmav, aes(x=cm, fill=factor(week)))+geom_dotplot(stackdir = "center")

#plot raster & tile
ggplot(data = cmav, aes(year, cm))+geom_raster(aes(fill=year))
ggplot(data = cmav, aes(Jday, cm))+geom_raster(aes(fill=year))
ggplot(data = cmav, aes(Jday, cm))+geom_raster(aes(fill=Jday))
ggplot(data = cmav, aes(month, cm))+geom_tile( colour="purple1")+ ylim(300, -150)


#ggplot(data = cmavdaywemoyr, aes(year, cm)) +geom_tile(aes(fill=factor(month)))

#plot averages of Jday, week, month, & years as lines
ggplot(data = cmavdaywemoyr, aes(Jday, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdaywemoyr, aes(year, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdaywemoyr, aes(month, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)
ggplot(data = cmavdaywemoyr, aes(week, cm)) +geom_line(colour="purple")+geom_smooth(colour="green")+ ylim(250, -75)

# graph by year:
ggplot(data = Kokomo71,
       aes(year, cm)) + 
  stat_summary(fun.y = "mean", # averages all observations for the year
               geom = "line") + # or "line"
  #scale_x_date(date_labels = "%Y", date_breaks = "1 year")+
  ylim(150, -5)

ggplot(data = Kokomo71,
       aes(year, cm)) +
  stat_summary(fun.y = "mean", # averages all observations for the year
               geom = "bar") + # or "line"
  #scale_x_date(date_labels = "%Y", date_breaks = "1 year")
  ylim(150, -5)

# graph by month:
ggplot(data = Kokomo71,
       aes(month, cm)) + 
  stat_summary(fun.y = "mean", # averages all observations for the month
               geom = "line") + # or "line"
  #scale_x_date(date_labels = "%m/%Y", date_breaks = "3 months")
  ylim(150, -5)

ggplot(data = Kokomo71,
       aes(month, cm)) + 
  stat_summary(fun.y = "mean", # averages all observations for the month
               geom = "bar") + # or "line"
  #scale_x_date(date_labels = "%m/%Y", date_breaks = "1 month") +
  ylim(150, -5) 

# graph by week:
ggplot(data = Kokomo71,
       aes(week, cm)) +
  stat_summary(fun.y = "mean", # averages all observations for the week
               geom = "line") + ylim(150, -5) # or "line"
  #scale_x_date(date_labels = "%d/%m/%Y", date_breaks = "1 week") +
  ylim(150, 0)

# graph by year:
ggplot(data = Kokomo71,
       aes(year, cm)) +
  stat_summary(fun.y = "mean", # averages all observations for the year in centimeters
               geom = "line") + # or "line"
  #  scale_x_date(date_labels = "%Y", date_breaks = "1 year") +
  ylim(150, 0)


ggplot(data = Kokomo71,
       aes(year, cm)) +
  stat_summary(fun.y = "mean", # averages all observations for the year in inches
               geom = "line") + # or "line"
  #scale_x_date(date_labels = "%Y", date_breaks = "1 year")
  ylim(100, 0) 
  
#plot(as.Date(Kokomo71$date,'%d/%m/%Y'),Kokomo71$feet, xlab="Date", ylab= "Feet",type="l", lwd=2, col='purple', main="Kokomo 71")
#grid(col="darkgrey")

Kokomo71$date<-as.POSIXlt(Kokomo71$date,format="%m/%d/%y %H:%M:%S")
Kokomo71 <- within(Kokomo71, {
                      day =   as.character(format(Kokomo71$date, "%m/%d/%y"))
                      Jday =  as.integer(format(Kokomo71$date, "%j"))
                      year =  as.integer(format(Kokomo71$date, "%Y"))
                      month = as.integer(format(Kokomo71$date, "%m"))
                      week =  as.integer(format(Kokomo71$date, "%W"))
                      })

test <- aggregate(cm ~ month, data = Kokomo71, mean)
ggplot(data=test, aes(month, cm))+geom_line(colour='purple')+ylim(100, -60)

Kokomo71_2006 <- subset(Kokomo71, year %in% 2006:2006 & month %in% c(6, 7, 8))
Kokomo71_2007 <- subset(Kokomo71, year %in% 2007:2008 & month %in% c(6, 7, 8))
Kokomo71_2008 <- subset(Kokomo71, year %in% 2008:2009 & month %in% c(6, 7, 8))
Kokomo71_2009 <- subset(Kokomo71, year %in% 2009:2010 & month %in% c(6, 7, 8))
Kokomo71_2010 <- subset(Kokomo71, year %in% 2010:2011 & month %in% c(6, 7, 8))
Kokomo71_2011 <- subset(Kokomo71, year %in% 2011:2012 & month %in% c(6, 7, 8))
Kokomo71_2012 <- subset(Kokomo71, year %in% 2012:2013 & month %in% c(6, 7, 8))
Kokomo71_2013 <- subset(Kokomo71, year %in% 2013:2014 & month %in% c(6, 7, 8))
Kokomo71_2014 <- subset(Kokomo71, year %in% 2014:2015 & month %in% c(6, 7, 8))
Kokomo71_2015 <- subset(Kokomo71, year %in% 2015:2016 & month %in% c(6, 7, 8))
Kokomo71_2016 <- subset(Kokomo71, year %in% 2016:2016 & month %in% c(6, 7, 8))

#plot line
ggplot()+geom_line(data=Kokomo71_2006, aes (date, cm))+geom_line(data=Kokomo71_2007, aes (date, cm))+geom_line(data=Kokomo71_2008, aes (date, cm))+geom_line(data=Kokomo71_2010, aes (date, cm))+geom_line(data=Kokomo71_2011, aes (date, cm))+geom_line(data=Kokomo71_2012, aes (date, cm))+geom_line(data=Kokomo71_2013, aes (date, cm))+geom_line(data=Kokomo71_2014, aes (date, cm))+geom_line(data=Kokomo71_2015, aes (date, cm))+geom_line(data=Kokomo71_2016, aes (date, cm))+ ylim(100, -150)
#ggplot(data=Kokomo71_2006, aes (date, cm)) +geom_line() + ylim(100, -5)
#ggplot(data=Kokomo71_2007, aes (date, cm)) +geom_line() + ylim(100, -5)

Kokomo71_2016month <- subset(Kokomo71, year==2016 & month %in% c(2,3))
ggplot(data = Kokomo71_2016month, aes(day, cm))+geom_line() +ylim(100, -5) #messy plot for day, week, month

Kokomo71_month6 <- subset(Kokomo71, month=="6")
ggplot(data = Kokomo71_month6, aes(day, cm))+geom_line() +ylim(100, -5)

ggplot(data = Kokomo71_month6, aes(day, cm)) +geom_smooth(colour="purple")+ ylim(250, -75)



#plot data
xyplot(cm ~ year | week, data=Kokomo71_month6, main='Water Table', type=c('l', 'g'), as.table=TRUE, layout=c(2,6), xlab='week', ylab='cm')

#plot data gaps
levelplot(factor(!is.na(cm)) ~ month * factor(year) | year, main='Water Table',
          data=Kokomo71, layout=c(2,6), col.regions=c('grey', 'purple'), cuts=2, 
          colorkey=FALSE, as.table=TRUE, scales=list(alternating=3, cex=1), 
          par.strip.text=list(cex=0.85), strip=strip.custom(bg='yellow'), 
          xlab='month', ylab='year')

#doesn't work yet
cm1 <- unique(Kokomo71$year$cm)
Kokomo71da <- seq.Date(as.Date(min(Kokomo71$year$cm)), as.Date(max(Kokomo71$year$cm)), by='3 months')
xyplot(cm ~ year | factor(year), data=Kokomo71da, as.table=TRUE, type=c('l','g'), strip=strip.custom(bg=grey(0.80)), layout=c(1,length(cm1)), scales=list(alternating=3, x=list(at=Kokomo71da, format="%Y")), ylab='cm', main='Water Table')









