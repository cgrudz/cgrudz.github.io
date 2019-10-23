<style>
.section .reveal .state-background {
   background: #ffffff;
}
.section .reveal h1 {
   color: black;
   margin-top: 50px;
   text-align: center;
   font-size:80px;
}

.section .reveal h2,
.section .reveal p {
   color: black;
   margin-top: 50px;
   text-align: center;
}
</style>

On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments
========================================================
date: 13 November, 2019 
autosize: true
incremental: true
width: 1920
height: 1080

## Authors:

<div style="text-align:center">
<p><strong>Colin Grudzien<sup>1,3</sup>, Marc Bocquet<sup>2</sup> and Alberto Carrassi<sup>3,4</sup></strong></p>
<ol style="font-size:30px;text-align: center;list-style-position: inside;">
  <li>University of Nevada, Reno, Department of Mathematics and Statistics</li>
  <li>CEREA, A joint laboratory &Eacute;cole des Ponts Paris Tech and EDF R&D, Universit&eacute; Paris-Est, Champs-sur-Marne, France.</li>
  <li>Nansen Environmental and Remote Sensing Center, Bergen, Norway</li>
  <li>Mathematical Institute, University of Utrecht, the Netherlands</li>
</ol>
</div>

<div style="float:left; width:33%">
<img style="width:70%", src="NERSC_logo.png" alt="Nansen Environmental and Remote Sensing Center logo."/>
</div>
<div style="float:left; width:33%; text-align:center;">
<img style="width:70%", src="UNR_logo.png" alt="University of Nevada, Reno logo."/>
</div>
<div style="float:left; width:33%; text-align:right;padding-top:88.575px">
<img style="width:70%;", src="cerea_logo.png" alt="CEREA logo."/>
</div>

========================================================

## Outline

<ul>
  <li> Twin experiments in toy models</li>
  <li> Multiscale model reduction error and random dynamical systems</li>
  <li> Stochastic integration schemes and bias in model statistics</li>
  <li> Numerical benchmarks:</li>
  <ol>
    <li>Strong and weak convergence</li>
    <li>Ensemble forecast statistics</li>
    <li>Filtering statistics</li>
  </ol>
  <li>Conclusions and future work</li>
</ul>


========================================================

## Bayesian Data assimilation in the geosciences

<ul>
  <li><b>Ensemble-based forecasting</b> and <b>Data assimilation (DA)</b> are the prevailing modes of:</li> 
  <ol>
    <li><b>prediction</b>; and</li> 
    <li><b>uncertainty quantification</b></li> 
  </ol>
  <li>in geophysical modeling.</li>
  <li><b>DA combines</b> simulations from a <span style="color:green;font-weight:bold">physics-based numerical model</span> and <span style="color:blue; font-weight:bold">real-world observations</span> of a physical process.</li>
  <li><b>Bayesian framework:</b></li>
  <ul>
    <li>An <span style="color:green;font-weight:bold;">ensemble-based forecast</span> is a sampling procedure for the <span style="color:green;font-weight:bold;">forecast-prior probability density</span>.</li>
    <ul>
      <li>The physics-based numerical model (and previous estimates of the state) encapsulate the <span style="color:green;font-weight:bold;">Bayesian prior knowledge</span>.</li>
    </ul>
  <li>The output of DA is an estimate of a <span style="color:red; font-weight:bold">posterior probability density</span> for the numerically simulated physical state, or some statistic.</li>
  </ul>
  <li><b>Bias</b> in the <span style="color:green;font-weight:bold;">forecast-prior estimate</span> will introduce <b>bias</b> into the <span style="color:red; font-weight:bold">posterior probability density</span>.</li>
  <li>Therefore, <b>understanding</b> and <b>quantifying</b> <span style="color:green;font-weight:bold;">model bias</span> has become a central discussion in <b>ensemble-forecasting</b> and <b>DA</b>.</li>
</ul>


========================================================
## Bias in twin experiments

* Currently, there is a gap in the discussion of the effects of <b>numerical precision loss in twin experiments</b>;

  * this is particularly in regards to <b>bias in the numerical integration scheme</b> and its effect on <b>ensemble forecast</b> and <b>DA statistics</b>.

* In a <b>deterministic, biased-model</b> setting, the <b>numerical precision</b> the <b><span style="color:green">ensemble forecast</span></b> can be <b>substantially reduced</b> without a major deterioration of the DA cycle's (relative) predictive performance<sup><b>2</b></sup>.  

  * The <b>model bias overwhelms the errors</b> that are introduced <b>due to precision loss</b> when the <b><span style="color:green">model-twin</span> is resolved with a low order of accuracy</b>.

* However, <b>differences in statistical properties</b> of model forecasts of <b>stochastic dynamical systems</b> have been observed <b>due to the discretization errors</b> of certain low-order schemes.  

  * For example, Frank & Gottwald develop an <b>order 2.0 Taylor scheme</b> to <b>correct the bias</b> in the drift term <b>in the Euler-Maruyama scheme</b> in a stochastically reduced, multiscale model<sup><b>3</b></sup>. 

