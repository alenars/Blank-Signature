library(ggplot2)
library(plyr)




Kokomo_sm=ldply(list.files(path="E:/Documents/GIS/Trainings/Stat_for_Soil_Survey/final_Project/nasis",pattern="csv",full.names=TRUE),function(filename) {
  dum=read.csv(filename)
  dum$filename=filename
  return(dum)
})

Kokomosm0 <- subset(Kokomo_sm, Moisture.Status == "wet")
#Kokomosm1 <- subset(Kokomo_sm, DMU.Description == "MLRA 111A Kokomo sicl, 0 to 2%" & Moisture.Status == "wet")

Kokomosm2 <- aggregate(Month ~ High & Low & RV, data = Kokomosm0)

attach(Kokomosm0)
#par(mfrow=c(3,1))
layout(matrix(c(1,1,2,3), 2,2, byrow=TRUE))
ggplot(data=Kokomosm0, aes(Month, High))+geom_point(colour='red') +ylim (175,0)
ggplot(data=Kokomosm0, aes(Month, Low))+geom_point(colour='purple') +ylim (175,0)
ggplot(data=Kokomosm0, aes(Month, RV))+geom_point(colour='green') +ylim (175,0)



#plots all 3 values overlayed
ggplot(data=Kokomosm0, (aes(Month, High))+ geom_point(colour='red')

ggplot()+geom_line(data=Kokomosm0, aes(Month, Low), colour='red')+geom_line(data=Kokomosm0, aes(Month, RV), colour='purple')+geom_point(data=Kokomosm0, aes(Month, High), colour='green') +ylim (175,0)


ggplot()+geom_point(data=Kokomosm0, aes(Month, Low), colour='red')+
  geom_point(data=Kokomosm0, aes(Month, RV), colour='purple')+
  geom_point(data=Kokomosm0, aes(Month, High), colour='green')+
  ylim (175,0)


ggplot()+geom_point(data=Kokomosm0, aes(Month, Low), colour='red')