v = c(1,2,3,4,5,6,7,8,9,10,11,12)
dim(v)=c(3,4)

matrix(data=v, nrow=3, ncol=4)
matrix(v, 3, 4, byrow=TRUE) #byrow = row에 의해서 (중심으로) 

rnames = c('1', '2', '3')
cnames = c('v1', 'v2', 'v3','v4')
matrix(v, 3, 4, dimnames=list(rnames, cnames))

w = c(1, 2,3, 4,5, 6)
mtx=matrix(w, 2, 3)
mtx
mtx + 1
mtx - 1
mtx * 2
mtx / 2

mtx = matrix(c(1,2,3,4,5,6), 2, 3)
mtx
rowSums(mtx)
colSums(mtx)
rowMeans(mtx)
colMeans(mtx)

t() # transposed의 약자 
lst = list(0.58, 1.96, 0.35)
lst
lst = list(1.23, 'apple', c(2,3,4,5,7))
lst


v1 = c('1', '2', '3')
v2 = c('mouse', 'keyboard', 'usb')
v3 = c(30000, 90000, 50000)
product = data.frame(v1, v2, v3)
product
product = data.frame(id=v1, id=v2, id=v3)
product

str(product)

x = 'we have a dream'
x
nchar(x)

length(x)
y=c('we', 'have', 'a', 'dream')
y
length(y)
nchar(y)

letters
sort(letters, decreasing=TRUE)

foxsays='It is only with the HEART that can See Rightly'
foxsays
tolower #소문자로 바꿔주는 함수
toupper(foxsays)


paste('everybody', 'wants')


paste('everybody', 'wants', 'to', 'fly')
paste('everybody', 'wants', 'to', 'fly', sep='-')
paste('everybody', 'wants', 'to', 'fly', sep='')


islands
head(islands)
islandnames = names(islands)
islandnames
grep(pattern = 'New', x= islandnames)
index = grep(pattern='New', islandnames)
islandnames[index]

x= pi
x
y=3
y
if (x>y)x
if(x<y)x
if(x<y)x else y
repeat print('hello')
qi=5
repeat{if(i>25) break
  else{
    print(i) 
    i=i+5}
}

i = 5
while(i<=25) {
  print(i)
  i=i+5
}

#Data-횡단면
#cross-section : 시점(spot), yearly(그해), 그 분기, monthy(그달), weekly(그주), daily(그날)
#빈도분석으로 시작함 : 명목, 서열 

#Data-시계열 : 종적 data, 시간의 흐름에 따라, time-series(ts)
#요인(Factor) : Grouping(요인)
# 명목< 서열<등간< 비율
# R의 데이터 세트가 내장된 것을 아는 것을 쓰시오


data()
AirPassengers
head(AirPassengers) #factor data : 승객수 하나만 있는 단별량 분석 가능 factor 데이터
str(AirPassengers)
help(AirPassengers)
#승객 숫자이므로 비율임..

BJsales
head(BJsales) #factor / time series / 비율척도

BOD #DATAframe / 횡단면 / 비율척도
str(BOD)
CO2 # datafraome / 횡단면 / 요인변수 존재
str(CO2)

ChickWeight
head(ChickWeight)
str(ChickWeight)
help(ChickWeight)

EuStockMarkets
head(EuStockMarkets)
str(EuStockMarkets) #시계열, 비율척도

HairEyeColor
head(HairEyeColor)
str(HairEyeColor) # list 형식, 교차표(table)을 넣은 list 복잡하고 귀찮아서 리스트와 매트릭스는 잘 쓰지 않는다.

InsectSprays
head(InsectSprays) #dataframe / 요인변수 들어감-스프레이드 종류
str(InsectSprays)

JohnsonJohnson
head(JohnsonJohnson)
str(JohnsonJohnson) #factor / 시계열/ 비율척도

LakeHuron
head(LakeHuron)
str(LakeHuron) 
help("LakeHuron")

LifeCycleSavings
head(LifeCycleSavings)
str(LifeCycleSavings) #dataframe / 횡단면 / 비율

Nile #time, vector data
str(Nile)
help(Nile)
head(Nile)

Orange # dataframe
head(Orange)
str(Orange)

PlantGrowth
head(PlantGrowth)
str(PlantGrowth)

Seatbelts
head(Seatbelts)
str(Seatbelts)

Titanic #table이 여러개 있는 list
str(Titanic)


ToothGrowth #num은 비율척도라고 하면 됨
head(ToothGrowth)
str(ToothGrowth)


UCBAdmissions
str(UCBAdmissions)

UKDriverDeaths
head(UKDriverDeaths)
str(UKDriverDeaths)
help(UKDriverDeaths)

USAccDeaths
USArrests
head(USArrests)
str(USArrests)

USPersonalExpenditure
str(USPersonalExpenditure)
help(USPersonalExpenditure)


