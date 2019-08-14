library("faraway")

lagdf <- embed(log(airpass$pass),14)
colnames(lagdf) <- c("y",paste0("lag",1:13))
lagdf <- data.frame(lagdf)
armod <- lm(y ~ lag1 + lag12 + lag13, data.frame(lagdf))
plot(pass ~ year, airpass, type="l", ylab="Passengers")
lines(airpass$year[14:144], exp(predict(armod)), lty=2)