* We study how and to what extent the <b>bias of numerical integration schemes</b> in <b>random dynamical systems</b> also <b>biases twin experiment statistics</b>.


<div style="width:100%;float:left;font-size:30px">
<b>2.</b> Hatfield, S. et al.<em> Choosing the optimal numerical precision for data assimilation in the presence of model error</em>. Journal of Advances in Modeling Earth Systems, 10, 2177–2191, 2018.<br>
<b>3.</b> Frank, J. and Gottwald, G. A.<em> A Note on Statistical Consistency of Numerical Integrators for Multiscale Dynamics</em>. Multiscale Modeling &
Simulation, 16, 1017–1033, 2018.
</div>


========================================================
## Two Layer Lorenz-96 Model

 <div style="float:left; width:30%">
<img style="width:100%", src="two_layer_lorenz.png" alt="Image of two-layer Lorenz-96 model coupling between fast and slow layers."/>
<p style="text-align:center;font-size:30px">From: Wilks, D. <em>Effects of stochastic parametrizations in the Lorenz'96 system.</em> Quarterly Journal of the Royal Meteorological Society 131.606 (2005): 389-407. </p>
</div>

<div style="width:70%; float:left">
<ul>
  <li>The <b>two layer Lorenz-96</b> model simulates <b>coupled, ocean-atmosphere dynamics</b>.</li>
  <li> This is a common model to study <b>stochastic model reduction</b>;</li>
  <ul>
    <li>instead of simulating the <b>fast-variable dynamics</b>, their effects on the slow variables <b>are parameterized with a stochastic process</b>.</li>
  </ul>
  <li>This can be <b>justified mathematically</b> due to the <b>Central Limit Theorem</b>:</li>
  <ul>
    <li>in the <b>asymptotic separation of the time scales</b> for the fast and slow variables,</li>
    <li>the effect of the <b>fast variables</b> will <b>reduce to additive, Gaussian noise</b><sup><b>1</b></sup>.</li>
  </ul>
  <li>Outside of the asymptotic separation of scales, the <b>white-in-time model error</b> assumption is <b>no longer valid</b>; 
  <ul>
    <li>non-Markovian memory terms should be included.</li>
 </ul>
</ul>
</div>
<div style="width:100%;float:left;font-size:28px">
Vissio, G. and Lucarini, V.: A proof of concept for scale-adaptive parametrizations: the case of the Lorenz’96 model, Quarterly Journal of
the Royal Meteorological Society, 144, 63–75, 2018.<br>
<b>1.</b> Gottwald, G. et al. <em>Stochastic climate theory</em>. Nonlinear and Stochastic Climate Dynamics. 209--240. 2015. Cambridge University Press.<br>
Demaeyer, J. and Vannitsem, S.: Stochastic Parameterization of Subgrid-Scale Processes: A Review of Recent Physically Based Approaches,
in: Advances in Nonlinear Geosciences, pp. 55–85, Springer, 2018.
</div>

  
========================================================
## L96-s Model



<ul>

  <li>We define the <b>L96-s model</b> as follows,
  $$\begin{align}
\frac{\mathrm{d} \mathbf{x}}{\mathrm{d} t} \triangleq \mathbf{f}(\mathbf{x}) + s(t)\mathbf{I}_{n}\mathbf{W}(t),
\end{align}$$
  where</li>
  <ol>
    <li> $\mathbf{f}$ is defined as in the <b>single layer Lorenz-96</b> model</li>
    <li>$\mathbf{I}_n$ is the $n\times n$ identity matrix,</li>
    <li>$\mathbf{W}(t)$ is an $n$-dimensional Wiener process; and</li>
    <li>$s(t):\mathbb{R}\rightarrow \mathbb{R}$ is a measurable function of (possibly) time-varying diffusion coefficients.</li>
  </ol>
  <li><b>Both the <span style="color:blue">truth-twin</span> and <span style="color:green">model-twin</span> are simulated with the L96-s model</b>.</li>
  <ul>
    <li>This is the analogue to a <b>geophysical problem</b> where the <b>numerical model is unbiased</b> in <b>representing the true physics</b>, but where the <b>physics are intrinsically random</b>.</li>
  </ul>
  <li>This represents an <b>idealized two layer Lorenz-96 model</b> in which the <b>separation of the time scales</b> of the atmosphere and ocean <b>is taken to infinity</b>.</li>
  <ul>
    <li>This configuration can be understood as a <b>perfect-random model</b> assumption.</li>
  </ul>
  <li>We use this to <b>distinguish</b> the effects of <b>numerical bias</b> from <b>bias in the random physical process model</b>.</li>
  <li>This is also a common configuration for twin experiments in DA;</li>
  <ul>
    <li>we use this system to prototype an unbiased <b>perfect-random model benchmark.</b>
  </ul>
</ul>

========================================================
## <span style="color:#e7298a">Strong</span> versus <span style="color:#1b9e77">weak</span> convergence

