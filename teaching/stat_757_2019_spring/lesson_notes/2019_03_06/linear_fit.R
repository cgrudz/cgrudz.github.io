library("faraway")

lmod <- lm(log(pass) ~ year, airpass)
plot(pass ~ year, airpass, type="l", ylab="Passengers")
lines(exp(predict(lmod)) ~ year, airpass)
