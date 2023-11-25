setwd("D:/쿠씨톤/open")

mydata <- read.csv("train.csv",header=T)

summary(mydata)
str(mydata)

train <- mydata[,c(1:8,23)] #test 데이터에 있는 변수만 추출

#연월일시 데이터 분리
train$year <- substr(train$사고일시,1,4)
train$month <- substr(train$사고일시,6,7)
train$day <- substr(train$사고일시,9,10)
train$time <- substr(train$사고일시,12,13)

#시군구 데이터 제거
train <- train[,-5]

##EDA
plot(x=1:length(train$ECLO), y=train$ECLO)
hist(train$ECLO,xlab="ECLO",main="Histogram of ECLO")
train <- train[train$ECLO < 16,] #이상치 제거

boxplot(train$ECLO~factor(train$노면상태),col=rainbow(6),ylab = "ECLO", xlab="노면상태")


a <- length(levels(factor(train$기상상태)))

boxplot(train$ECLO~factor(train$기상상태),col=rainbow(a),ylab = "ECLO", xlab="기상상태",at=c(3,1,2,5,4,6))

plot(x=jitter(as.numeric(factor(train$기상상태))),y=jitter(as.numeric(factor(train$노면상태))))

table(factor(train$노면상태),factor(train$기상상태))
table(factor(train$노면상태))
table(factor(train$기상상태))

boxplot(train$ECLO~factor(train$사고유형),col=rainbow(3),ylab = "ECLO", xlab="사고유형")

boxplot(train$ECLO~factor(train$요일),col=rainbow(7),ylab = "ECLO", xlab="요일")

boxplot(train$ECLO~factor(train$year),col=rainbow(3),ylab = "ECLO", xlab="년도")

###################
summary(aov(ECLO~factor(요일),data=train))

model1 <- lm(ECLO~factor(요일),data=train)
summary(model1) #금토일

summary(aov(ECLO~factor(노면상태),data=train))
model3 <- lm(ECLO~factor(노면상태),data=train)
summary(model3) #건조-맑음,젖음/습기-비

summary(aov(ECLO~factor(사고유형),data=train))
model5 <- lm(ECLO~factor(사고유형),data=train)
summary(model5) #차대차,차대사람

model6 <- lm(train$ECLO~as.numeric(train$time))
summary(model6)
plot(x=jitter(as.numeric(train$time)),y=train$ECLO)#시간과 ECLO사이 관계

summary(aov(ECLO~factor(time),data=train))
model6_2<- lm(ECLO~factor(time), data=train)
summary(model6_2) #3시, 9시, 10시, 11시, 13~19시

summary(aov(ECLO~factor(year),data=train))
model7 <- lm(ECLO~factor(year),data=train) #year가 3개밖에 없으므로 multinomial 변수로 처리하는 게 낫다고 판단
summary(model7)

summary(aov(ECLO~factor(month),data=train))
model8 <- lm(ECLO~factor(month),data=train)
summary(model8)

model8_1 <- lm(ECLO~as.numeric(month),data=train)
summary(model8_1)
#월은 수치데이터로선 크게 의미가 없는 듯 함

summary(aov(ECLO~factor(day),data=train))
model9 <- lm(ECLO~factor(day),data=train)
summary(model9)
#일 자체는 크게 의미 없을 듯