<ul>
  <li>We study numerical integration schemes which <b>converge in the <span style="color:#e7298a">strong</span> sense</b>;</li>
  <ul>
    <li><b><span style="color:#e7298a">strong convergence</span></b> measures the <b><span style="color:#e7298a">expected path-discretization errors</span></b> over all possible Wiener processes <b>starting at an initial condition</b>.</li>
    <li>This is the <b><span style="color:#e7298a">analogue</span></b> of <b><span style="color:#e7298a">deterministic path-discretization errors</span></b>.</li>
  </ul>
  <li> If $\mathbf{x}_\mathrm{SP}$ is an <b>exact sample path</b>, evolving with respect to a particular Wiener process;</li>
  <li> and $\mathbf{x}$ is an <b>approximation of this path</b>, discretized at a maximum step size of $\Delta$;</li>
  <li>loosely, we say the approximate $\mathbf{x}$ <b><span style="color:#e7298a">converges strongly</span></b> to $\mathbf{x}_\mathrm{SP}$ at order $\gamma$ if:
  </li>
  <ul>
    <li>there exists a $\Delta_0$ and a constant $C>0$ such that for every $\Delta &lt; \Delta_0$
  </ul>
  <li>then the <b><span style="color:#e7298a">expected path-discretization error</span> is bounded</b> as
    $$\begin{align}
\mathbb{E}\left[\left\Vert \mathbf{x}(T) - \mathbf{x}_\mathrm{SP}(T)\right\Vert\right] \leq C \Delta^\gamma
\end{align}$$
where these are the states, evolved from time $0$ to time $T$.
</li>
</ul>

========================================================
## <span style="color:#e7298a">Strong</span> versus <span style="color:#1b9e77">weak</span> convergence -- continued

<ul>
<li><b><span style="color:#1b9e77">Weak convergence</span></b> measures the error in <b><span style="color:#1b9e77">representing some statistic</span></b> of the forward distribution, 
  <ul>
    <li> given the <b><span style="color:#1b9e77">evolution an initial point Dirac-delta</span></b> distribution over all possible realizations of the Wiener process.</li>
  </ul>
  <li>If $g$ is a $2(\gamma +1)$ continuously differentiable function of at most polynomial growth;</li>
  <ul>
    <li> we say that $\mathbf{x}$ <b><span style="color:#1b9e77">converges weakly</span></b> to $\mathbf{x}_\mathrm{SP}$ at order $\gamma$ if for all $\Delta< \Delta_0$, 
      $$\begin{align}
\left\Vert \mathbb{E}\left[ g(\mathbf{x}(T)) - g(\mathbf{x}_\mathrm{SP}(T))\right] \right\Vert \leq C \Delta^\gamma,
\end{align}$$
for any such statistic $g$.
    </li>
  </ul>
  <li>Loosely, <span style="color:#e7298a"><b>strong convergence</b></span> measures the <span style="color:#e7298a"><b>mean of the path-discretization errors</b></span>, while <span style="color:#1b9e77"><b>weak convergence</b></span> can measure the <span style="color:#1b9e77"><b>error in representing the mean</b></span> over all paths.</li>
</ul>

========================================================
## <span style="color:#e7298a">Strong</span> versus <span style="color:#1b9e77">weak</span> convergence in twin experiments

<ul>
  <li>Note: integration schemes that converge in the <span style="color:#e7298a"><b>strong</b></span> sense <b>also converge</b> in the <span style="color:#1b9e77"><b>weak</b></span> sense,</li>
  <ul>
    <li>however, <span style="color:#1b9e77"><b>weak</b></span> schemes <b>aren't guaranteed to converge</b> in the <span style="color:#e7298a"><b>strong</b></span> sense.</li>
  </ul>
  <li>For twin experiments, there is an <b>important distinction</b> between these modes of convergence:</li>
  <ul>
    <li>The <span style="color:blue"><b>truth-twin</b></span> should be generated by a simulation which is precise in the <span style="color:#e7298a"><b>strong</b></span> sense,</li>
    <ul>
      <li>here we assume we have <span style="color:blue"><b>observations of a path</b></span> that is <b>consistent</b> with the <b>governing dynamics</b> <sup><b>4</b></sup>.</li>
    </ul>
    <li>An <span style="color:green"><b>ensemble forecast</b></span> representation of the <span style="color:green"><b>prior</b></span> needs to converge in the <span style="color:#1b9e77"><b>weak</b></span> sense alone;</li>
    <li>indeed, the <span style="color:green"><b>forecast</b></span> represents the <span style="color:green"><b>sampling of the prior density</b></span>, and we do not need to ensure the precision of each path solution if the density is accurate.</li>
    <ul>
      <li>Therefore, the <span style="color:green"><b>model-twin</b></span> should be evaluated in terms of the precision in the <span style="color:#1b9e77"><b>weak</b></span> sense.</li>
    </ul>
  </ul>
</ul>

<div style="width:100%;float:left;font-size:30px">
<b>4.</b>Hansen, J. A. and Penland, C. <em>Efficient approximate techniques for integrating stochastic differential equations</em>. Monthly weather review. 134, 3006–3014, 2006.
</div>

