<style>
.section .reveal .state-background {
   background: #ffffff;
}
.section .reveal h1,
.section .reveal h2,
.section .reveal p {
   color: black;
   margin-top: 50px;
   text-align: center;
}


</style>

Methods for scalable data assimilation
========================================================
autosize: true
incremental: true
width: 1920
height: 1080




<div style="text-align:center">
<h3>Colin Grudzien<sup>1,2</sup>, Marc Bocquet<sup>3</sup>, Sukhreen Sandhu<sup>2</sup> et al.</h3>
<div style="float:left; width:100%; text-align:center; padding-top:20px;">
<div style="float:left; width:30%; text-align:center;  padding-top:40px">
<img style="width:100%", src="UNR_logo_H.png" alt="University of Nevada, Reno."/>
</div>
<div style="float:left; width:40%; text-align:center; padding-top:20px">
<img style="width:100%", src="CW3E-Logo.png" alt="Center for Western Weather and Water Extremes."/>
</div>
<div style="float:left; width:30%; text-align:center;  padding-top:40px">
<img style="width:100%", src="cerea_logo.png" alt="CEREA."/>
</div>
</div>
<div style="float:left; width:100%; padding-top:40px;">
<ol style="font-size:30px;text-align: center;list-style-position: inside;">
  <li>Center for Western Weather and Water Extremes (CW3E), Scripps Institution of Oceanography, University of California San Diego, San Diego, CA, USA</li>
  <li>Department of Mathematics and Statistics, University of Nevada, Reno, Reno, NV, USA</li>
  <li>CEREA, A joint laboratory of &Eacute;cole des Ponts Paris Tech and EDF R&D, Universit&eacute; Paris-Est, Champs-sur-Marne, France.</li>
</ol>
</div>
</div>


========================================================
## Research themes

* Data assimilation (DA) refers to methodology for combining:
  
  * <b  style="color:#1b9e77">data from physics-based, numerical models</b>; and 
  * <b style="color:#7570b3">real-world observations</b>

* to produce an <b style="color:#d95f02">improved estimate for the state</b> of a time-evolving, random process and the parameters that govern its evolution. 

* My <b>research experience</b> is in developing <strong>scalable data assimilation methodology</strong>.
  
* I utilize <b>statistical, mathematical and numerical tools</b> for understanding:

  <ul>
    <li>the <strong>stability and convergence</strong> of these estimators;</li>
    <li>the <strong>robustness and reliability</strong> of their inferences in the presence of modeling errors and bias;</li>
    <li>and the <strong>numerical efficiency</strong> of these schemes</li>
  </ul>

* for problems inspired by <b  style="color:#1b9e77">high-dimensional, chaotic dynamical systems</b> characteristic of weather and climate.

========================================================
## Motivation