airquality #전형적인 dataframe 성격
head(airquality)
str(airquality)

cars
head(cars)

euro # euro is a named vector of length 11, euro.cross a matrix of size 11 by 11, with dimnames. matrix로 구분짓는게 맞는것 같음 
str(euro)
help(euro)
#table이 되려면 최소한 차원이 2개씩은 되어야함 

faithful
head(faithful)

iris
head(iris)

islands #matrix로 예상 ex) euro랑 비슷
head(islands)
str(islands)
lynx

mtcars # 많이 씀
head(mtcars)
str(mtcars)

quakes
head(quakes)
str(quakes)

rivers #생긴건 벡터처럼  생겼지만 s가 붙었으므로 matrix에 가깝다
head(rivers)
str(rivers)
help(rivers)

trees #data.frame
head(trees)
str(trees)

volcano #matrix
head(volcano)
str(volcano)
help(volcano)

women #dataframe 시계열 요소가 없는 횡단면
head(women)
str(women)



Orange

sum_code = function(인자1, 인자2) {
  a = 인자1 + 인자2
  return(a)
}
help(Orange)
euro
Nile
women



head(Orange$age)
min(Orange$age)
max(Orange$age)
mean(Orange$age)
median(Orange$age)
var(Orange$age)
sd(Orange$age)
range(Orange$age)

summary(Orange$age)
var(Orange$age)
sd(Orange$age)
range(Orange$age)

head(Orange$circumference)
min(Orange$circumference)
max(Orange$circumference)
mean(Orange$circumference)
median(Orange$circumference)
var(Orange$circumference)
sd(Orange$circumference)
range(Orange$circumference)
summary(Orange$circumference)


#탐색적 요인분석 #5월 8일(월)
library(readxl)
library(lavaan)
library(psych)

getwd()
setwd("/Users/leedonghoo/Desktop/R")

factor <- read_excel('retire.xlsx')
attach(factor)
head(factor)
factor <- subset(factor,select = c("satis_1","satis_2","satis_3",'expect_1','expect_2','expect_3','edu_1','edu_2','edu_3'))
factor
fa.out <- factanal(factor,factors = 3, rotation = 'varimax')
#factanal: R에서 요인 분석을 수행하는 함수입니다.
#factors = 3: 분석에서 추출할 요인 수를 3개로 지정
#rotation = 'varimax': 요인 회전 방법으로 varimax 방법은 요인들 간의 독립성을 높이기 위해 사용
fa.out
print(fa.out, cutoff = 0.2, sort=T)
#cutoff = 0.2: 요인 적재값의 절대값이 0.2 이상인 것만 출력하도록 설정 
#적재값이 작은 경우 해당 요인과 관련이 적다고 판단하고 결과에서 제외가능

KMO(factor)# MSA가 0.5이상이면 이 데이터가 탐색적요인분석에 적합한 데이터다라고 판단.
cortest.bartlett(factor) # p-v 값이 유의하다는 것은 탐색적 요인분석이 잘 수행됐다라는 뜻.


# 변수 6개이상인 r 내장 데이터
install.packages('openxlsx')
install.packages("readxl")
install.packages("lavaan")
install.packages("psych")
library('openxlsx')
mt <- mtcars[1:7]
mtcars
write.xlsx(mtcars, "mt.xlsx")



library(readxl)
library(lavaan)
library(psych)

mt <- read_excel('mt.xlsx')
attach(mt)
head(mt)
mt <- subset(mt,select = c('mpg','cyl','disp','hp','drat','wt','qsec'))
mt.out <- factanal(mt,factors = 3, rotation = 'varimax')
mt.out
print(mt.out, cutoff = 0.2, sort=T) #요인 적재값의 절대값이 0.2 이상인 것만 출력하도록 설정
KMO(mt) #MSA가 0.83으로 탐색적  요인분석에 적합한 데이터다라고 판단 가능
cortest.bartlett(mt) # p-v 값이 유의하다는 것은 탐색적 요인분석이 잘 수행됐다라는 뜻.


str(faithful)
#기본적인 함수
plot(faithful)
#eruption 알아두기
#points를 통해서 색깔 표현이 가능함
eruption.long=with(faithful, faithful[eruptions>3,])
#lm으로 waiting이 eruptions에 영향을 미친다고 가정했다고 친다.
faithful.lm=lm(waiting~eruptions, data=faithful)
plot(faithful)
points (eruption.long, col="red", pch=19)
lines(x=faithful$eruptions, y=fitted(faithful.lm), col="blue")
abline(v=3, col="purple") #drawing a vertical line
abline(h=mean(faithful$waiting), col="green")

str(ToothGrowth)
head(ToothGrowth)
ToothGrowth
plot(ToothGrowth$supp, ToothGrowth$len)