========================================================
## Integration schemes

<ul>
  <li>We study three commonly used <b>numerical integration schemes</b> for <b>stochastic differential equations (SDEs)</b>:</li>
  <ol>
    <li><b>Euler-Maruyama</b> -- a simple extension of the deterministic Euler scheme, <b>order 1.0 strong convergence</b> in L96-s.</li>
    <li><b>4-stage Runge-Kutta</b> -- a simple extension of the determinstic 4-stage Runge-Kutta scheme<sup><b>5</b></sup>, <b>order 1.0 strong convergence</b> in L96-s</li>
    <li><b>Second order Taylor</b> -- an integration scheme based on the Taylor-Stratonovich expansion<sup><b>6</b></sup>, <b>order 2.0 strong convergence</b> in L96-s.</li>
  </ol>
  <li>The <b>derivation of the order 2.0 strong Taylor scheme</b> for the Lorenz-96 model is <b>nontrivial</b> and <b>has not appeared earlier</b> in the literature to the authors' knowledge.</li>
  <ul>
    <li>Because <b>L96-s model</b> has:</li>
    <ol>
      <li> <b>constant</b> or <b>vanishing second derivatives</b> in the deterministic component;</li>
      <li><b>periodic boundary conditions</b>; and</li> 
      <li><b>additive scalar noise</b>;</li> 
    </ol>
    <li>we can <b>compute</b> this scheme <b>efficiently</b>, with <b>complexity growing linearly</b> in the system dimension $n$.</li>
  </ul>
<ul>
<div style="width:100%; float:left; font-size:30px"/>
<b>5.</b> Rüemelin, W.<em> Numerical treatment of stochastic differential equations</em>, SIAM Journal on Numerical Analysis, 19, 604–613, 1982.
 <br>
<b>6.</b> Kloeden, P. and Platen, E. Numerical Solution of Stochastic Differential Equations, Stochastic Modelling and Applied Probability, Springer
Berlin Heidelberg, page 359. 2013.
</div>


========================================================
## <span style="color:#e7298a">Strong</span> convergence benchmarks

 <div style="float:left; width:50%">
<img style="width:100%", src="strong_convergence_5_pane.png" alt="Plot of strong convergence discretization error versus step size."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>We plot the <span style="color:#e7298a"><b>estimated strong convergence discretization error</b></span> in the vertical axis <b>versus the time-discretization step size</b> in log-log base 10 scale.</li>
  <li><b>Point estimates</b> are given by the <b>average estimated discretization error</b> over <b>500 independent batches of simulations</b>.</li>
  <ul>
    <li><b>Each batch</b> simulates the evolution of an initial condition with respect to <b>100 independent Wiener processes</b>.</li>
    <li>For <b>each Wiener process</b>, we simulate a <b>finely discretized path solution $\mathbf{x}_\mathrm{SP}$</b> with error on $\mathcal{O}\left(10^{-7}\right)$, and a <b>coarser approximation</b> by one of the tested methods.</li>
    <li>We <b>estimate</b> the quantity,
    $$\begin{align}
    \mathbb{E}\left[\left\Vert \mathbf{x}(T) - \mathbf{x}_\mathrm{SP}(T)\right\Vert\right]
    \end{align}$$
    as the <b>mean difference</b> of the <b>finely discretized solution</b> versus the <b>coarse discretization</b> over all Wiener processes in the batch.</li>
  </ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>It is known that these <b>batch-mean estimates</b> are realizations of <b>Gaussian random variables distributed around the true expectation</b> for sufficiently many samples of Wiener processes.</li>
  <li>Therefore, the <b>slope (order of convergence)</b> is estimated with <b>weighted least squares</b> with weights proportional to the inverse standard deviation of the batch realizations.</li>
</ul>
</div>

========================================================
## <span style="color:#e7298a">Strong</span> convergence benchmarks -- continued

 <div style="float:left; width:50%">
<img style="width:100%", src="strong_convergence_5_pane.png" alt="Plot of strong convergence discretization error versus step size."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>The parameter <b>$s$</b>, fixed for each panel, is the <b>diffusion level</b> in the L96-s model.</li>
  <li>We note that all the orders of convergence are empirically verified here.</li>
  <ul>
    <li>However, the <b>constant $C$</b> in the bound $C\Delta^\gamma$ has a <b>large impact</b> on the overall <b><span style="color:#e7298a">strong</span> discretization error</b>.</li>
  </ul>
  <li>In the <b>low diffusion regime</b>, the order <b>1.0 Runge-Kutta scheme</b> has an <b>overall discretization error comparable</b> to the order <b>2.0 Taylor scheme</b>.</li>
  <li>The performance of the <b>Runge-Kutta scheme varies significantly</b>, however, between <b>low and high diffusion</b>.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>While the <b>order of convergence remains the same</b> in all diffusion regimes, the <b>difference in performance is reflected in the constant $C$</b>.</li>
</ul>
</div>

========================================================
## <span style="color:#1b9e77">Weak</span> convergence

 <div style="float:left; width:50%">