<div style="float:left; width:100%">
<ul>
  <li>A <b>Bayesian approach to DA</b> is widely adopted because it provides a <strong>unified treatment of the tools from statistical estimation, nonlinear optimization and machine learning</strong>.</li>
  <li>Suppose that the <b style="color:#1b9e77">dynamical physical states</b> can be written in a vector, $\pmb{x}_k \in \mathbb{R}^{N_x}$, where $k$ corresponds to some time $t_k$.</li>
  <li>Abstractly, the <strong>time-evolution</strong> of these states is represented by the <b style="color:#1b9e77">nonlinear map $\mathcal{M}$</b>,
  $$\begin{align}\\
  \pmb{x}_k = \mathcal{M}_{k} \left(\pmb{x}_{k-1}, \boldsymbol{\lambda}\right) + \boldsymbol{\eta}_k
  \end{align}$$
  where</li>
  <ul>
    <li>$\pmb{x}_{k-1}$ is the <b>vector of physical states</b> at an <strong>earlier time</strong> $t_{k-1}$;</li>
    <li>$\boldsymbol{\lambda}$ is a vector of <b>uncertain physical parameters</b> on which the <strong>time evolution depends</strong>;</li>
    <li>$\boldsymbol{\eta}_k$ is an <b>additive, stochastic noise</b> term, representing <strong>errors in our model for the physical process</strong>.</li>
  </ul>
  <li>We wish to <b style="color:#d95f02">estimate the random vector</b> ${\color{#d95f02} {\pmb{x}_k } }$ with a prior distribution on $\left(\pmb{x}_{k-1}, \boldsymbol{\lambda}\right)$ and knowledge of $\mathcal{M}_{k}$ and knowledge of how $\boldsymbol{\eta}_k$ is distributed.</li>
    <li>For the rest of this discussion, we <b>restrict to the case</b> that $\boldsymbol{\lambda}$ is a known constant, and the forecast model is perfect,
  $$\begin{align}
  \pmb{x}_k = \mathcal{M}_{k} \left(\pmb{x}_{k-1}\right),
  \end{align}$$
  <strong>for simplicity</strong>.</li>
  <li>However, a strength of the <b>Bayesian approach</b> is that it is <strong>easily extended to handle the more general case</strong>.</li>
</ul>
</div>

========================================================
## Motivation

  
<ul>
  <li>At time $t_{k-1}$, we make a <b style="color:#1b9e77">forecast for the distribution of $\pmb{x}_k$</b> with our prior knowledge, including the physics-based model.</li>  
  <li>After some time, we are given <b style="color:color:#7570b3">real-world observations</b> ${\color{#7570b3} {\pmb{y}_k\in\mathbb{R}^{N_y}} }$ related to the physical states by,
  $${\color{#7570b3} { \pmb{y}_k = \mathcal{H}_k \left(\pmb{x}_k\right) + \boldsymbol{\epsilon}_k } }$$
  where</li>
  <ul>
    <li>${\color{#7570b3} {\mathcal{H}_k:\mathbb{R}^{N_x} \rightarrow \mathbb{R}^{N_y} } }$ is a nonlinear map relating the <b style="color:#d95f02">states we wish to estimate $\pmb{x}_k$</b> to the <b style="color:#7570b3">values that are observed</b> ${\color{#7570b3} { \pmb{y}_k} }$.</li>
    <ul>
      <li>Typically $N_y \ll N_x$ so this is information is sparse and observations are not $1:1$ with the unobserved states.</li>
    </ul>
    <li>$\boldsymbol{\epsilon}_k$ is an <b>additive, stochastic noise</b> term representing <strong>errors in the measurements</strong>.</li>
  </ul>
  <li>At time $t_k$ we have a <b style="color:#1b9e77">forecast distribution</b> for the states $\pmb{x}_k$  <strong>generated by our prior on $\pmb{x}_{k-1}$ and our state model $\mathcal{M}$</strong>.</li>
  <li>We also have an <b style="color:#7570b3">observation $\pmb{y}_k$</b> with uncertainty.</li>
  <li>The basic goal of Bayesian DA to find a <b style="color:#d95f02">posterior distribution for $\pmb{x}_k$</b> <b style="color:#7570b3">conditioned on $\pmb{y}_k$</b>, or some statistic of this distribution.</li>
  <li>For <b>operational forecasting</b>, this furthermore should be performed <strong>sequentially and recursively in time</strong>.</li>
</ul> 

========================================================
## <span style="color:#7570b3">Observation</span>-<span style="color:#d95f02">analysis</span>-<span style="color:#1b9e77">forecast</span> cycle

 <div style="float:left; width:50%" class="fragment">
<img style="width:100%", src="forecast_cycle_diagram_009.svg" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:left; width:50%">
<ul>
  <li><strong>Recursive estimation</strong> of the distribution for $\pmb{x}_k$ conditional  on $\pmb{y}_k$ can be described as an:</li>
  <ol>
    <li><span style="color:#7570b3;font-weight:bold">observation</span></li>
    <li><span style="color:#d95f02;font-weight:bold">analysis</span></li>
    <li><span style="color:#1b9e77;font-weight:bold">forecast</span></li>
  </ol>
  <li><b>cycle</b>.</li>
  <li>Assume an initial <span style="color:#1b9e77;font-weight:bold">forecast-prior</span> for the <span style="color:#1b9e77;font-weight:bold">physics-based numerical model state</span>.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>Using the <span style="color:#1b9e77;font-weight:bold">forecast-prior</span> and the <span style="color:#7570b3;font-weight:bold">likelihood of the observation</span>,</li>
  <ul>
    <li>we estimate the <b>Bayesian update</b> of the <span style="color:#1b9e77;font-weight:bold">prior</span> to the <span style="color:#d95f02;font-weight:bold">posterior</span></li>
    <li>conditioned on the <span style="color:#7570b3;font-weight:bold">observation</span>.</li>
  </ul>
</ul>
</div>

========================================================
### <span style="color:#d95f02">Smoothing</span>

 <div style="float:left; width:50%" class="fragment">
<img style="width:100%", src="smoothing_diagram.svg" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:right; width:45%">
<ul>
  <li>Recursive estimates of the <b>current state</b> can be performed in this fashion, but a related question regards the <strong>past states</strong>.</li>
  <li><b>New observations from the future</b> gives information about the model states at <strong>past times</strong>.</li>
  <li>This produces a <span style="color:#d95f02;font-weight:bold">retrospective posterior estimate</span> for the past states.</li>
    <li><strong>Recursive estimation of the present state</strong> is known as <b>filtering</b>.</li>
  <li><strong>Conditional estimation of a past state given future observations</strong> is known as <b>smoothing</b>.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>Note that the <b>filtering density for the current time</b> is actually just a <strong>marginal of this joint posterior over all states in the DAW</strong>
  $$\begin{align}
  p(\pmb{x}_3 \vert \pmb{y}_3, \pmb{y}_2, \pmb{y}_1) = \int \int p(\pmb{x}_3, \pmb{x}_2, \pmb{x}_1 \vert \pmb{y}_3, \pmb{y}_2, \pmb{y}_1)\mathrm{d}\pmb{x}_2 \mathrm{d}\pmb{x}_1
  \end{align}$$
  </li>
  <li>A smoothing estimate may be produced in a variety of ways, exploiting different formulations of the Bayesian problem.</li>
   <li>We may estimate only a <b>marginal</b> as on the left-hand-side, or the <strong>entire joint posterior</strong> as in the integrand above.<sup>1</sup></li>
   <li>Depending on how the Bayesian analysis is performed, one can <b>design different estimators to exploit the operational problem</b>.</li>
</ul>
</div>
<div style="width:100%;float:left;font-size:30px;">
<b>1.</b> Cosme, E., et al. (2012). Smoothing problems in a Bayesian framework and their linear Gaussian solutions. Monthly Weather Review, 140(2), 683-695.
</div>

========================================================

## Hidden Markov models


<ul>
  <li> Recall the <b style="color:#1b9e77">physical state model</b> and <b style="color:#7570b3">forward observation model</b>, 
  $$\begin{align}
  \pmb{x}_k &= \mathcal{M}_{k} \left(\pmb{x}_{k-1}\right)\\
  \pmb{y}_k &= \mathcal{H}_k \left(\pmb{x}_k\right) + \boldsymbol{\epsilon}_k
  \end{align}$$</li>
  <li>Denote <b style="color:#1b9e77">state model</b> and <b style="color:#7570b3">observation model</b> time series for $k &lt; l$ as,
  $$\begin{align}
\pmb{x}_{l:k} := \left\{\pmb{x}_l, \pmb{x}_{l-1}, \cdots, \pmb{x}_k\right\}, & &
\pmb{y}_{l:k} := \left\{\pmb{y}_l, \pmb{y}_{l-1}, \cdots, \pmb{y}_k\right\}. 
\end{align}$$</li>
  <li><b>Assume</b> that the sequence of <b style="color:#7570b3">observation error</b> 
    $$\begin{align}
    \{\boldsymbol{\epsilon}_k :  k=1,\cdots, L, \cdots\}
    \end{align}$$
    is <strong>independent in time</strong>.</li> 
  <li>The above formulation is a type of <b>hidden Markov model</b>;</li>
  <ul>
    <li>the dynamic state variables $\pmb{x}_k$ are known as the <b>hidden variables</b>, because they <strong>are not directly observed</strong>. </li>
    </ul>
  <li>These assumptions determine the <b>Markov probability densities</b> for the hidden variables, i.e.,
  $$\begin{align}
  p\left(\pmb{x}_{L:0}\right) &= p\left(\pmb{x}_{L} \vert \pmb{x}_{L-1:0}\right) p\left(\pmb{x}_{L-1:0}\right)\\
  &= p\left(\pmb{x}_{L} \vert \pmb{x}_{L-1}\right) p\left(\pmb{x}_{L-1:0} \right).
  \end{align}$$</li>
  <li>Applying the <b>Markov</b> property <strong>recursively</strong>,
  $$p\left(\pmb{x}_{L:0}\right) = p(\pmb{x}_0) \prod_{k=1}^{L} p(\pmb{x}_k|\pmb{x}_{k-1}).$$</li>
  <li>Similarly,
  $$p\left(\pmb{y}_{k}\vert \pmb{x}_k, \pmb{y}_{k-1:1}\right) = p\left(\pmb{y}_k \vert \pmb{x}_k\right)=p_{\pmb{\epsilon}_k}\left(\pmb{y}_k - \mathcal{H}_k(\pmb{x})\right)$$
  by the <strong>independence assumption</strong> on the <b style="color:#7570b3">observation</b> errors.</li>
</ul>

========================================================
## Bayesian inference

<ul>
  <li>Using these assumptions and Bayes' law, the  filtering cycle is written as
  $$\begin{align}
  {\color{#d95f02} {p\left(\pmb{x}_{L} \vert \pmb{y}_{L:1}\right)} } &=\frac{ {\color{#7570b3} { p\left(\pmb{y}_L \vert \pmb{x}_L\right) } } {\color{#1b9e77} { p\left(\pmb{x}_L\vert   \pmb{y}_{L-1:1}\right) } } }{p\left(\pmb{y}_L\vert \pmb{y}_{L-1:1}\right)}.
  \end{align}$$</li>
  <li>where:
  <ul>
    <li>${\color{#d95f02} {p\left(\pmb{x}_{L} \vert \pmb{y}_{L:1}\right)}}$ -- this is the <strong style="color:#d95f02">posterior estimate for the hidden states (at the current time)</strong> given all observations $\pmb{y}_{L:1}$;</li>
    <li>${\color{#7570b3} {p\left(\pmb{y}_{L}\vert \pmb{x}_{L}\right)}}$ -- this is the <strong style="color:#7570b3">likelihood of the observed data given our model forecast</strong>;</li>
    <li>${\color{#1b9e77} {p\left(\pmb{x}_L\vert   \pmb{y}_{L-1:1}\right)}}$ -- this is the <strong style="color:#1b9e77">model forecast-prior</strong> from our last best estimate of the state.</li>
    <ul>
      <li>Suppose that the <b style="color:#d95f02">posterior probability density</b> ${\color{#d95f02} {p(\pmb{x}_{L-1} \vert \pmb{y}_{L-1:1})}}$ at the <strong>last observation time</strong> $t_{L-1}$ is computed;</li>
      <li>then the <span style="color:#1b9e77;font-weight:bold">model forecast probability density</span></b> is given by,
      $$\begin{align}
      {\color{#1b9e77} {p(\pmb{x}_L\vert \pmb{y}_{L-1:1})} } &= \int p(\pmb{x}_L \vert \pmb{x}_{L-1}) {\color{#d95f02} {p(\pmb{x}_{L-1} \vert \pmb{y}_{L-1:1})} }\mathrm{d}\pmb{x}_{L-1}
      \end{align}$$</li>
    </ul>
    <li>$p\left(\pmb{y}_L \vert \pmb{y}_{L-1:1}\right)$ is the <b>marginal of joint density</b> $p( \pmb{y}_L, \pmb{x}_L \vert \pmb{y}_{L-1:1})$ <strong>integrating out the hidden variable</strong>,
    $$p\left(\pmb{y}_L \vert \pmb{y}_{L-1:1}\right) = \int p(\pmb{y}_L \vert \pmb{x}_L) p(\pmb{x}_L \vert \pmb{y}_{L-1:1})\mathrm{d}\pmb{x}_{L}.$$
  </ul>
</ul>   


========================================================

## Bayesian MAP estimates


<ul>
  <li>Typically, the probability density in the denominator
  $$p\left(\pmb{y}_L \vert \pmb{y}_{L-1:1}\right) = \int p(\pmb{y}_L \vert \pmb{x}_L) p(\pmb{x}_L \vert \pmb{y}_{L-1:1})\mathrm{d}\pmb{x}_{L}$$
  is <b>mathematically intractable</b>.</li>
  <ul>
    <li>However, the <strong>denominator is independent of the hidden variable</strong> $\pmb{x}_{L}$;</li>
    <ul>
      <li>its purpose is only to <strong>normalize the integral of the posterior density to $1$</strong> over all $\pmb{x}_{L}$.</li>
    </ul>
  </ul>
  <li>Instead, as a proportionality statement,
  $$\begin{align}
  {\color{#d95f02} {p\left(\pmb{x}_{L} \vert \pmb{y}_{L:1}\right)} } &\propto {\color{#7570b3} { p\left(\pmb{y}_L \vert \pmb{x}_L\right) } } {\color{#1b9e77} { p\left(\pmb{x}_L\vert   \pmb{y}_{L-1:1}\right) } } ,
  \end{align}$$</li>
  <li>we can devise the <b>Bayesian maximum a posteriori (MAP) estimate</b> as the choice of $\overline{\pmb{x}}_L$ that maximizes the posterior density,</li>
  <ul>
    <li>but written in terms of the two right-hand-side components.</li>
  </ul>
  <li><b>Maximizing the posterior density</b>, the <strong>denominator leads to insignificant constants that we can neglect</strong>.</li>
  <ul>
    <li><strong>Computing the MAP sequentially and recursively in time</strong>, we only need a <b>recursion in proportionality as above</b>.</li> 
  </ul>

========================================================

### Bayesian MAP estimates
<ul>
  <li>Under the <strong>``linear-Gaussian'' assumption</strong>, the optimal filtering problem is equivalent to the <b>Bayesian MAP cost function</b>
$$\begin{align}
{\color{#d95f02} {\mathcal{J}(\pmb{x}_{L})} } &= {\color{#1b9e77} {\frac{1}{2}\parallel  \overline{\pmb{x}}_{L}^\mathrm{fore} -\pmb{x}_{L}\parallel_{\mathbf{B}_{L}^\mathrm{fore}}^2} } + {\color{#7570b3} {\frac{1}{2}\parallel\pmb{y}_L - \mathbf{H}_L \pmb{x}_L\parallel_{\mathbf{R}_L}^2} },
\end{align}$$
where the above weighted norms can be understood as:
<ul>
  <li>$\parallel \circ \parallel_{\mathbf{B}_k^\mathrm{fore}}$ weighting relative to the  <b style="color:#1b9e77">forecast covariance (spread)</b>; and 
  <li>$\parallel \circ \parallel_{\mathbf{R}_k}$ weighting relative to the <b style="color:#7570b3">observation error covariance (imprecision)</b>.</li>
</ul>
<li>The <b style="color:#d95f02">MAP state interpolates</b> the <b style="color:#1b9e77">forecast mean</b> and the <b style="color:#7570b3">observational data</b> <strong>relative to the uncertainty in each piece of data</strong>.</li>
<li>To render the cost function into <b>right-transform analysis</b>, write the matrix factor
$$\begin{align}
\mathbf{B}_{L}^\mathrm{fore} : = \boldsymbol{\Sigma}_{L}^\mathrm{fore} \left(\boldsymbol{\Sigma}_{L}^\mathrm{fore}\right)^\top.
\end{align}$$</li>
<li>The analysis can be written in terms of <strong>optimizing weights $\pmb{w}$</strong> where
$$\begin{align}
\pmb{x}_L := \overline{\pmb{x}}_L^\mathrm{fore} + \boldsymbol{\Sigma}_L^\mathrm{fore}\pmb{w};
\end{align}$$</li>
<li>the equation written in terms of the weights is given as
$$\begin{align}
{\color{#d95f02} {\mathcal{J}(\pmb{w}) } } = {\color{#1b9e77} {\frac{1}{2} \parallel \pmb{w}\parallel^2} } + {\color{#7570b3} {\frac{1}{2} \parallel \pmb{y}_L - \mathbf{H}_L \overline{\pmb{x}}_L^\mathrm{fore} - \mathbf{H}_L \boldsymbol{\Sigma}_L^\mathrm{fore} \pmb{w} \parallel_{\mathbf{R}_L}^2 } }.
\end{align}$$</li>
</ul>

========================================================

### Bayesian MAP estimates

<div style="float:left; width:100%">
<ul>
  <li>Make the following definitions:
  
  $$\begin{align}
  \overline{\pmb{y}}_L = \mathbf{H}_L \overline{\pmb{x}}_L^\mathrm{fore}, & &
  \overline{\pmb{\delta}}_L &= \mathbf{R}^{-\frac{1}{2}}_L \left(\pmb{y}_L - \overline{\pmb{y}}_L\right), & &
  \boldsymbol{\Gamma}_L  =\mathbf{R}_L^{-\frac{1}{2}}\mathbf{H}_L \boldsymbol{\Sigma}_L^\mathrm{fore}.
  \end{align}$$
</li>
<ul>
  <li>The vector $\overline{\pmb{y}}_L$ is the <b>forecast mean</b> <strong>mapped to observation space</strong>.</li>
  <li> The vector $\overline{\pmb{\delta}}$ is the <b>innovation vector</b>, <strong>weighted by the observation uncertainty</strong>.</li>
  <li> $\boldsymbol{\Gamma}_L$ in <b>one dimension</b> would equal the  <b style="color:#1b9e77">standard deviation of the  model forecast</b> <strong>relative to</strong> the <b style="color:#7570b3">standard deviation of the observation error</b>.</li>
</ul>
<li> Then, the MAP cost function is further reduced to
  $$\begin{align}
  {\color{#d95f02} {\mathcal{J}(\pmb{w}) } } = {\color{#1b9e77} {\frac{1}{2} \parallel \pmb{w}\parallel^2}} +  {\color{#7570b3} {\frac{1}{2} \parallel \overline{\pmb{\delta}}_L  - \boldsymbol{\Gamma}_L \pmb{w} \parallel^2 } }
  \end{align}$$
</li>
<li> This cost function is quadratic in $\pmb{w}$ and can be <b>globally minimized</b> where $\nabla_{\pmb{w}} \mathcal{J} = \pmb{0}$.</li>
<li>Solving this is similar to solving the <strong>normal equations of least-squares regression</strong>;</li>
<ul>
  <li> indeed, the <b>Kalman filter</b> is also the <b>best linear unbiased estimator (BLUE)</b> for <strong>linear-Gaussian hidden Markov models</strong>.<sup>2</sup></li>
</ul>
<li>Note, the MAP weights $\overline{\pmb{w}}$ don't themselves provide an update to the forecast covariance $\mathbf{B}_L^\mathrm{fore}$.</li> 
<li>A sub-optimal approach is to assume that the background covariance $\mathbf{B}_L^\mathrm{fore} \equiv \mathbf{B} \equiv \mathbf{B}_L^\mathrm{filt}$ is completely invariant-in-time.</li>
<ul>
  <li>This 3D-VAR approach is computationally cost-effective, but <b>lacks the information</b> of the <b style="color:#1b9e77">time-dependent forecast spread</b>.</li>
</ul>
<li>In the simplified linear-Gaussian model, we can <strong>find a recursive form for the filter covariance</strong>;</li>
<ul>
  <li>the forecast model propagates the filter covariance, so that one can <b>recursively solve this equation in time</b>.</li>
</ul>
</ul>
</div>
<div style="width:100%;float:left;font-size:30px;">
<b>2.</b> Asch, M., Bocquet, M., & Nodet, M. (2016). Data assimilation: methods, algorithms, and applications. Society for Industrial and Applied Mathematics.
</div>


========================================================

### Bayesian MAP estimates

* Setting the <b>gradient</b> $\nabla_{\pmb{w}} \mathcal{J}$ equal to zero for $\overline{\pmb{w}}$ we find the critical value as
  
  $$\begin{align}
  \overline{\pmb{w}} = \pmb{0} - {\boldsymbol{\Xi}_\mathcal{J}}^{-1} \nabla_{\pmb{w}} \mathcal{J}|_{\pmb{w}=\pmb{0}}.
  \end{align}$$
  where $\boldsymbol{\Xi}_\mathcal{J}:= \nabla^2_{\pmb{w}}\mathcal{J}$ is the <b>Hessian of the cost function</b>.
  * This corresponds to a single iteration of <b>Newton's descent algorithm</b>.

* The forecast mean is updated as,
  
  $$\begin{align}
  \overline{\pmb{x}}_L^\mathrm{filt}:= \overline{\pmb{x}}_{L}^\mathrm{fore} + \boldsymbol{\Sigma}_{L}^\mathrm{fore} \overline{\pmb{w}}.
  \end{align}$$

* Defining a right-transform matrix, $\mathbf{T}:= \boldsymbol{\Xi}^{-\frac{1}{2}}_{\mathcal{J}}$,  the update for the covariance is given as
  
  $$\begin{align}
  \mathbf{B}^\mathrm{filt}_L = \left(\boldsymbol{\Sigma}_L^\mathrm{fore} \mathbf{T} \right)\left(\boldsymbol{\Sigma}_L^\mathrm{fore} \mathbf{T} \right)^\top.
  \end{align}$$
  
* This derivation sketches the <b>square root Kalman filter</b>,<sup>3</sup> written for the <strong>perfect, linear-Gaussian model</strong>.

* Under the <b>perfect model assumption</b>, the forecast is furthermore written

  $$\begin{align}
  \overline{\pmb{x}}_{L+1}^\mathrm{fore}:= \mathbf{M}_{L+1} \overline{\pmb{x}}_{L}^{\mathrm{filt}} & & \boldsymbol{\Sigma}_{L+1}^\mathrm{fore} := \mathbf{M}_{L+1}\left(\boldsymbol{\Sigma}_{L}^\mathrm{filt}\right)
  \end{align}$$
  giving a <strong>complete recursion in time, within the matrix factor</strong>.
  
<div style="width:100%;float:left;font-size:30px;">
<b>3.</b> Tippett, M. K., Anderson, J. L., Bishop, C. H., Hamill, T. M., & Whitaker, J. S. (2003). <i>Ensemble square root filters</i>. Monthly Weather Review, 131(7), 1485-1490.
</div>

========================================================

## The ETKF


* The <b style="color:#d95f02">square root Kalman filter</b> analysis is written entirely in terms of the weight vector $\overline{\pmb{w}}$ and the right-transform matrix $\mathbf{T}$.

  * The cost of computing $\boldsymbol{\Xi}_{\mathcal{J}}^{-1}$ and $\mathbf{T}:=\boldsymbol{\Xi}_{\mathcal{J}}^{-\frac{1}{2}}$ are <strong>both subordinate to the cost of the singular value decomposition</strong> of $\boldsymbol{\Xi}_{\mathcal{J}}$.

* This is core to the efficiency of the <b>ensemble transform Kalman filter (ETKF),</b><sup>4</sup> using a reduced-rank approximation to the background $\mathbf{B}^\mathrm{i}_L$.

* Given an <b>ensemble matrix</b> $\mathbf{E}^\mathrm{i}_L \in \mathbb{R}^{N_x \times N_e}$

  * the <strong>columns are assumed</strong> an <b>independent identically distributed (iid)</b> sample of some distribution corresponding to the label $\mathrm{i}$.

  * In weather and climate models $N_e \ll N_x$, and $N_x$ can be on order $\mathcal{O}\left(10^9\right)$;<sup>5</sup>
  
  * $N_e$ is typically on order $\mathcal{O}\left(10^2\right)$.
  
* Writing the <strong>cost function restricted to the ensemble span</strong>, we have a <b>restricted Hessian</b> $\boldsymbol{\Xi}_{\widetilde{\mathcal{J}}}$ of the form
 
 $$\begin{align}
 \boldsymbol{\Xi}_\mathcal{\widetilde{J}} \in \mathbb{R}^{N_e \times N_e}.
 \end{align}$$

<div style="width:100%;float:left;font-size:30px;">
<b>4.</b> Sakov, P., & Oke, P. R. (2008). Implications of the form of the ensemble transformation in the ensemble square root filters. Monthly Weather Review, 136(3), 1042-1053.<br>
<b>5.</b> Carrassi, A., Bocquet, M., Bertino, L., & Evensen, G. (2018). <i>Data assimilation in the geosciences: An overview of methods, issues, and perspectives</i>. Wiley Interdisciplinary Reviews: Climate Change, 9(5), e535.
</div>

========================================================

## The ETKF

* Using <b>ensemble-based, empirical estimates</b>,
  
  $$\begin{align}
  & & \hat{\pmb{x}}_L^\mathrm{fore} &= \mathbf{E}_L^\mathrm{fore} \pmb{1} / N_e ; & 
  \hat{\pmb{\delta}}_L &= \mathbf{R}_k^{-\frac{1}{2}}\left(\pmb{y}_L - \mathbf{H}_L \hat{\pmb{x}}_L\right)\\
  &&\mathbf{X}_L^\mathrm{fore} &= \mathbf{E}_L^\mathrm{fore} - \hat{\pmb{x}}^\mathrm{fore}_L \pmb{1}^\top ; & 
  \mathbf{P}^\mathrm{fore}_L &= \mathbf{X}_L^\mathrm{fore} \left(\mathbf{X}_L^\mathrm{fore}\right)^\top / \left(N_e - 1\right);\\
  & &\mathbf{S}_L &:=\mathbf{R}_L^{-\frac{1}{2}}\mathbf{H}_L \mathbf{X}_L^\mathrm{fore};
  \end{align}$$

* the <strong>ensemble-based cost function</strong> is written as
  
  $$\begin{alignat}{2}
  & & {\color{#d95f02} {\widetilde{\mathcal{J}} (\pmb{w})} } &= {\color{#1b9e77} {\frac{1}{2} \parallel \hat{\pmb{x}}_L^\mathrm{fore} - \mathbf{X}^\mathrm{fore}_L \pmb{w}- \hat{\pmb{x}}^\mathrm{fore}_L \parallel_{\mathbf{P}^\mathrm{fore}_L}^2} } + {\color{#7570b3} {\frac{1}{2} \parallel \pmb{y}_L - \mathbf{H}_L\hat{\pmb{x}}^\mathrm{fore}_L - \mathbf{H}_L \mathbf{X}^\mathrm{fore}_L \pmb{w} \parallel_{\mathbf{R}_L}^2 } }\\
  \Leftrightarrow& & {\color{#d95f02} {\widetilde{\mathcal{J}}(\pmb{w})} } &= {\color{#1b9e77} {\frac{1}{2}(N_e - 1) \parallel\pmb{w}\parallel^2} } + {\color{#7570b3} {\frac{1}{2}\parallel \hat{\pmb{\delta}}_L - \mathbf{S}_L \pmb{w}\parallel^2 } }
  \end{alignat}$$
  which is an <b>optimization over a weight vector $\pmb{w}$ in the ensemble dimension $N_e$</b> <strong>rather than in the state space dimension $N_x$</strong>.
  
* This a key reduction that <b>makes Monte Carlo methods feasible</b> for the large size of geophysical models.

  * Still, other techniques such as <strong>covariance localization<sup>6</sup> and hybridization<sup>7</sup> are used in practice to overcome the curse of dimensionality</strong>.

<div style="width:100%;float:left;font-size:30px;">
<b>6.</b> Sakov, P., & Bertino, L. (2011). Relation between two common localisation methods for the EnKF. Computational Geosciences, 15(2), 225-237.<br>
<b>7.</b> Penny, S. G. (2017). Mathematical foundations of hybrid data assimilation from a synchronization perspective. Chaos: An Interdisciplinary Journal of Nonlinear Science, 27(12), 126801.<br>
</div>


========================================================

### The ETKF
<ul>
  <li> This is a sketch of the derivation of the <b>local ensemble transform Kalman filter (LETKF)</b>.<sup>8</sup></li>
  <li>In this formalism, an <b>ensemble right-transform</b> $\boldsymbol{\Psi}_k$ exists such that for any $t_k$,

 $$\begin{align}
 \mathbf{E}^\mathrm{filt}_k = \mathbf{E}^\mathrm{fore}_k \boldsymbol{\Psi}_k
 \end{align}$$
  where in the above we would say that (approximately)
  $$\begin{align}
  \mathbf{E}^\mathrm{filt}_k &\sim p(\pmb{x}_k \vert \pmb{y}_{k:1}) \\
  \mathbf{E}^\mathrm{fore}_k &\sim p(\pmb{x}_k \vert \pmb{y}_{k-1:1})
  \end{align}$$</li>

  <li>We will associate $\mathbf{E}^\mathrm{filt}_L \equiv \mathbf{E}^\mathrm{smth}_{L|L}$;</li>
  <ul>
    <li>under the <strong>linear-Gaussian model</strong>, we furthermore have that

  $$\begin{align}
  \mathbf{E}^\mathrm{smth}_{k |L} = \mathbf{E}^\mathrm{smth}_{k|L-1}\boldsymbol{\Psi}_{L} & &
  \mathbf{E}^\mathrm{smth}_{k|L} \sim p(\pmb{x}_k \vert \pmb{y}_{L:1}).
  \end{align}$$</li>
  </ul>
  <li> A <b style="color:#d95f02">retrospective smoothing analysis</b> can be performed on all past states stored in memory <strong>using the latest right-transform update from the filtering step</strong>.</li>
  <li>This form of <b style="color:#d95f02">retrospective analysis</b> is the basis of the <b>ensemble Kalman smoother (EnKS)</b>.<sup>9</sup></li>
</ul>

<div style="width:100%;float:left;font-size:30px">
<b>8.</b> Hunt, B. R., Kostelich, E. J., & Szunyogh, I. (2007). <i>Efficient data assimilation for spatiotemporal chaos: A local ensemble transform Kalman filter</i>. Physica D: Nonlinear Phenomena, 230(1-2), 112-126.<br>
<b>9.</b> Evensen, G., & Van Leeuwen, P. J. (2000). <i>An ensemble Kalman smoother for nonlinear dynamics. Monthly Weather Review, 128(6), 1852-1867.</i>
</div>

========================================================

### The EnKS

<div style="float:left; width:100%">
<ul>
  <li>The EnKS takes advantage of the simple form of the <b style="color:#d95f02">retrospective, right-transform analysis</b> by including an <strong>additional, inner loop of the filtering cycle</strong>.</li>
</ul>
</div>
<div style="float:left; width:100%; text-align:center;" class="fragment">
<img style="width:60%", src="enks_scheme.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:left; width:100%">
<ul>
    <li><b>Time is the horizontal axis</b> where right moves forward in time.</li>
    <li>At each time, we produce the standard <b style="color:#d95f02">filtering estimate</b> by computing $\boldsymbol{\Psi}_L$ from the cost function, and updating the <b style="color:#1b9e77">forecast</b> 
    $$\mathbf{E}^\mathrm{filt}_L = \mathbf{E}_L^\mathrm{fore} \boldsymbol{\Psi}_L.$$</li> 
    <li>The <b style="color:#7570b3">information of incoming observations</b> is <strong>passed backward in time using the right-transform</strong> to condition the ensemble at past times:
    $$\begin{align}
    \mathbf{E}^\mathrm{smth}_{k|L} = \mathbf{E}^\mathrm{smth}_{k|L-1} \boldsymbol{\Psi}_L.
    \end{align}$$
</ul>
</div>

========================================================

## The 4D cost function
<div style="float:left; width:100%;">
<ul>
  <li><b>However</b>, re-initializing the DA cycle with the <b style="color:#d95f02">smoothed conditional ensemble estimate</b> $\mathbf{E}^\mathrm{smth}_{0|L}$ can <strong>dramatically improve the performance of the subsequent forecast and filtering statistics</strong>.</li>
  <ul>
    <li>Let us denote the <b style="color:#1b9e77">composition of the model forecast</b> as,
  $$\begin{align}
  \\
  \mathcal{M}_{l:k} : = \mathcal{M}_l \circ \cdots \circ \mathcal{M}_{k} & & \mathbf{M}_{l:k} := \mathbf{M}_{l}\cdots \mathbf{M}_{k}
  \end{align}$$</li>
  </ul>
  <li>This <b>exploits the miss-match</b> in nonlinear dynamics between
  $$\begin{align}
  \\
  \mathcal{M}_{L:1}\left(\mathbf{E}_{0|L}^\mathrm{smth}\right):= \mathcal{M}_L \circ \cdots \circ \mathcal{M}_1\left(\mathbf{E}_{0|L}^\mathrm{smth}\right) \neq \mathbf{E}_{L}^\mathrm{filt}.
  \end{align}$$
  </li>
  <li>The effectiveness of the <b>linear-Gaussian approximation</b> strongly depends on the <strong>length of the forecast window</strong> $\Delta t$;</li>
  <ul>
    <li>for small $\Delta t$, the <strong>densities are well-approximated with Gaussians</strong>, yet there are <b>deformations induced due to nonlinearity</b>.</li>
  </ul>
  <li> When the dynamics are <b>weakly nonlinear</b>, correlations between the model forecast and the initial condition bring <strong>new information into the forecast states in the next DAW</strong>.</li>
  <li> This has been exploited to a great extent by utilizing the <b>4D cost function;</b></li>
  <ul>
    <li>the filtering MAP cost function is <strong>extended over multiple observations simultaneously, and in terms of a lagged state directly</strong>.</li>
  </ul>
</ul>
</div>


========================================================

### The 4D cost function

<div style="float:left; width:100%;">
<ul>
  <li> Suppose now we want to write $p(\pmb{x}_{L:1}\vert \pmb{y}_{L:1})$, the <b style="color:#d95f02">joint smoothing posterior</b> over the current DAW, as a <strong>recursive update</strong> to the last <b style="color:#d95f02">smoothing posterior</b>.</li>
</ul>
</div>
<div style="float:left; width:100%; text-align:center;" class="fragment">
<img style="width:60%", src="cycling.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:left; width:100%">
<ul>
  <li> Using a Bayesian analysis like before, we can write 
  $$\begin{align}
  {\color{#d95f02} { p(\pmb{x}_{L:1} \vert \pmb{y}_{L:1}) } }
  &\propto  \int \mathrm{d}\pmb{x}_0 \underbrace{ {\color{#d95f02} { p(\pmb{x}_0 \vert \pmb{y}_{L-S:-S}) } } }_{(1)} \underbrace{ {\color{#7570b3} { \left[ \prod_{k=L-S+1}^L   p(\pmb{y}_k \vert \pmb{x}_k) \right] } }}_{(2)} \underbrace{{\color{#1b9e77} {  \left[\prod_{k=1}^L p(\pmb{x}_k|\pmb{x}_{k-1}) \right]  } }}_{(3)}
  \end{align}$$
  where</li>
  <ol>
    <li> is the marginal for $\pmb{x}_0$ of the last <b style="color:#d95f02">joint smoothing smoothing posterior</b> $p(\pmb{x}_{L-S:-S}\vert\pmb{y}_{L-S:-S})$;</li>
    <li> is the <b style="color:#7570b3">joint likelihood of the incoming observations</b> to the current DAW, given the background forecast;</li>
    <li> is the <b style="color:#1b9e77">free-forecast with the perfect model</b> $\mathcal{M}_k$.
  </ol>
  </ul>
</div>

========================================================

### The 4D cost function
<div style="float:left; width:100%">
<ul>
  <li>Under the <b>linear-Gaussian assumption</b>, the resulting cost function takes the form
  $$\begin{alignat}{2}
  & & {\color{#d95f02} {\mathcal{J} (\pmb{w})} } &= {\color{#d95f02} {\frac{1}{2} \parallel \overline{\pmb{x}}_{0|L-S}^\mathrm{smth} - \boldsymbol{\Sigma}^\mathrm{smth}_{0|L-S} \pmb{w}- \overline{\pmb{x}}^\mathrm{smth}_{0|L-S} \parallel_{\mathbf{B}^\mathrm{smth}_{0|L-S}}^2} } + {\color{#7570b3} {\sum_{k=L-S+1}^L \frac{1}{2} \parallel \pmb{y}_k - \mathbf{H}_k {\color{#1b9e77} { \mathbf{M}_{k:1}} } {\color{#d95f02} {\overline{\pmb{x}}^\mathrm{smth}_{0|L-S}} } - \mathbf{H}_k {\color{#1b9e77} {\mathbf{M}_{k:1}}} {\color{#d95f02} {\boldsymbol{\Sigma}^\mathrm{smth}_{0|L-S} \pmb{w} }} \parallel_{\mathbf{R}_k}^2 } } \\
  \Leftrightarrow& & \mathcal{J}(\pmb{w}) &= \frac{1}{2}\parallel\pmb{w}\parallel^2 + \sum_{k=L-S+1}^L \frac{1}{2}\parallel \overline{\pmb{\delta}}_k - \boldsymbol{\Gamma}_k \pmb{w}\parallel^2 .
  \end{alignat}$$</li>
  <li> In the <b>linear-Gaussian case</b>, the solution can again be found by a <strong>single iteration of Newton's descent</strong>
  $$\begin{align}
  \nabla_{\pmb{w}} \mathcal{J}:= \pmb{w} - \sum_{k=L-S+1}^{L}\boldsymbol{\Gamma}^\top_k \left(\overline{\pmb{\delta}}_k - \boldsymbol{\Gamma}_k \pmb{w}\right), & &
\mathbf{H}_{\mathcal{J}} := \mathbf{I} + \sum_{k=L-S+1}^L \boldsymbol{\Gamma}_k^\top \boldsymbol{\Gamma}_k, & &
 \overline{\pmb{w}} := \pmb{0} - \mathbf{H}_{\mathcal{J}}^{-1} \nabla_{\pmb{w}} \mathcal{J}|_{\pmb{w}=\pmb{0}}\\
 \overline{\pmb{x}}_{0|L}^\mathrm{smth} = \overline{\pmb{x}}^\mathrm{smth}_{0|L-S} + \boldsymbol{\Sigma}_{0|L-S}^\mathrm{smth} \overline{\pmb{w}} & & \mathbf{T}:= \mathbf{H}_{\mathcal{J}}^{-\frac{1}{2}} & &\boldsymbol{\Sigma}_{0|L}^\mathrm{smth}:= \boldsymbol{\Sigma}_{0|L-S}^\mathrm{smth}\mathbf{T}
 \end{align}$$</li>
 <li>  However, when the <b>state and observation model are nonlinear</b>, using $\mathcal{H}_k$ and $\mathcal{M}_{k:1}$ in the cost function, this <strong>cost function is solved iteratively to find a local minimum</strong>.</li>
  <li> The difficulty arises in that the gradient $\nabla_{\pmb{w}}$ actually requires <b style="color:#1b9e77">differentiating the equations of motion</b> in $\mathcal{H}_k\circ\mathcal{M}_{k:1}$.</li>
  <li> In <b>4D-VAR</b>, this is performed by an <strong>incremental linearization in the tangent linear model and back propagation of sensitivities by the adjoint model</strong>;</li>
  <ul>
    <li>this can also be hybridized with an ensemble in various forms of <b>ensemble-variational (EnVAR)</b> techniques.<sup>10</sup></li>
  </ul>
</ul>
</div>
<div style="width:100%;float:left;font-size:30px;">
<b>10.</b> Bannister, R. N. (2017). A review of operational methods of variational and ensemble‐variational data assimilation. Quarterly Journal of the Royal Meteorological Society, 143(703), 607-633.
</div>

========================================================
## Hybrid EnVAR in the EnKF analysis

* One alternative to constructing the tangent-linear and adjoint models is to perform a hybrid,  analysis as based on the ETKF.

* This approach is at the basis of the <b>iterative ensemble Kalman filter / smoother (IEnKF/S)</b>.<sup>11</sup>

* This technique seeks to perform an ensemble analysis like the square root ETKF by <strong>defining the ensemble estimates and the weight vector directly in the ensemble span</strong>

  $$\begin{alignat}{2}
  & & {\color{#d95f02} {\widetilde{\mathcal{J}} (\pmb{w})} } &= {\color{#d95f02} {\frac{1}{2} \parallel \hat{\pmb{x}}_{0|L-S}^\mathrm{smth} - \mathbf{X}^\mathrm{smth}_{0|L-S} \pmb{w}- \hat{\pmb{x}}^\mathrm{smth}_{0|L-S} \parallel_{\mathbf{P}^\mathrm{smth}_{0|L-S}}^2} } + {\color{#7570b3} {\sum_{k=L-S+1}^L \frac{1}{2} \parallel \pmb{y}_k - \mathcal{H}_k\circ {\color{#1b9e77} { \mathcal{M}_{k:1}\left( {\color{#d95f02} { \hat{\pmb{x}}^\mathrm{smth}_{0|L-S} +  \mathbf{X}^\mathrm{smth}_{0|L-S} \pmb{w} } } \right)}}\parallel_{\mathbf{R}_k}^2 } }\\
 \Leftrightarrow & & {\color{#d95f02} {\widetilde{\mathcal{J}} (\pmb{w})} } &= {\color{#d95f02} {(N_e - 1) \frac{1}{2} \parallel \pmb{w}\parallel^2} } + {\color{#7570b3} {\sum_{k=L-S+1}^L \frac{1}{2} \parallel \pmb{y}_k - \mathcal{H}_k\circ {\color{#1b9e77} { \mathcal{M}_{k:1}\left( {\color{#d95f02} { \hat{\pmb{x}}^\mathrm{smth}_{0|L-S} +  \mathbf{X}^\mathrm{smth}_{0|L-S} \pmb{w} } } \right)}}\parallel_{\mathbf{R}_k}^2 } }.
  \end{alignat}$$


* The scheme produces an <b>iterative estimate</b> using a <strong>Gauss-Newton</strong>-<sup>11</sup> or, e.g., <strong>Levenberg-Marquardt</strong>-based<sup>12</sup> optimization.


<div style="width:100%;float:left;font-size:30px">
<b>11.</b> Bocquet, M., & Sakov, P. (2014).<i> An iterative ensemble Kalman smoother</i>. Quarterly Journal of the Royal Meteorological Society, 140(682), 1521-1535.<br>
<b>12.</b> Bocquet, M., & Sakov, P. (2012). Combining inflation-free and iterative ensemble Kalman filters for strongly nonlinear systems. NPG, 19(3), 383-399.<br>
</div>


========================================================

## The single iteration ensemble transform Kalman smoother (SIEnKS)

<div style="float:left; width:100%">
<ul>
  <li> Accuracy can increase with <b>iterations in the 4D estimate</b>, at the <b style="color:#1b9e77">cost of the state ensemble forecast</b> ${\color{#1b9e77} { \mathcal{M}_{L:1} } }$.</li>
  <li>In short-range forecasting the <b>linear-Gaussian approximation</b> of the evolution of the densities is actually an <strong>adequate approximation</strong>;</li>
  <ul>
    <li><b style="color:#1b9e77">iterating over the nonlinear dynamics</b> <strong>may not be justified by the improvement in the forecast statistics</strong>.</li>
  </ul>
  <li>However, the <b>iterative optimization over a nonlinear observation operator $\mathcal{H}_k$ or hyper-parameters in the filtering step</b> of the classical EnKS can be run <strong>without the additional cost of model forecasts</strong>.</li>
  <ul>
    <li>This can be performed similarly to the IEnKS with the <b>maximum likelihood ensemble filter (MELF)</b> analysis.<sup>13</sup></li>
  </ul>
  <li> Subsequently, the <b style="color:#d95f02">retrospective, right-transform analysis</b> can be applied to <b style="color:#d95f02">condition the initial ensemble</b>
 
 $$\begin{align}
 \mathbf{E}^\mathrm{smth}_{0|L} = \mathbf{E}_{0:L-1}^\mathrm{smth} \boldsymbol{\Psi}_L
 \end{align}$$</li>
  <li> As with the 4D cost function, one can <b>initialize the next DA cycle in terms of the retrospective analysis</b>, and gain the benefit of the improved initial estimate.</li>
  <li>This scheme, <strong>currently in open review</strong>, is the <b>single-iteration ensemble Kalman smoother (SIEnKS)</b>.<sup>14</sup></li>
</ul>
</div>
<div style="width:100%;float:left;font-size:30px">
<b>13.</b> Zupanski, M., et al. (2008). The Maximum Likelihood Ensemble Filter as a non-differentiable minimization algorithm. Quarterly Journal of the Royal Meteorological Society, 134, 1039–1050.<br>
<b>14.</b> Grudzien, C. and Bocquet, M. (2021): A fast, single-iteration ensemble Kalman smoother for sequential data assimilation. GMD Discussions [preprint], https://doi.org/10.5194/gmd-2021-306, in open review.
</div>
  
========================================================

### The single iteration ensemble Kalman smoother (SIEnKS)


<div style="float:left; width:100%">
<ul>
  <li>Compared to the classical EnKS, this <strong>adds an outer loop</strong> to the <b style="color:#d95f02">filtering cycle</b> to produce the <b style="color:#d95f02">posterior analysis</b>.</li>
</ul>
</div>
<div style="float:left; width:100%; text-align:center;" class="fragment">
<img style="width:65%", src="single_iteration_diagram.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:left; width:100%">
<ul>
  <li>The <b style="color:#7570b3">information flows</b> from the filtered state back in time from the <b style="color:#d95f02">retrospective analysis</b>.</li>
  <li>This re-analyzed state becomes the <b style="color:#1b9e77">initialization for the next cycle</b> over the shifted DAW, carrying this information forward.</li>
  <li>The iterative cost function is only solved in the <b>filtering estimate</b> for the <b style="color:#7570b3">new observations entering the DAW</b>.</li>
  <ul>
    <li>Combined with the retrospective analysis, this comes <b style="color:#1b9e77">without the cost of iterating the model forecast over the DAW</b>.</li>
  </ul>
  <li>For <b>short-range forecasting</b>, this is shown to be an <strong>accurate and highly efficient approach to sequential smoothing</strong>.</li>
</ul>
</div>

========================================================
### The single iteration ensemble Kalman smoother (SIEnKS)

<div style=float:left; width:100%">
<ul>
  <li>Our <b>key result</b> is an <strong>efficient multiple data assimilation (MDA)</strong><sup>15</sup>  scheme within the EnKS cycle.</li>
  <ul>
    <li>MDA is a technique based on statistical tempering<sup>16</sup> designed to relax the nonlinearity of the Bayesian MAP estimation.</li>
  </ul>
  <li>In a <b>single data assimilation (SDA) smoother</b>, each observation is only assimilated once so that <strong>new observations are only distantly connected to the initial conditions</strong> of the simulation;</li>
  <ul>
    <li>this can introduce many local minima to the 4D cost function, strongly affecting the optimization.<sup>17</sup></li>
  </ul>
  <li>MDA is designed to <b>artificially inflate observation errors</b> and <strong>weakly assimilate the same observation over multiple DAWs</strong>.</li>
  <ul>
    <li>This weakens the effects of local minima, and slowly brings the estimator close to a more optimal solution.<sup>18</sup></li>
  </ul>
  <li>However, the <b>SIEnKS treats MDA</b> <strong>differently than 4D-EnVAR estimators</strong> by using a classic EnKS cycle to weakly assimilate the observations over multiple passes.</li>
  <ul>
    <li>The filter step in this analysis is used as a <b>boundary condition</b> for the <strong>interpolation of the posterior over the lag window</strong>.</li>
  </ul>
   <li>This MDA scheme is demonstrated to be <b>more accurate, stable and cost-effective</b> than EnKF-based 4D-EnVAR schemes <strong>in short-range forecasts</strong>.</li>
   <ul>
    <li>Note, the <b>SIEnKS is not as robust as 4D estimates</b> in <strong>highly nonlinear forecast dynamics</strong>.</li>
   </ul>
</ul>
</div>
<div style="width:100%;float:left;font-size:30px">
<b>15.</b> Emerick, A. A., & Reynolds, A. C. (2013). Ensemble smoother with multiple data assimilation. Computers & Geosciences, 55, 3-15.<br>
<b>16.</b> Neal, R. M. (1996). Sampling from multimodal distributions using tempered transitions. Statistics and computing, 6(4), 353-366.<br>
<b>17.</b> Fillion, A., Bocquet, M., and Gratton, S. (2018). Quasi-static ensemble variational data assimilation: a theoretical and numerical study with the iterative ensemble Kalman smoother, NPG, 25, 315–334.<br>
<b>18.</b> Evensen, G.: Analysis of iterative ensemble smoothers for solving inverse problems, Computational Geosciences, 22, 885–908, 2018.
</div>

========================================================
### The single iteration ensemble Kalman smoother (SIEnKS)

<div style="float:left; width:100%; text-align:center;">
<img style="width:80%;", src="sda_heat_plot.png" alt="Ensemble statistics" class="fragment"/>
<div style="position:absolute; top:58px; left:0px; width:100%">
<img style="width:80%;", src="mda_heat_plot.png" alt="Ensemble statistics" class="fragment"/>
</div>
</div>


========================================================
### The single iteration ensemble Kalman smoother (SIEnKS)

<div style="float:left;  width:100%; text-align:center;">
<img style="width:80%;", src="sda_line_plot.png" alt="Ensemble statistics" class="fragment"/>
<div style="position:absolute; top:58px; left:0px; width:100%">
<img style="width:80%;", src="mda_line_plot.png" alt="Ensemble statistics" class="fragment"/>
</div>
</div>
<div style="float:left;  width:100%">
<div style="float:left; width:100%">
<ul>
  <li>The <b>data boundary condition</b> <strong>improves the forecast statistics</strong>, controlling the accumulated forecast error over lagged states unlike traditional 4D-EnVAR approaches.</li>
  <li>Similarly, the <b>interpolation of the posterior</b> estimate remains <strong>more stable over the DAW</strong>, when the forecast error dynamics are not highly nonlinear.</li>
</ul>
</div>

========================================================
### The single iteration ensemble Kalman smoother (SIEnKS)

<ul>
  <li>A <strong>wide variety of test cases</strong> for short-range forecast systems are presented in our manuscript<sup>19</sup>.</li>
  <ul>
    <li>We demonstrate improved accuracy at lower leading order cost of the SIEnKS with highly nonlinear observation operators, hyper-parameter optimization and other relevant tests.</li>
  </ul>
  <li>The <b>two qualifications</b> are that:
  <ol>
    <li>these <b>theoretical results</b> are based on the <strong>perfect model assumption for simplicity</strong> in this initial analysis; and</li>
    <li>we have <strong>not yet introduced localization or covariance hybridization</strong> in this initial study for simplicity.</li>
  </ol>
  <li>However, localization / hybridization are likely easy extensions based on the forecast regime that we target.</li>
  <li>Initial results in model error support the case that the SIEnKS can be modified for this regime.</li> 
  <li>Our mathematical results are <strong>supported by extensive numerical demonstration</strong>, with the <b>Julia package DataAssimilationBenchmarks.jl</b><sup>20</sup></li>
  <li>A wider survey of methods for Bayesian DA in the geosciences is available in my condensed lecture notes<sup>21</sup> which will be expanded upon in a longer-term book project.<sup>22</sup>
</ul>
  

<div style="width:100%;float:left;font-size:30px">
<b>19.</b> Grudzien, C. and Bocquet, M. (2021): A fast, single-iteration ensemble Kalman smoother for sequential data assimilation. GMD Discussions [preprint], https://doi.org/10.5194/gmd-2021-306, in open review.<br>
<b>20.</b> Grudzien, C., Sandhu, S. (2021). DataAssimilationBenchmarks.jl: a data assimilation research framework. In submission to The Journal of Open Source Software.<br>
<b>21.</b> Grudzien, C. and Bocquet, M. (2021). A Tutorial on Bayesian Data Assimilation. Invited submission to Applications of Data Assimilation and Inverse Problems in the Earth Sciences. Cambridge University Press.<br>
<b>22.</b> Carrassi, A., Grudzien, C., Bocquet, M., Farchi, A., Raanes, P. Data assimilation for dynamical system and their discovery through machine learning. Accepted Book Proposal in Springer-Nature.  Target submission in 2023.
</div>