#회귀선 데이터프레임 연속변수가 있는 두개로 고르면 된다.
#1
#기본적인 함수
head(iris)
plot(iris)
#eruption 알아두기
#point를 통해서 색깔 표현이 가능함
eruption.long=with(iris, iris[Sepal.Width>3,])
#lm으로 waiting이 eruptions에 영향을 미친다고 가정했다고 친다.
Sepal.lm=lm(Sepal.Length~Sepal.Width, data=iris)
plot(iris$Sepal.Length, iris$Sepal.Width)
points (eruption.long, col="red", pch=19)
lines(x=iris$Sepal.Length, y=fitted(Sepal.lm), col="blue")
abline(v=, col="purple") #drawing a vertical line
abline(h=mean(faithful$waiting), col="green")
mt <- mtcars[c('mpg','hp')]
mt.lm=lm(hp~mpg, data=mt)
plot(mt)
mt.long=with(mt, mt[hp>115,])
points(mt.long,col='red',pch=19)
lines(x=mt$mpg, y=fitted(mt.lm), col="blue")
abline(v=20.5,col='purple')
abline(v=mean(mt$hp), col='green')
#2
iris
str(trees)
head(airquality)
airquality
plot(iris$Species,iris$Sepal.Length)
mtcars


mt <- mtcars[c('mpg','hp')]
mt.lm=lm(hp~mpg, data=mt)
plot(mt)
mt.long=with(mt, mt[hp>115,])
points(mt.long,col='red',pch=19)
lines(x=mt$mpg, y=fitted(mt.lm), col="blue")
abline(v=20.5,col='purple')
abline(h=mean(mt$hp), col='green')


#1. 시계열 time series
#2. 잔차도표 통계 분석은 오차항으로 인하여 많이 생기게 되는 것 
# 많은 것들이 1. 오차항 2. 척도 3. ... 등으로 인하여 만들어짐

#회귀분석 중요한 가정
# 1. 정규분포 2. 독립변수간 상관관계(낮은지) 3. 잔차간(오차항)간 상관관계 (낮은지)
#5/22실습내용 시계열은 추세가 있는지 보아야함 추세가 있으면 비정상 시계열 
#시계열
str(sunspot.year)
head(sunspot.year)
plot(sunspot.year)
plot(log(sunspot.year))

#횡단면
str(faithful)
faithful.lm=lm(waiting~eruptions, data=faithful)
class(faithful.lm)
plot(faithful.lm)
plot(faithful.lm)
summary(faithful.lm)
install.packages("lmtest")
library(lmtest)
dwtest(faithful.lm)

str(mt)
mt.lm=lm(mpg~hp, data=mt)
class(mt.lm)
plot(mt.lm)
summary(mt.lm)
install.packages("lmtest")
library(lmtest)
dwtest(mt.lm)



#50분간 볼 예정 함수명 / 인수

#grid() 함수는 격자를 의미함
#points() 점(들)에 대한 함수
# pch 인수 = point character
# 히스토그램은 빈도분석시에 많이 사용된다./ 정규분포인지를 확인할 때 자주 그린다. 척도 scale이 무엇인지 알아야 그래프와 분석 방법으 선택 할 수 있다.
# 명목 < 서열 < 등간 < 비율 순으로 데이터가 많다. 
# [  범주형  ]  [  연속형  ]
# 범주형이 빈도분석으로 자주 쓰임
# 연속형을 히스토그램을 그랠 때는 정규 분포인지를 확인 할 때이다.
# 첨도 : 뾰족 +- 10
# 왜도 : 왼쪽 / 오른쪽
# 제일 많이 그릴 그림은 히스토그램 / 시간에 따라 양이 변하는 시계열 그래프
plot(CO2$uptake,type='n')
grid()
points(CO2$uptake, pch=10, col='green')


str(LifeCycleSavings)
head(LifeCycleSavings)
dotchart(LifeCycleSavings$dpi, labels=row.names(LifeCycleSavings), cex=0.7,
         xlab="dpi", main="LifeCycleSavings")

str(ToothGrowth)
head(ToothGrowth)
hist(ToothGrowth$len, main="histogram ToothGrowth")

str(WorldPhones)
head(WorldPhones)
# cex란 무엇인가 chraacter expend 점크기 바꾸기 pch는 점 모양



#시험 시간은 50분이다.
# scatterplot3d

library(scatterplot3d)
attach(mtcars)
str(mtcars)
scatterplot3d(wt, disp, mpg, main="3D scatterplot")

#bar chart
head(Titanic)
str(Titanic)
Titanic
class=margin.table(Titanic, 1) # 1means class
class
Titanic
barplot(class, main="simple bar chart")

plot(LakeHuron)
plot(LakeHuron, lty="solid")
plot(LakeHuron, lty="dashed")
plot(LakeHuron, lty="dotted")
plot(LakeHuron, lty="dotdash")
plot(LakeHuron, lty="longdash")
plot(LakeHuron, lty="twodash")