<img style="width:100%", src="weak_convergence_5_pane.png" alt="Plot of weak convergence discretization error versus step size."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>


<div style="float:left; width:50%">
<ul>
  <li>The <b>effect of the constant</b> is even <b>more pronounced</b> in the <span style="color:#1b9e77"><b>weak</b></span> convergence metric.</li>
  <li>The <b>order 1.0 Runge-Kutta scheme outperforms the order 2.0 Taylor scheme in low diffusion</b>.</li>
  <li>The <b>overall <span style="color:#1b9e77">weak</span> discretization error varies on an order of magnitude</b> between <b>low</b> and <b>high</b> diffusion levels.</li
  </ul>
  <li><b>High precision</b> in the <b><span style="color:#e7298a">strong</span></b> sense across all diffusion regimes makes the <b>Taylor scheme</b> a natural choice for generating the <span style="color:blue"><b>truth-twin</b></span>.</li>
  <li>The <b>Runge-Kutta</b> scheme is appealing to generate the <span style="color:green"><b>ensemble forecast</b></span> of the <span style="color:green"><b>model-twin</b></span>, due to its accuracy in the <span style="color:#1b9e77"><b>weak</b></span> sense.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>However, because the <span style="color:#1b9e77"><b>weak</b></span> convergence of the <b>Runge-Kutta</b> scheme <b>varies by an order of magnitude</b> between diffusion levels, we use the <b>Taylor scheme</b> as a <b>benchmark</b> in the following experiments.</li>
  <li>We study how the <span style="color:green"><b>ensemble forecast statistics</b></span> of the <b>Euler-Maruyama</b> and the <b>Runge-Kutta</b> schemes <b>differ</b> from those generated by the <b>Taylor</b> scheme.</li>
</ul>
</div>

========================================================
## <span style="color:green">Ensemble forecast statistics</span> -- fine discretization

 <div style="float:left; width:45%">
<img style="width:100%", src="ensemble_stats_4_times_5_fine.png" alt="Plot ensemble forecast bias versus time."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>

<div style="float:left; width:55%;">
<ul>
  <li>We <b>generate 500 initial conditions</b> of the L96-s model and <span style="color:green"><b>forecast the initial condition</b></span> with <b>100 independent Wiener processes</b> to time plus 10 (horizontal axis).</li>
  <li>The <b>ensemble of evolved states</b> is then used to compute the <b>empirical, ensemble-estimated mean</b> and <b>ensemble-estimated spread</b> of the <span style="color:green"><b>forward distribution</b></span>.</li>
  <li>This is performed over each of the integration schemes:</li>
  <ol>
    <li><b>order 2.0 Taylor</b></li>
    <li><b>Euler-Maruyama</b></li>
    <li><b>4-stage Runge-Kutta</b></li>
  </ol>
  <li><b>Top panels:</b> we compute the <b>root-mean-square-deviation</b> of the <b>ensemble mean</b> of either the <b>Euler-Maruyama</b> or the <b>Runge-Kutta from</b> the <b>ensemble mean</b> of <b>Taylor</b>.</li>
  <li><b>Bottom panels:</b> we compute the <b>ratio of the ensemble spreads</b> of either the <b>Euler-Maruyama</b> or <b>Runge-Kutta</b> with that <b>Taylor</b>.</li>
  <li><b>Taylor scheme</b> uses a <b>step size of $\Delta=10^{-3}$</b> and the <b>same step size</b> is used for <b>Euler-Maruyama</b> and <b>Runge-Kutta</b>.</li>
</ul>
</div>


========================================================
## <span style="color:green">Ensemble forecast statistics</span> -- fine discretization continued

 <div style="float:left; width:45%">
<img style="width:100%", src="ensemble_stats_4_times_5_fine.png" alt="Plot of ensemble forecast bias versus time."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>

<div style="float:left; width:55%;">
<ul>
  <li>We plot the <b>summary statistics versus forecast time</b> over the 500 initial conditions, where the:</li>
  <ul>
    <li><b>median is plotted as a solid line</b>;</li>
    <li><b>inner 80 percentile is plotted shaded</b>;</li>
    <li><b>min/ max values are plotted in dashed</b>.</li>
  </ul>
  <li>The <span style="color:green"><b>ensemble statistics</b></span> of <b>Runge-Kutta</b> have <b>almost no difference</b> from <b>Taylor</b> for forecast times of <b>up to $T\approx 3$</b>.</li> 
  <li>There is <b>rapid divergence of the <span style="color:green">ensemble mean</span></b> and a <b>bias in the <span style="color:green">ensemble spread</span></b> of the <b>Euler-Maruyama</b>;</li>
  <li>the <b>median spread ratio</b> is <b>above 1.0</b> asymptotically.</li>
</ul>
</div>

========================================================
## <span style="color:green">Ensemble forecast statistics</span> -- coarse discretization

 <div style="float:left; width:45%">
<img style="width:100%", src="ensemble_stats_4_times_5_coarse.png" alt="Plot of ensemble forecast bias versus time."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>


