require(stabledist)
z= seq(-6, 6, length = 300)
s.norm = dstable(z, # values of the density
                 alpha = 2, # tail
                 beta = 0, # skewness
                 gamma = 1, # scale
                 delta = 0, # location
                 pm = 1) # type of parametrization

s.cauchy = dstable(z, # values of the density
                   alpha = 1, # tail
                   beta = 0, # skewness
                   gamma = 1, # scale
                   delta = 0, # location
                   pm = 0)  # type of parametrization

s.levy = dstable(z, #values of the density
                 alpha = 0.5, # tail
                 beta = 0.9999, # skewness
                 gamma = 1, # scale
                 delta = 0, # location
                 pm= 0)  # type of parametrization

plot(z, s.norm, # plot normal
     col ="red", type ='l', ylim = c(0,0.5))

lines(z, s.cauchy, # plot Cauchy
      col ="green")

lines(z, s.levy, # plot Levy
      col ="blue")
