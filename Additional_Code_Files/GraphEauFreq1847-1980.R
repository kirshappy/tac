#Bar plot code
#General Settings

library("ggplot2")
library("scales")

setwd("/Users/myriam/Desktop/data")
eauData<-read.csv("wordeauFreqall.csv",header=TRUE,sep=",")
summary(eauData) #statistics information about data

pdf(file="EauBulletinsComm1847-1980.pdf")
geauData<-ggplot(eauData,aes(x=an,y=freq,fill=mot))+geom_col(position="dodge")
geauData<-geauData+scale_x_continuous("Année",breaks=seq(1870,1920,2))+scale_y_continuous("Fréquence",breaks=seq(0,150,5))+theme_bw()+theme(legend.title=element_blank(),legend.position="bottom",axis.line=element_line(colour="black"),strip.background=element_rect(fill="white"))
geauData<-geauData+ggtitle("Apparition des mots eau et eaux dans les Bulletins du conseil communal tenu entre 1847 et 1978")
geauData
dev.off()