<div style="float:left; width:55%;">
<ul>
  <li>We evaluate the <b>same plot except</b> where the <b>Rung-Kutta and Euler scheme use a step size of $\Delta=10^{-2}$</b> while the <b>benchmark Taylor uses a step size of $\Delta=10^{-3}$</b>.</li>
  <li>There is a <b>more rapid divergence of the ensemble means for both schemes</b>, as well as <b>differences induced in the ensemble spreads</b>.</li>
  <li>The <b>Euler-Maruyama scheme</b> has <b>extreme divergence of the ensemble means</b>, especially in the <b>low difussion</b>.</li>
  <li>The <b>ensemble spread is extremely biased for the Euler-Maruyama</b>,</li>
  <ul>
    <li>the <b>spread ratio has a miniumum value consistently above 1.0</b>.</li>
  </ul>
  <li><b>Runge-Kutta does not have extreme divergence of trajectories, and the spread remains unbiased asymptotically</b>.</li>
</ul>
</div>


========================================================
## Summary of bias in <span style="color:green">ensemble forecast</span>

* We confirm the <b>robustness</b> of <b>Runge-Kutta</b> in generating <span style="color:green; font-weight:bold">ensemble forecast statistics</span> in the L96-s model.

* Even for a <b>coarse time step of $\Delta=10^{-2}$</b>, <bRunge-Kutta</b> has <b>unbiased spread compared with Taylor using a step size of $\Delta=10^{-3}$</b>.
  
  * While <b>divergence of the Runge-Kutta trajectories from Taylor trajectories occurs earlier</b> with a <b>coarse time step</b>, 
  
  * <b>divergence of their ensemble means matches the asymptotic divergence</b> of the <b>finely resolved Runge-Kutta</b> using <b>time-step of $\Delta=10^{-3}$</b>.
  
* <b>Euler-Maruyama introduces systematic biases into <span style="color:green">ensemble forecast statistics</span></b>.

  * The <b><span style="color:green">asymptotic ensemble spread</span> is systematically, artifically larger</b>.
  
  * There is <b>extreme divergence of trajectories</b> causing the <b><span style="color:green">ensemble mean</span> to depart from the benchmark Taylor scheme</b>;
  
   * the divergence is <b>over an order of magnitude difference</b> compared with the Runge-Kutta scheme.

* This is concerning as <b>Euler-Maruyama is commonly used to simulate systems of SDEs for twin experiments</b>.

* This indicates the <b>biasing</b> of <span style="color:green; font-weight:bold;">ensemble forecast statistics</span>, 
  
  * however, this doesn't yet demonstrate the <b>effect of this bias on a filter twin experiment</b>.

  * This is demonstrated in the following experiements.


========================================================
## Taylor benchmark configuration -- <span style="color:red">filter statistics</span>

 <div style="float:left; width:50%">
<img style="width:100%", src="ty_fine_obs_fine_ens.png" alt="Plot of benchmark Taylor configuration filtering statistics."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>We plot the <b>twin-experiment RMSE</b> and <b>ensemble spread</b> for an <b>ensemble Kalman filter (EnKF)</b>;</li> 
  <li>both the <span style="color:blue; font-weight:bold">truth-twin</span> and <span style="color:green; font-weight:bold">model-twin</span> are <b>generated</b> with the <b>order 2.0 Taylor scheme</b>.</li> 
  <li><b>Both twins</b> use <b>step size $\Delta=10^{-3}$</b>.</li>
  <li><b>Vertical axis:</b> diffusion level $s$.</li>
  <li><b>Horizontal axis:</b> variance of the error in the observations given to the ensemble Kalman filter.</li>
  <li>We take <b>$N=10^2$ samples in the ensemble Kalman filter</b>, while the <b>state dimension is $n=10$</b>;</li>
  <li>this <b>guarantees convergence</b> of the <span style="color:red; font-weight:bold">filtering statistics</span> without additional techniques (inflation/ localization).</li>
  </ul>
</div>
<div style="float:left; width:100%;">
<ul>
  <li>The <b>RMSE</b> and <b>spread</b> are computed as the <b>asymptotic average over $2.5\times 10^{4}$ <span style="color:red">analysis cycles</span></b>.</li>
  <li><span style="color:red; font-weight:bold">Analysis RMSE</span> is <b>comparable</b> to the <span style="color:red; font-weight:bold">analysis spread</span>, and <b>lower</b> than the standard deviation of <b>the error in the observations</b>.</li>
  <ul>
    <li>This indicates that this represents the <span style="color:red; font-weight:bold">stable filter statistics</span>.</li>
  </ul>
  <li>We demonstrate the <b>effects of varying the <span style="color:green">model-twin integration scheme</span></b>.</li>
  <li>We <b>vary the method of <span style="color:green">ensemble integration</span></b> between <b>Runge-Kutta</b> and <b>Euler-Maruyama</b>, with a <b>step size between $\Delta\in\left\{10^{-3},10^{-2}\right\}$</b>.</li>
</ul>
</div>

========================================================
## <span style="color:red">Filter benchmark</span> -- <span style="color:green">Runge-Kutta model-twin, coarse discretization</span>, <span style="color:blue">Taylor truth-twin, fine discretization</span>

 <div style="float:left; width:50%">
<img style="width:100%", src="rk_fine_obs_coarse_ens.png" alt="Plot of coarse Runge-Kutta filter simulation versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>The difference between generating the <span style="color:green; font-weight:bold;">ensemble</span> with the <b>Runge-Kutta</b> with a <b>step size $\Delta= 10^{-3}$</b> and <b>benchmark Taylor is negligible</b>.</li>
  <ul>
    <li><b>Filtering statistics for these two configurations differ on the order of $10^{-6}$.</b></li>
  </ul>
  <li>Increasing the step size of <b>Runge-Kutta</b> to <b>$\Delta=10^{-2}$</b>, we introduce small errors,</li>
  <ul>
    <li>however, the <b>residuals are unstructured in sign or magnitude</b>.</li>
  </ul>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>The <b>mean of the differences in the RMSE is approximately $8\times 10^{-5}$</b> though with a <b>standard deviation of approximately $10^{-3}$ (on the order of the weak-discretization error)</b>.</li>
  <li>This indicates that the <b>observed differences in the filtering statistics</b> can be attributed to <b>random numerical errors, which are themselves unbiased</b>.</li>
</ul>
</div>

========================================================
## <span style="color:red">Filter benchmark</span> -- <span style="color:green">Euler-Maruyama model-twin, fine discretization</span>, <span style="color:blue">Taylor truth-twin, fine discretization</span>
 <div style="float:left; width:50%">
<img style="width:100%", src="em_fine_obs_fine_ens.png" alt="Plot of of coarse Runge-Kutta filter simulation versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>
<div style="float:left; width:50%">
<ul>
  <li>Generating the <span style="color:green; font-weight:bold">ensemble forecast</span> with <b>Euler-Maruyama</b> with <b>time step $\Delta=10^{-3}$</b>, we find <b>structure in the residuals</b>.</li>
  <li>In <b>low diffusion</b>, the <b><span style="color:red">RMSE</span> using Euler-Maruyama suffers from biases observed in the <span style="color:green">ensemble forecast</span></b>.</li>
  <li>The <b><span style="color:red">spread</span> suffers from the artificial inflation in the <span style="color:green;">forecast</span></b>.</li>
  <li>However, in <b>high diffusion</b>, the <b><span style="color:red">RMSE</span> and <span style="color:red">spread</span> of the ensemble are nearly identical</b> using <b>either Taylor</b> or <b>Euler-Maruyama</b>.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li><b>The level at which the bias impacts the twin experiment statistics depends strongly on the observation uncertainty, and most especially on the model uncertainty</b>.</li>
  <li>We demonstrate the <b>effect of increasing the step size of Euler-Maruyama to $\Delta=10^{-2}$ in <span style="color:green">generating the ensemble</span></b>.</li>
</ul>
</div>



========================================================
## <span style="color:red">Filter benchmark</span> -- <span style="color:green">Euler-Maruyama model-twin, coarse discretization</span>, <span style="color:blue">Taylor truth-twin, fine discretization</span>
 <div style="float:left; width:50%">
<img style="width:100%", src="em_fine_obs_coarse_ens.png" alt="Plot of coarse Euler-Maruyama filter simulation versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>
<div style="float:left; width:50%">
<ul>
  <li>The <b>structure of the residuals</b> remains largely the <b>same for the coarse discretization</b>, but the <b>magnitude changes</b> dramatically.</li>
  <li>In <b>low diffusion</b> the <span style="color:green; font-weight:bold">forecast discretization error</span> forces <span style="color:red; font-weight:bold">filter divergence</span>.</li>
  <li>In <b>high diffusion, $s\geq 0.5$</b>, the <b>difference of the <span style="color:red;">RMSE</span> with the benchmark Taylor is on the order of $10^{-2}$</b>.</li>
  </ul>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>We consistently see the <b>bias in the <span style="color:green">ensemble spread</span>, present once again</b>.</li> 
</ul>
</div>

========================================================
## <span style="color:red">Filter benchmark</span> -- <span style="color:green">Runge-Kutta model-twin, coarse discretization</span>, <span style="color:blue">Taylor truth-twin, coarse discretization</span>

 <div style="float:left; width:50%">
<img style="width:100%", src="rk_coarse_obs_coarse_ens.png" alt="Plot of of coarse Runge-Kutta filter simulation with coarse truth-twin versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. Geoscientific Model Development. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li> As an additional check, we <b>test the benchmark configuration versus</b>:</li>
  <ul>
    <li><b>Runge-Kutta with step size $\Delta=10^{-2}$ to generate the <span style="color:green">model-twin</span></b>; and</li>
    <li><b>Taylor with step size $\Delta = 5 \times 10^{-3}$ to generate the <span style="color:blue">truth-twin</span></b>.</li> 
  </ul>
  <li>This ensures that the <b>expected discretization error is less than $10^{-3}$ over all diffusion regimes</b>.</li>
  <li><b>Innacuracy in the <span style="color:blue">truth-twin</span> possibly adds structure in the residuals</b>,</li>
  <li>however, the results are <b>largely the same</b> as with the <b>accurate</b> <span style="color:blue; font-weight:bold">truth-twin</span>.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li><b><span style="color:blue">Increasing the step size</span> of the <span style="color:blue"> Taylor truth-twin</span></b> with the <span style="color:green; font-weight:bold">model-twin</span> generated by <span style="color:green; font-weight:bold">Euler-Maruyama</span> the results are <b>largely the same</b>.</li>
  <ul>
    <li>This <b>relaxes the issues with Euler-Maruyama</b> when the <b><span style="color:green">model-twin</span> uses a step size of <span style="color:green">$\Delta=10^{-3}$</span></b>.</li>
    <li>However, <b><span style="color:red">filter divergence</span> still occurs when the <span style="color:green">model-twin</span> uses a step size of <span style="color:green">$\Delta=10^{-2}$</span></b>.</li>
  </ul>
  <li>Our results suggest a <b>computationally efficient and statistically robust configuration for twin experiments using <span style="color:blue">Taylor</span> for the <span style="color:blue">truth-twin</span> and <span style="color:green">Runge-Kutta</span> for the <span style="color:green">model-twin</span></b>.</li>
</ul>
</div>


========================================================
## Conclusions

* Typically, <b>Lorenz-96</b> is simulated with a <b>4-stage Runge-Kutta</b> scheme with <b>step size up to $0.5$ in deterministic settings</b>.

  * We show that <b>the same standards cannot apply to twin experiments in the commonly used form of the L96-s</b>.
  
* We must <b>distinguish between <span style="color:#e7298a">strong</span> and <span style="color:#1b9e77">weak</span> convergence</b>, and its <b>impact</b> on the <span style="color:blue; font-weight:bold;">truth-twin</span> and the <span style="color:green; font-weight:bold;">model-twin</span> respectively.

* <b>Euler-Maruyama is a commonly used integration scheme for SDEs, but we find that it introduces strong, systematic bias into twin experiments when the step size is greater than or equal to $\Delta=10^{-2}$</b>.

  * Effects of the <b>bias depends strongly on the observation and especially model uncertainty</b> in a twin experiment;
  
  * however, the <b>bias is sufficient to cause filter divergence</b> in weak diffusion.
  
* We find that the <b>4-stage Runge-Kutta scheme is a statistically robust solver</b>, without the systematic biases encountered in the Euler-Maruyama scheme.

  * For <b>small step sizes</b> $\Delta$ on $\mathcal{O}\left(10^{-3}\right)$, we find <b>virtually no difference between the Runge-Kutta scheme and the higher order Taylor scheme</b>.
  
  * A <b>step size of $\Delta=10^{-2}$ introduces additional discretization error</b>, but the <b>error doesn't significantly influence the RMSE or spread of the EnKF</b>.
  
========================================================
## Conclusions -- continued

<ul>
  <li>Due to the computational constraints in running twin experiments, <b>a step size of $\Delta=10^{-3}$ is often unreasonable for generating the <span style="color:blue">truth-twin</span> or <span style="color:green">model-twin</span></b>.</li>
  <li> A step size on $\mathcal{O}\left(10^{-2}\right)$ is what can be afforded in a <b>typical benchmark study</b>.</li>
  <li> This <b>excludes the use of Euler-Maruyama from statistically robust, perfect-random twin experiments entirely</b>.</li>
  <li>We demonstrate in our work that an <b>overall discretization error can be bounded by $10^{-3}$</b>, using:</li>
  <ol>
    <li><b><span style="color:green">4-stage Runge-Kutta with step size $\Delta=10^{-2}$ to generate the model-twin</span></b>; and</li>
    <li><b><span style="color:blue"> order 2.0 Taylor with step size $\Delta=5\times 10^{-3}$ to generate the truth-twin</span></b>.</li>
  </ol>  
  <li>This forms a practical compromise, which <b>our diagnostics demonstrate does not bias the outcomes of the <span style="color:red">filtering statistics</span></b>.</li>
  <li>We provide a <b>computationally efficient framework for statistically robust twin experiments in the L96-s model</b>.</li>
  <li><b>We provide a novel derivation of ther order 2.0 Taylor scheme for the L96-s model</b>.</li>
  <ul>
    <li>This <b>derivation has not previously appeared in the literature</b> to the authors' knowledge, and we moreover <b>provide benchmarks on the convergence of this and other schemes</b>.</li>
  </ul>
  <li> As an <b>open question:</b></li>
  <ul>
    <li><strong>Can using weak integration schemes (which may not converge to any sample path) reduce the computational burden of ensemble-based forecasts in geophysical models?</strong></li>
  </ul>
  <li><b>If the goal of the forecast is to converge in distribution alone, this may be a viable alternative to traditional geophysical modeling paradigms</b>.</li>
</ul>

