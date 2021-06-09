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

A fast, single-iteration ensemble Kalman smoother for online, sequential data assimilation
========================================================
autosize: true
incremental: true
width: 1920
height: 1080

## Authors:

<div style="text-align:center">
<p><strong>Colin Grudzien<sup>1</sup>, Marc Bocquet<sup>2</sup></strong></p>
<h3>Special Thanks:</h3>
<p>Eric Olson<sup>1</sup> & Mihye Ahn<sup>1</sup> for HPC logistics and support</p>
<ol style="font-size:30px;text-align: center;list-style-position: inside;">
  <li>University of Nevada, Reno, Department of Mathematics and Statistics</li>
  <li>CEREA, A joint laboratory &Eacute;cole des Ponts Paris Tech and EDF R&D, Universit&eacute; Paris-Est, Champs-sur-Marne, France.</li>
</ol>
</div>

<div style="text-align:center">

</div>
<div style="float:left; width:33%">
<img style="width:70%", src="UNR_logo.png" alt="University of Nevada, Reno logo."/>
</div>
<div style="float:right; width:33%; text-align:right;padding-top:88.575px">
<img style="width:70%;", src="cerea_logo.png" alt="CEREA logo."/>
</div>

========================================================


<h2>Outline</h2>
  * Motivation
  * A review of the ensemble transform Kalman filter (ETKF) in perfect, hidden Markov models
  * Fixed-lag smoothing
  * The classic ensemble transform Kalman smoother (ETKS)
  * The 4D smoothing cost function
    * Iterative analysis and the iterative ensemble Kalman smoother (IEnKS)
  * An alternative formulation of iterative smoothing for weakly nonlinear forecast error dynamics:
    * The single-iteration ensemble transform Kalman smoother (SIETKS)
  * Numerical simulations
    * Optimizing hyper-parameters: adaptive inflation
    * Nonlinear observation operators with SDA / MDA
    * Varying lag / shift sizes with SDA / MDA

========================================================
## Motivation

* <b>Iterative, ensemble-variational</b> methods form the basis for the <strong>state-of-the-art for
nonlinear, scalable data assimilation (DA)</strong><sup><b>1</b></sup>

  * Methods following an <strong>ensemble Kalman filter (EnKF) style analysis</strong> 
  include the <b>ensemble randomized maximum likelihood method (EnRML)</b><sup><b>2</b></sup>
  and the <b>iterative ensemble Kalman smoother (IEnKS)</b><sup><b>3</b></sup>

<ul>
  <li>These iterative, ensemble-variational methods combine the benefits of:</li>
  <ol>
    <li>the <strong>high-accuracy</strong> of the iterative solution of the <b>Bayesian maximum a posteriori (MAP)</b> solution to the DA problem;</li>
    <li>the relative <strong>simplicity of numerical model development and maintenance</strong> in <b>ensemble-based DA</b>;</li>
    <li>the <b>ensemble-based analysis</b> of <strong>time-dependent errors</strong> and possibly <strong>discontinuous, physical model parameters</strong>; and</li>
    <li>the <b>variational analysis</b>, <strong>optimizing hyper-parameters</strong> for, e.g., inflation<sup><b>4</b></sup>, localization<sup><b>5</b></sup> and surrogate models<sup><b>6</b></sup> to augment the estimation scheme.
  </ol>  
</ul>

<div style="width:100%;float:left;font-size:30px">
<b>1.</b> Bannister, R. (2017). <i>A review of operational methods of variational and ensemble‐variational data assimilation</i>. Quarterly Journal of the Royal Meteorological Society, 143(703), 607-633.</br>
<b>2.</b> Chen, Y., & Oliver, D. (2012). <i>Ensemble randomized maximum likelihood method as an iterative ensemble smoother</i>. Mathematical Geosciences, 44(1), 1-26.</br>
<b>3.</b> Bocquet, M., & Sakov, P. (2014). <i>An iterative ensemble Kalman smoother</i>. Quarterly Journal of the Royal Meteorological Society, 140(682), 1521-1535.</br>
<b>4.</b> Bocquet, M., Raanes, P., & Hannart, A. (2015). <i>Expanding the validity of the ensemble Kalman filter without the intrinsic need for inflation</i>. Nonlinear Processes in Geophysics, 22(6), 645-662.<br>
<b>5.</b> Lorenc, A. C. (2003). <i>The potential of the ensemble Kalman filter for NWP—A comparison with 4D‐Var</i>. Quarterly Journal of the Royal Meteorological Society: A journal of the atmospheric sciences, applied meteorology and physical oceanography, 129(595), 3183-3203.<br>
<b>6.</b> Bocquet, M., Brajard, J., Carrassi, A., & Bertino, L. (2020). <i>Bayesian inference of chaotic dynamics by merging data assimilation, machine learning and expectation-maximization</i>.Foundations of Data Science,  2(1): 55-80 (2020).
</div>


========================================================
### Motivation

* However, a barrier to the use of <b>iterative, ensemble-variational</b> schemes in <b>online, sequential DA</b> still lies in the <strong>computational bottleneck of ensemble simulation in the nonlinear, physics-based model</strong>. 

* Many iterative smoothing procedures require <strong>multiple runs of the ensemble simulations</strong> to produce the <b style="color:#1b9e77">forecast</b>, <b style="color:#7570b3">filtering</b> and re-analyzed <b style="color:#d95f02">smoothing</b> statistics. 

* For <strong>online applications</strong> in which there is a <strong>short operational time-window</strong> to produce a forecast for future states, the <b>iterative ensemble simulations may be prohibitively expensive</b>.

* Particularly in case where nonlinearity in the DA cycle is <strong>not dominated by the forecast error dynamics</strong>,

  * i.e., if the <strong>tangent-linear evolution</strong> of <strong>Gaussian error distributions</strong> is an <b>adequate approximation</b>,
  
* the cost of an <strong>iterative, ensemble simulation</strong> <b>may not be justified</b> by the improvement in forecast accuracy.

* For short-range forecasting, nonlinearity in the DA cycle may instead by dominated by: 
  
  * nonlinearity in the observation operator, 
  * nonlinearity in hyper-parameter optimization, and / or 
  * nonlinearity in temporally interpolating a re-analyzed solution over the lagged states.

* For sequential forecast cycles in which the <strong>linear-Gaussian approximation</strong> of the forecast error may be appropriate, like <b>synoptic meteorology</b>, 

  * a different form of iterative, ensemble-variational smoother may have substantial advantages in a <strong>computational cost / forecast accuracy tradeoff</strong>.

========================================================
### Motivation

* We consider a simple <strong>hybridization</strong> of the <b>classic ensemble transform Kalman smoother (ETKS)</b> with the <b>iterative ensemble Kalman smoother (IEnKS)</b> to produce a <strong>single-iteration, fixed-lag, sequential smoother</strong>. 

* We combine:
  <ol>
    <li>the <b>filtering solution and retrospective analysis</b> as in the classic EnKS; and</li>
    <li>a <b>single iteration of the ensemble simulation</b> over the lagged states with the re-analyzed prior;</li>
  </ol>
  
* to <strong>improve the EnKF filter and forecast statistics</strong> in the subsequent DA cycle.

* The resulting scheme is a <b>"single-iteration"</b>, ensemble Kalman smoother that <strong>sequentially solves the
filtering, Bayesian MAP cost-function</strong>;

  * the scheme produces the <b style="color:#1b9e77">forecast</b>, <b style="color:#7570b3">filtering</b> and re-analyzed <b style="color:#d95f02">smoothing</b> statistics within a <strong>single iteration of the ensemble simulation of the lagged states</strong>.

* This scheme seeks to <strong>minimize the leading order cost of ensemble-variational smoothing</strong>, i.e., the <b>ensemble simulation in the nonlinear forecast model</b>.

  * However, we are free to <strong>iteratively solve the filtering cost function</strong> for any single observation <b>without iterations of the ensemble simulation</b>. 

* This is an <strong>outer-loop optimization of the cost of fixed-lag, sequential smoothing</strong>, designed for <b>online applications with weakly nonlinear forecast error evolution</b>.

* We will denote the general framework as a <b>"single-iteration" smoother</b>, while the specific implementation presented here is denoted the <b>single-iteration ensemble transform Kalman smoother (SIETKS)</b>.


========================================================
### Motivation

* For <strong>linear-Gaussian systems with the perfect model hypothesis</strong>, the SIETKS is a <b>fully consistent Bayesian estimator</b>, albeit one that uses redundant model simulations. 

* When the <strong>forecast error dynamics are weakly nonlinear</strong>, yet <b>other aspects of the DA cycle are strongly nonlinear</b>,
  
  * e.g., the <strong>filtering cost function is nonlinear</strong> due to <b>hyper-parameters</b> or a <b>nonlinear observation operator</b>,

* we demonstrate the <b>SIETKS has predictive performance comparable with fully iterative methods</b>.

  * However, the SIETKS has a <strong>numerical cost that scales with matrix inversions in the ensemble dimension</strong>, rather than the cost of the ensemble simulation.

* We furthermore derive a method of <b>multiple data assimilation (MDA)</b> for this hybrid smoother scheme;
  
  * the MDA scheme <strong>handles the increasing nonlinearity</strong> of the temporal interpolation of the posterior over <b>long lag windows or large shifts of the smoothing solution</b>.

* The result is a <b>two-stage MDA algorithm</b>, estimating the <b style="color:#1b9e77">forecast</b>, <b style="color:#7570b3">filtering</b> and re-analyzed <b style="color:#d95f02">smoothing</b>, and shifting the smoother forward in time with two sweeps of the lagged states with an ensemble simulation.


* Stage:
  1. <strong>samples the posterior density</strong>, balancing the MDA weights to produce the ensemble estimates;
  2. <strong>shifts the window of lagged states</strong>, updating the MDA weights for the shifted window.

========================================================

## Perfect hidden Markov models

<ul>
  <li>We use the <b>perfect model assumption</b>; <strong>generalizing the techniques for the presence of model errors is ongoing work</strong>.</li>
  <li> Define a <b style="color:#1b9e77">perfect physical process model</b> and <b style="color:#7570b3">observation model</b>, 
  $$\begin{align}
  \pmb{x}_k &= \mathcal{M}_{k} \left(\pmb{x}_{k-1}\right)  & & \pmb{x}_k\in\mathbb{R}^{N_x}\\
  \pmb{y}_k &= \mathcal{H}_k \left(\pmb{x}_k\right) + \boldsymbol{\epsilon}_k & & \pmb{y}_k\in\mathbb{R}^{N_y}
  \end{align}$$</li>
  <li>Let us denote the sequence of the <b style="color:#1b9e77">process model states</b> and <b style="color:#7570b3">observation model states</b> as,
  $$\begin{align}
\pmb{x}_{m:k} &:= \left\{\pmb{x}_m, \pmb{x}_{m+1}, \cdots, \pmb{x}_k\right\}, \\
\pmb{y}_{m:k} &:= \left\{\pmb{y}_m, \pmb{y}_{m+1}, \cdots, \pmb{x}_k\right\}. 
\end{align}$$</li>
  <li>We <b>assume</b> that the sequence of <b style="color:#7570b3">observation error</b> vectors
    $$\begin{align}
    \{\boldsymbol{\epsilon}_k :  k=1,\cdots, L\}
    \end{align}$$
    is <strong>independent in time</strong>.</li> 
  <li>  In the above configuration, we will say that the <b>transition "density"</b> is given in terms of
  $$\begin{align}
  p(\pmb{x}_k \vert \pmb{x}_{k-1}  ) \propto \pmb{\delta} \left\{\pmb{x}_k - \mathcal{M}_k\left(\pmb{x}_{k-1}\right)\right\}\label{eq:dirac_distribution}
  \end{align}$$
where $\pmb{\delta}$ represents the <b>Dirac distribution</b>.</li>
  <li>The filtering problem is to sequentially and recursively estimate,
  $$\begin{align}
  p(\pmb{x}_L \vert \pmb{y}_{L:1})
  \end{align}$$
  or some statistic of this density, given:</li>
  <ul>
    <li>an initial prior $p(\pmb{x}_0)$; and </li>
    <li>the observation likelihoods $p(\pmb{y}_k \vert \pmb{x}_k )$.</li>
  </ul>
    <li>This can be described as an <b style="color:#7570b3">observation</b>-<b style="color:#d95f02">analysis</b>-<b style="color:#1b9e77">forecast</b> cycle.</li>
</ul>

========================================================
### The <b style="color:#7570b3">observation</b>-<b style="color:#d95f02">analysis</b>-<b style="color:#1b9e77">forecast</b> cycle

 <div style="float:left; width:60%">
<img style="width:100%", src="forecast_cycle_diagram_009.svg" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:right; width:40%">
<ul>
  <li>Using Bayes' law, this can be written as
$$\begin{align}
  {\color{#d95f02} {p\left(\pmb{x}_{L} \vert \pmb{y}_{L:1}\right)} } &\propto {\color{#7570b3} { p\left(\pmb{y}_L \vert \pmb{x}_L\right) } } {\color{#1b9e77} { p\left(\pmb{x}_L\vert   \pmb{y}_{1:L-1}\right) } } 
  \end{align}$$</li>
  <li>When the models are linear, i.e.,
  $$\begin{align}
  \pmb{x}_k &= \mathbf{M}_k \pmb{x}_{k-1};\\
  \pmb{y}_k &= \mathbf{H}_k \pmb{x}_k + \pmb{\epsilon}_k;
  \end{align}$$</li>
  <li>and the error densities are Gaussian, i.e.,
  $$\begin{align}
  p(\pmb{x}_0) &= N\left(\overline{\pmb{x}}_0, \mathbf{B}_0\right);\\
  p\left(\pmb{y}_k \vert \pmb{x}_k \right) &= N\left(\mathbf{H}_k\pmb{x}_k, \mathbf{R}_k\right);
  \end{align}$$</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>the posterior filtering density is Gaussian at all times,
  $${\color{#d95f02} {p\left(\pmb{x}_{L} \vert \pmb{y}_{L:1}\right)\equiv N\left(\overline{\pmb{x}}^\mathrm{filt}_k, \mathbf{B}_k^\mathrm{filt}\right)}}$$ 
  and can be computed analytically in a recursive formulation by the <b>Kalman filter</b>.</li>
  <li>The <b>ensemble Kalman filter (EnKF)</b> uses an empirical, ensemble-based forecast mean and covariance, along with the parametric update of the Kalman filter, to <b style="color:#d95f02">approximate the Bayesian posterior</b>.</li>
  <li>Many different techniques have been developed to efficiently re-sample an ensemble from the posterior, using the above approximation.</li>
</ul>
</div>

========================================================

## The ETKF

* We will consider the <b>right ensemble transform</b> version.

* Specifically, with Gaussian error densities,
  
  $$\begin{align}
  p(\pmb{x}_L\vert \pmb{y}_{1:L-1}) = N\left(\overline{\pmb{x}}_L^\mathrm{fore}, \mathbf{B}_L^\mathrm{fore}\right) & & p\left(\pmb{y}_L \vert \pmb{x}_L \right) = N\left(\mathbf{H}_L \pmb{x}^\mathrm{fore}_L, \mathbf{R}_L\right)
  \end{align}$$
  this can be written as a <strong>least-squares optimization</strong> as follows.

* Suppose that a <b style="color:#1b9e77">forecast ensemble</b> $\mathbf{E}_{L}^\mathrm{fore}\in \mathbb{R}^{N_x \times N_e}$ is drawn iid from $p(\pmb{x}_L\vert \pmb{y}_{1:L-1})$.

* Define the ensemble-based, empirical estimates,
  
  $$\begin{align}
  & & \hat{\pmb{x}}_L^\mathrm{fore} &:= \mathbf{E}_L^\mathrm{fore} \pmb{1} / N_e ; & 
  \hat{\pmb{\delta}}_L &:= \mathbf{R}_k^{-\frac{1}{2}}\left(\pmb{y}_L - \mathbf{H}_L \hat{\pmb{x}}_L\right)\\
  &&\mathbf{X}_L^\mathrm{fore} &:= \mathbf{E}_L^\mathrm{fore} - \hat{\pmb{x}}^\mathrm{fore}_L \pmb{1}^\top ; & 
  \mathbf{P}^\mathrm{fore}_L &:= \mathbf{X}_L^\mathrm{fore} \left(\mathbf{X}_L^\mathrm{fore}\right)^\top / \left(N_e - 1\right);\\
  & &\mathbf{S}_L &:=\mathbf{R}_L^{-\frac{1}{2}}\mathbf{H}_L \mathbf{X}_L^\mathrm{fore};  & \pmb{x}&:= 
  \hat{\pmb{x}}_L^\mathrm{fore} + \mathbf{X}^\mathrm{fore}_L \pmb{w} .
  \end{align}$$

* Maximizing the empirical posterior density is equivalent to <strong>minimizing the cost function</strong> $\mathcal{J}(\pmb{x}) \equiv \widetilde{\mathcal{J}}(\pmb{w})$,
  
  $$\begin{alignat}{2}
  & & {\color{#d95f02} {\widetilde{\mathcal{J}} (\pmb{w})} } &= {\color{#1b9e77} {\frac{1}{2} \parallel \hat{\pmb{x}}_L^\mathrm{fore} - \mathbf{X}^\mathrm{fore}_L \pmb{w}- \hat{\pmb{x}}^\mathrm{fore}_L \parallel_{\mathbf{P}^\mathrm{fore}_L}^2} } + {\color{#7570b3} {\frac{1}{2} \parallel \pmb{y}_L - \mathbf{H}_L\hat{\pmb{x}}^\mathrm{fore}_L - \mathbf{H}_L \mathbf{X}^\mathrm{fore}_L \pmb{w} \parallel_{\mathbf{R}_L}^2 } }\\
  \Leftrightarrow& & {\color{#d95f02} {\widetilde{\mathcal{J}}(\pmb{w})} } &= {\color{#1b9e77} {\frac{1}{2}(N_e - 1) \parallel\pmb{w}\parallel^2} } + {\color{#7570b3} {\frac{1}{2}\parallel \hat{\pmb{\delta}}_L - \mathbf{S}_L \pmb{w}\parallel^2 } }
  \end{alignat}$$
  which is an <b>optimization over a weight vector $\pmb{w}$ in the ensemble dimension $N_e \ll N_x$</b>.

========================================================

### The ETKF

<div style="float:left; width:100%">
<ul>
  <li>Setting the <b>gradient</b> $\nabla_{\pmb{w}} \widetilde{\mathcal{J}}$ equal to zero for $\overline{\pmb{w}}$ we find
  $$\begin{align}
  \overline{\pmb{w}} = \pmb{0} - {\widetilde{\mathbf{H}}_{\widetilde{\mathcal{J}}}}^{-1} \nabla_{\pmb{w}} \widetilde{\mathcal{J}}.
  \end{align}$$
  where $\widetilde{\mathbf{H}}_{\widetilde{\mathcal{J}}}:= \nabla^2_{\pmb{w}} \widetilde{\mathcal{J}}$ is the <b>Hessian of the cost function</b>.</li>
  <li> This corresponds to a single iteration of <b>Newton's descent algorithm</b>, yielding
  $$\overline{\pmb{x}}_L^\mathrm{filt} := \overline{\pmb{x}}_{L}^\mathrm{fore}  + \mathbf{X}_L^\mathrm{fore} \overline{\pmb{w}}.$$</li>
  <li>If we define a right-transform matrix,
  $$\begin{align}
  \mathbf{T}:= \widetilde{\mathbf{H}}_{\widetilde{\mathcal{J}}}^{-\frac{1}{2}},
  \end{align}$$</li>
  
  <li>we similarly have the update for the covariance as
  $$\begin{align}
  \mathbf{P}^\mathrm{filt}_L = \left(\mathbf{X}_L^\mathrm{fore} \mathbf{T} \right)\left(\mathbf{X}_L^\mathrm{fore} \mathbf{T} \right)^\top /(N_e - 1).
  \end{align}$$</li>
  <li> The <b>numerical cost</b> of the Newton step and the transform $\mathbf{T}$ are <strong>subordinate to the cost of the eigen value decomposition</strong> of $\mathbf{H}_{\mathcal{J}} \in \mathbb{R}^{N_e \times N_e}$.</li>
  <li> This sketches the right <b>ensemble transform Kalman filter</b> recursion as in the derivation of the <b>local ensemble transform Kalman filter (LETKF).</b><sup><b>7</b></sup></li>
</ul>
</div>
<div style="width:100%;float:left;font-size:30px">
<b>7.</b> Hunt, B.R., Kostelich, E.J., & Szunyogh, I. (2007). <i>Efficient data assimilation for spatiotemporal chaos: A local ensemble transform Kalman filter</i>. Physica D: Nonlinear Phenomena, 230(1-2), 112-126.
</div>


========================================================
## <span style="color:#d95f02">Smoothing</span>

 <div style="float:left; width:60%">
<img style="width:100%", src="smoothing_diagram.svg" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:right; width:40%">
<ul>
  <li>This recursively estimates the density of the <b>current state</b>, but a related question regards the <strong>past states</strong>.</li>
  <li>E.g., the observation at time $t_3$ can be used to <b>update the conditional estimate</b> for the model state at times $t_0$, $t_1$ and $t_2$.</li>
  <li>This produces a <span style="color:#d95f02;font-weight:bold">smoothing posterior estimate</span> for the past states.</li>
  <li>The smoothing estimate conditions all past states within the <b>data assimilation window (DAW)</b>, i.e., over the <strong>time series of all lagged states</strong>.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>A smoothing estimate may be produced in a variety of ways, exploiting different formulations of the <b>Bayesian inference problem</b> as a <strong>joint or marginal smoother</strong>.<sup><b>8</b></sup></li>
  <li>The implementation also depends on whether the <b>DAW</b> is <strong>fixed in time, or if this window is shifted in time sequentially</strong>.</li>
  <ul>
    <li>For online,  <b style="color:#7570b3">observation</b>-<b style="color:#d95f02">analysis</b>-<b style="color:#1b9e77">forecast</b> cycles, we will sequentially shift the DAW.</li>
  </ul>
</ul>
</div>


<div style="width:100%;float:left;font-size:30px">
<b>8.</b> Cosme, E., Verron, J., Brasseur, P., Blum, J., & Auroux, D. (2012). <i>Smoothing problems in a Bayesian framework and their linear Gaussian solutions</i>. Monthly Weather Review, 140(2), 683-695.
</div>



========================================================
### <span style="color:#d95f02">Sequential Smoothing</span>

 <div style="float:left; width:100%; text-align:center;">
<img style="width:70%", src="cycling.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:left; width:100%">
<ul>
  <li>In the above, we see a schematic of how the <strong>DAW is sequentially shifted in time</strong> for a <b>general fixed-lag smoother</b>.</li>
  <li>Generally, we will consider a <b>DAW of a lag length</b> $L \times \Delta t$, with a sequential <strong>shift of length</strong> $S\times \Delta t$.</li>
  <li>After the conditional estimate is formed, we will shift the DAW by $S \times \Delta t$;</li>
  <ul>
    <li>this will discard $S \times \Delta t$ past states from the DAW, and $S \times \Delta t$ new states and observations will enter the DAW.</li>
  </ul>
  <li>In the figure above, the $S \times \Delta t$ new states and observations that enter the DAW are filled in black.</li>
  <li>The above fixed-lag formalism allows us to <strong>treat the smoothing problem</strong> <b>like sequential filtering</b>.</li>
  <li>This can come with large benefits to the <b>precision of estimation</b> by <strong>utilizing a full time series to form conditional estimates</strong>;
  <ul>
    <li>however, it can also become <strong>extremely costly to produce conditional estimates</strong> this way when <b>$S$ is small and $L$</b> is large.</li>
  </ul>
</ul>
</div>



========================================================

## The ETKS



* In the ETKF formalism, we can define an <b>ensemble right-transform</b> $\boldsymbol{\Psi}_k$ such that for any $t_k$,

 $$\begin{align}
 \mathbf{E}^\mathrm{filt}_k = \mathbf{E}^\mathrm{fore}_k \boldsymbol{\Psi}_k
 \end{align}$$
  where we say that the columns of the matrices are distributed iid as
  $$\begin{align}
  \mathbf{E}^\mathrm{filt}_k &\sim p(\pmb{x}_k \vert \pmb{y}_{1:k}) \\
  \mathbf{E}^\mathrm{fore}_k &\sim p(\pmb{x}_k \vert \pmb{y}_{1:k-1})
  \end{align}$$

* We will associate $\mathbf{E}^\mathrm{filt}_k \equiv \mathbf{E}^\mathrm{post}_{k|k}$, where we define
  
  $$\begin{align}
  \mathbf{E}^\mathrm{post}_{k \vert K} \sim p(\pmb{x}_k \vert \pmb{y}_{1:K})
  \end{align}$$
  for $K>k$.


  * Under the <strong>linear-Gaussian model</strong>, we furthermore have that

  $$\begin{align}
  \mathbf{E}^\mathrm{post}_{k |L} = \mathbf{E}^\mathrm{post}_{k|L-1}\boldsymbol{\Psi}_{L}.
  \end{align}$$

* A <b style="color:#d95f02">retrospective smoothing analysis</b> can be performed on all past states stored in memory by <strong>using the latest right-transform update from the filtering step</strong>.

* This form of <b style="color:#d95f02">retrospective analysis</b> is the basis of the classic <b>ensemble Kalman smoother (EnKS).<sup><b>9</b></sup></b>

<div style="width:100%;float:left;font-size:30px">
<b>9.</b> Evensen, G., & Van Leeuwen, P. J. (2000). <i>An ensemble Kalman smoother for nonlinear dynamics. Monthly Weather Review, 128(6), 1852-1867.</i>
</div>


========================================================

### The ETKS

<div style="float:left; width:100%">
<ul>
  <li>The <b>ensemble transform Kalman smoother (ETKS)</b> takes advantage of the simple form of the <b style="color:#d95f02">retrospective, right-transform analysis</b> by including an <strong>additional, inner loop of the filtering cycle</strong>.</li>
</ul>
</div>
<div style="float:left; width:100%; text-align:center;" class="fragment">
<img style="width:60%", src="enks_scheme.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
</div>
<div style="float:left; width:100%">
<ul>
    <li>In the above, time is the horizontal axis where right moves forward in time.</li>
    <li>At each time, we produce the standard <b style="color:#d95f02">filtering estimate</b> by computing $\boldsymbol{\Psi}_L$ from the cost function, and updating the <b style="color:#1b9e77">forecast</b> 
    $$\mathbf{E}^\mathrm{filt}_L = \mathbf{E}_L^\mathrm{fore} \boldsymbol{\Psi}_L.$$</li> 
    <li>The <b style="color:#7570b3">information from incoming observations</b> is <strong>passed backward in time using the right-transform</strong> to condition the ensemble at past times:
    $$\begin{align}
    \mathbf{E}^\mathrm{post}_{k|L} = \mathbf{E}^\mathrm{post}_{k|L-1} \boldsymbol{\Psi}_L.
    \end{align}$$
</ul>
</div>

========================================================

### The ETKS

* The <b style="color:#7570b3">information</b> in the posterior estimate thus <strong>flows in reverse time to the lagged states</strong> stored in memory, but the <b>information flow is unidirectional</b> in this scheme.  

* The <b style="color:#d95f02">improved posterior estimate</b> for the lagged states <strong>does not improve the filtering estimate</strong> in the <b>perfect, linear-Gaussian model</b>:
  
  $$\begin{align}
  \mathbf{M}_{k} \mathbf{E}_{k-1|L}^\mathrm{post}& = \mathbf{M}_{k} \mathbf{E}_{k-1|k-1}^\mathrm{post}    
  \prod_{j=k}^{L} \boldsymbol{\Psi}_j \\
  & =\mathbf{E}_{k|k}^\mathrm{post}\prod_{j=k+1}^L \boldsymbol{\Psi}_j\\
  & = \mathbf{E}_{k|L}^\mathrm{post}.
  \end{align}$$
  
* This demonstrates that the effect of the  <b style="color:#d95f02">conditioning on the information</b> from the observation is <strong>covariant with the dynamics</strong>.  

* In fact, in the case of the <b>perfect, linear-Gaussian model</b>, the  <b style="color:#d95f02">backward-in-time conditioning</b> is <strong>equivalent to the reverse time model forecast</strong> $\mathbf{M}_k^{-1}$, as demonstrated by <b>Rauch, Tung and Striebel (RTS)</b>.<sup><b>10</b></sup>

<div style="width:100%;float:left;font-size:30px">
<b>10.</b> Jazwinski, A. H. (2007). <i>Stochastic processes and filtering theory</i>. Courier Corporation.  See example 7.8, chapter 7.
</div>

========================================================

## The 4D cost function

<div style="float:left; width:100%">
<ul>
  <li>The <b style="color:#d95f02">conditioning is not covariant</b> with the model dynamics <b style="color:#1b9e77">model dynamics</b> in the presence of <strong>nonlinearity or model error</strong>.</li>
  <li> Re-initializing the DA cycle in a perfect, nonlinear model with the <b style="color:#d95f02">smoothed conditional ensemble estimate</b> $\mathbf{E}^\mathrm{post}_{0|L}$ can <strong>dramatically improve the performance of the subsequent forecast and filtering statistics</strong>.</li>
  <li> Let us denote the <b style="color:#1b9e77">composition of the model forecast</b> as,
  $$\begin{align}
  \mathcal{M}_{k:m} : = \mathcal{M}_k \circ \cdots \circ \mathcal{M}_{m} & & \mathbf{M}_{k:m} := \mathbf{M}_{k}\cdots \mathbf{M}_{m}
  \end{align}$$</li>
  <li> Particularly, this <b>exploits the miss-match</b> in perfect, nonlinear dynamics between
  $$\begin{align}
  \mathcal{M}_{L:1}\left(\mathbf{E}_{0|L}^\mathrm{post}\right):= \mathcal{M}_L \circ \cdots \circ \mathcal{M}_1\left(\mathbf{E}_{0|L}^\mathrm{post}\right) \neq \mathbf{E}_{L}^\mathrm{filt}.
  \end{align}$$</li>
<li> The effectiveness of the <b>linear-Gaussian approximation</b> strongly depends on the <strong>length of the forecast window</strong> $\Delta t$;</li>
  <ul>
    <li>for sufficiently small $\Delta t$, the <strong>densities are well-approximated with Gaussians</strong>, yet there are <b>deformations induced due to nonlinearity</b>.</li>
  </ul>
<li>If the dynamics for the evolution of the densities are <b>weakly nonlinear</b>, re-initializing the model forecast with the posterior estimate can bring <strong>new information into the forecast states in the next DAW</strong>.</li>
<li> This has been exploited to a great extent by utilizing the <b>4D-cost function,</b><sup><b>11</b></sup> in which the filtering MAP cost function is <strong>extended over multiple observations simultaneously, and can be written in terms of a lagged state directly</strong>.</li>
</ul>
</div>

<div style="width:100%;float:left;font-size:30px">
<b>11.</b> Hunt, B.R., et al. (2004). <i>Four-dimensional ensemble Kalman filtering</i>. Tellus A: Dynamic Meteorology and Oceanography, 56(4), 273-277.
</div>

========================================================

### The 4D cost function

* Suppose now we want to write $p(\pmb{x}_{1:L}\vert \pmb{y}_{1:L})$, the <b style="color:#d95f02">joint smoothing posterior</b> over the current DAW, as a <strong>recursive update</strong> to the last <b style="color:#d95f02">smoothing posterior</b>.

* We will suppose that there is an <b>arbitrary shift $S\geq 1$</b>.

* Using a Bayesian analysis like before, we can write 
  
  $$\begin{align}
  {\color{#d95f02}{p(\pmb{x}_{1:L} \vert \pmb{y}_{0:L})}}
  &\propto  \int \mathrm{d}\pmb{x}_0 \underbrace{{\color{#d95f02}{p(\pmb{x}_0 \vert \pmb{y}_{0:L-1})}}}_{(1)} \underbrace{{\color{#7570b3}{\left[\prod_{k=L-S+1}^Lp(\pmb{y}_k \vert \pmb{x}_k)\right]}}}_{(2)} \underbrace{{\color{#1b9e77}{\left[\prod_{k=1}^L \pmb{\delta}\left\{\pmb{x}_k - \mathcal{M}_{k} \left(\pmb{x}_{k-1}\right)\right\}\right]}}}_{(3)}
  \end{align}$$
  where
  <ol>
    <li> is the marginal for $\pmb{x}_0$ of the last <b style="color:#d95f02">joint smoothing smoothing posterior</b> $p(\pmb{x}_{0:L-1}\vert\pmb{x}_{0:L-1})$;</li>
    <li> is the <b style="color:#7570b3">joint likelihood of the incoming observations</b> to the current DAW, given the background forecast;</li>
    <li> is the <b style="color:#1b9e77">free-forecast with the perfect model</b> $\mathcal{M}_k$.
  </ol>
  
* Using the fact that $p(\pmb{x}_{1:L} \vert \pmb{y}_{1:L} ) \propto p(\pmb{x}_{1:L} \vert \pmb{y}_{0:L})$, we can <strong>chain together a recursive fixed-lag smoother, sequentially across DAWs</strong>.

========================================================

### The 4D cost function

* Under the <b>linear-Gaussian assumption</b>, the resulting cost function takes the form

  $$\begin{alignat}{2}
  & & {\color{#d95f02} {\widetilde{\mathcal{J}} (\pmb{w})} } &= {\color{#d95f02} {\frac{1}{2} \parallel \hat{\pmb{x}}_{0:L-1}^\mathrm{post} - \mathbf{X}^\mathrm{post}_{0:L-1} \pmb{w}- \hat{\pmb{x}}^\mathrm{post}_{0:L-1} \parallel_{\mathbf{P}^\mathrm{post}_{0|L-1}}^2} } + {\color{#7570b3} {\sum_{k=L-S+1}^L \frac{1}{2} \parallel \pmb{y}_k - \mathbf{H}_k {\color{#1b9e77} { \mathbf{M}_{k:1}} }\hat{\pmb{x}}^\mathrm{post}_{0:L-1} - \mathbf{H}_k {\color{#1b9e77} {\mathbf{M}_{k:1}}} \mathbf{X}^\mathrm{post}_{0:L-1} \pmb{w} \parallel_{\mathbf{R}^{-1}_L}^2 } } \\
  \Leftrightarrow& & \widetilde{\mathcal{J}}(\pmb{w}) &= \frac{1}{2}(N_e - 1) \parallel\pmb{w}\parallel^2 + \sum_{k=L-S+1}^L \frac{1}{2}\parallel \hat{\pmb{\delta}}_k - \mathbf{S}_k \pmb{w}\parallel^2 
  \end{alignat}$$
  where the weights $\pmb{w}$ give the <b>update to the initial state</b> $\pmb{x}^\mathrm{post}_{0|L-1}$.
  
* In the <b>linear-Gaussian case</b>, the solution can again be found by a <strong>single iteration of Newton's descent</strong> for the cost function above,

  $$\begin{alignat}{2}
  \overline{\pmb{w}} &= 0 - \mathbf{H}_{\widetilde{\mathcal{J}}}^{-1}\nabla_{\pmb{w}} \widetilde{\mathcal{J}} ; \quad\quad &&
  \mathbf{T} &= \mathbf{H}_{\widetilde{\mathcal{J}}}^{-\frac{1}{2}}; \\
  \hat{\pmb{x}}^\mathrm{post}_{0|L}&= \hat{\pmb{x}}_{0|L-1}^\mathrm{post} + \mathbf{X}_{0|L-1}^\mathrm{post}\overline{\pmb{w}};\quad \quad&&
  \mathbf{P}_{0|L}^\mathrm{post} &= \left(\mathbf{X}^\mathrm{post}_{0|L-1}\mathbf{T}\right)\left(\mathbf{X}^\mathrm{post}_{0|L-1}\mathbf{T}\right)^\top / \left(N_e - 1\right).
  \end{alignat}$$


========================================================

### The 4D cost function

* When the <b>state and observation model are nonlinear</b>, using $\mathcal{H}_k$ and $\mathcal{M}_{k:1}$ in the cost function, this <strong>cost function can be solved iteratively to find local minimum with a recursive Newton step</strong> as on the last slide.

* This approach is at the basis of the <b>iterative ensemble Kalman smoother (IEnKS),</b><sup><b>12</b></sup> which produces a more accurate solution than the linear approximation when the models are highly nonlinear;

  * this also allows an easy <strong>generalization to optimizing hyper-parameters for the empirical density represented by the ensemble</strong> as a <b>Gaussian mixture</b>.
  
* Ensemble Gaussian mixture models as above have been used variously to: 
  * <b>correct for sampling error due to nonlinearity</b>,<sup><b>13</b></sup> 
  * <b>correct model error in the form of stochasticity and parametric error</b><sup><b>14</b></sup> and 
  * <b>optimize localization coefficients</b> for analyzing the spatially extended state.<sup><b>15</b></sup> 
  
<div style="width:100%;float:left;font-size:30px">
<b>12.</b> Bocquet, M., & Sakov, P. (2014).<i> An iterative ensemble Kalman smoother</i>. Quarterly Journal of the Royal Meteorological Society, 140(682), 1521-1535.<br>
<b>13.</b> Bocquet, M., Raanes, P., & Hannart, A. (2015). <i>Expanding the validity of the ensemble Kalman filter without the intrinsic need for inflation</i>. Nonlinear Processes in Geophysics, 22(6), 645-662.<br>
<b>14.</b> Raanes, P. N., Bocquet, M., & Carrassi, A. (2019). <i>Adaptive covariance inflation in the ensemble Kalman filter by Gaussian scale mixtures</i>. Quarterly Journal of the Royal Meteorological Society, 145(718), 53-75.<br>
<b>15.</b> Lorenc, A. C. (2003). <i> The potential of the ensemble Kalman filter for NWP—A comparison with 4D‐Var</i>. Quarterly Journal of the Royal Meteorological Society: A journal of the atmospheric sciences, applied meteorology and physical oceanography, 129(595), 3183-3203.
</div>

========================================================

## The single-iteration ensemble transform Kalman smoother (SIETKS)


* <strong>Every iteration of the 4D cost function</strong> comes at the <b style="color:#1b9e77">cost of the ensemble forecast</b>.

* In synoptic meteorology, e.g., $\Delta t \approx 6$ hours, the <b>linear-Gaussian approximation</b> of the evolution of the densities is often an <strong>adequate approximation</strong>;

  * <b style="color:#1b9e77">iterating over the nonlinear dynamics</b> <strong>may not be justified by the improvement in the forecast statistics</strong>.
  
* However, the <b>iterative optimization over hyper-parameters in the filtering step</b> of the classic ETKS can be run <strong>without the additional cost of model forecasts</strong>.

  * This is likewise the case for a <b>nonlinear observation operator in the filtering step</b>.

* A right transform $\boldsymbol{\Psi}_L$ can be found with iterative optimization of the filtering cost function 
  
  $$\begin{align}
   {\color{#d95f02} {\widetilde{\mathcal{J}}(\pmb{w})} } &= {\color{#1b9e77} {\frac{1}{2}(N_e - 1) \parallel\pmb{w}\parallel^2} } + {\color{#7570b3} {\frac{1}{2}\parallel \hat{\pmb{\delta}}_L - \mathbf{S}_L \pmb{w}\parallel^2 } }
  \end{align}$$
with cost <strong>expanding in the eigen value decomposition of the Hessian</strong> $\mathbf{H}_{\mathcal{J}} \in \mathbb{R}^{N_e \times N_e}$.

* Subsequently, the <b style="color:#d95f02">retrospective analysis</b> in the form of the filtering right-transform can be applied to <b style="color:#d95f02">condition the initial ensemble</b>
 
 $$\begin{align}
 \mathbf{E}^\mathrm{post}_{0|L} = \mathbf{E}_{0:L-1}^\mathrm{post} \boldsymbol{\Psi}_L
 \end{align}$$

* We <b>initialize the next DA cycle in terms of the retrospective analysis</b>, and gain the benefit of the improved initial estimate.

  * This leads to a <b style="color:#1b9e77">single iteration of the model forecast</b> ${\color{#1b9e77} {\mathcal{M}_{L:1} } }$, while <strong>still optimizing over the nonlinear filtering cost function</strong>.
  
========================================================

### The single-iteration ensemble transform Kalman smoother (SIETKS)


<div style="float:left; width:100%">
<ul>
  <li>Compared to the classic ETKS, this <strong>adds an outer loop</strong> to the <b style="color:#d95f02">filtering cycle</b> to produce the <b style="color:#d95f02">posterior, smoothing analysis</b>.</li>
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
</ul>
</div>


========================================================

### The single-iteration ensemble transform Kalman smoother (SIETKS)

<ul>
  <li>By framing the development of this method in the Bayesian MAP formalism for fixed-lag smoothing we can discuss its novelty.</li>
  <li>Similar to the IEnKS, this <strong>estimates the joint posterior over the DAW</strong> <b>via the marginal</b> for $\pmb{x}_{0|L-1}^\mathrm{post}$.</li>
  <li>However, instead of solving the 4D cost function, this <strong>sequentially solves the filtering cost function</strong> and <b>applies a retrospective analysis</b>.</li>
  <li> A similar retrospective analysis and re-initialization has been performed in some notable examples:
  <ul>
    <li>The <b>Running In Place (RIP) smoother</b><sup><b>16</b></sup></li>
    <ul>
      <li>The RIP is an iterative scheme over the model forecast, used to spin up the LETKF;</li>
      <li>this uses a lag of $L=1$ and multiple iterations of the filtering step to cold-start a filtering cycle.</li>
    </ul>
    <li>The <b>One Step Ahead (OSA) smoother</b><sup><b>17</b></sup> </li>
    <ul>
      <li>The OSA is a single iteration scheme, using a lag of $L=1$ and performing a retrospective analysis followed by a second analysis of the re-initialized state.</li>
      <li>Without model error, the second analysis of the re-initialized state reduces to the free forecast forward-in-time.</li>
    </ul>
  </ul>
  <li>With a <strong>single iteration, a perfect model and a lag of $L=1$</strong> <b>all these schemes coincide</b>.</li>
  <li><b>SIETKS generalizes these ideas</b> for <strong>arbitrary lags $L>1$ and shifts $S\leq L$, MDA in perfect models and iterative optimization of the filtering cost function alone for ensemble hyper-parameters</strong>.</li>
</ul>


<div style="width:100%;float:left;font-size:30px">
<b>16.</b> Kalnay, E., & Yang, S. C. (2010). Accelerating the spin‐up of ensemble Kalman filtering. Quarterly Journal of the Royal Meteorological Society, 136(651), 1644-1651.<br>
<b>17.</b> Desbouvries, F., Petetin, Y., & Ait-El-Fquih, B. (2011). Direct, prediction-and smoothing-based Kalman and particle filter algorithms. Signal processing, 91(8), 2064-2077.
</div>


========================================================
## Single-layer Lorenz-96 model, linear observations

<div style="float:left;width:100%">
<ul>
  <li>We <strong>simulate the performance of the SIETKS</strong> versus:
  <ul>
    <li>the <b>classic ETKS</b>,</li>
    <li>the <b>"linear" IEnKS (LIEnKS) using a single iteration</b>, and</li>
    <li>the <b>fully iterative IEnKS</b>.</li>
  </ul>
<li>Our study system is the $N_x=40$ dimensional, single-layer <b>Lorenz-96 model</b><sup><b>18</b></sup>.</li>
<ul>
  <li>The system is fully observed with observation error 
  $$\boldsymbol{\epsilon}_k \sim N(\pmb{0}, \mathbf{I}_{40})$$</li>
  <li>The forecast window is defined as $\Delta t = 0.05$, <strong>comparable to a 6 hour atmospheric forecast range</strong>.</li>
  <li>The observation map will be defined as $\mathcal{H}(\pmb{x}) = \pmb{x}$.</li>
  <li><strong>Tuned multiplicative inflation</strong> is selected for <strong>minimum smoothing RMSE</strong>, with discretization $\lambda \in \{1.0 + j \times 0.01\}_{j=0}^{10}$.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>The ensemble size ranges $N_e \in \{15, 17, \cdots, 41, 43\}$, where the unstable-neutral dimension of the model is $n_0 = 14$, making <strong>localization unnecessary</strong>.</li>
  <li>Adaptive inflation is implemented with the <b>finite-size formalism</b>,<sup><b>19</b></sup> with schemes denoted with "-N".</li>
    <li>RMSE and spread are taken as an average over $2\times 10^{4}$ observation times;</li>
  <li>an additional $5\times 10^{3}$ observation times are discarded as an initial spin to the steady state statistics.</li>
</ul>
</div>

<div style="width:100%;float:left;font-size:30px">
<b>18.</b> Lorenz, E. N. (1996, September). Predictability: A problem partly solved. In Proc. Seminar on predictability (Vol. 1, No. 1).<br>
<b>19.</b> Bocquet, M., Raanes, P. N., & Hannart, A. (2015). <i>Expanding the validity of the ensemble Kalman filter without the intrinsic need for inflation</i>. Nonlinear Processes in Geophysics, 22(6), 645-662.
</div>

========================================================
### Numerical demonstrations -- tuned inflation

 <div style="float:left; width:100%;">
<img style="width:100%", src="heat_plot_tanl_05_tuned.png" alt="Heat plot."/>
</div>
<div style="float:left; width:100%">
<ul>
</ul>
</div>


========================================================
### Numerical demonstrations -- adaptive inflation

 <div style="float:left; width:100%">
<img style="width:100%", src="heat_plot_tanl_05_adaptive.png" alt="Heat plot."/>
</div>


========================================================
### Numerical demonstrations -- tuned inflation

 <div style="float:left; width:100%">
<img style="width:100%", src="line_plot_tanl_05_tuned.png" alt="line."/>
</div>


========================================================
### Numerical demonstrations -- adaptive inflation

 <div style="float:left; width:100%">
<img style="width:100%", src="line_plot_tanl_05_adaptive.png" alt="line."/>
</div>

========================================================
## Single-layer Lorenz-96 model, nonlinear observations

* For a nonlinear observation map in the Lorenz-96 model, we choose
  
  $$\begin{align}
  \mathcal{H}(\pmb{x}) = \frac{\pmb{x}}{2} \circ\left[ \pmb{1} + \left(\frac{\vert \pmb{x}\vert}{10} \right)^{1-\gamma} \right]
  \end{align}$$
  
  where:
  
  * $\circ$ denotes the Hadamard product;
  * $\gamma=1$ defines a linear map; and 
  * the nonlinearity of the map $\mathcal{H}$ increases for larger $\gamma$.<sup><b>20</b></sup>
  
* The ETKF Newton step can be applied iteratively as an extension of the <b>maximum likelihood ensemble filter (MLEF)</b>.<sup><b>21</b></sup>

* Both the <b>ETKS and the SIETKS</b> can <strong>include an iterative analysis of the filtering cost function directly in their filtering steps</strong>.

* The (L)IEnKS does not need be modified in any way to handle the nonlinear observation operator, but the <b>LIEnKS</b> will again only use a <strong>single iteration of the 4D cost function</strong>.

* We compare the performance of these schemes versus $\gamma \in [1.0, 11.0]$, with SDA and MDA.

<div style="width:100%;float:left;font-size:30px">
<b>20.</b> Asch, M., Bocquet, M., & Nodet, M. (2016). <i>Data assimilation: methods, algorithms, and applications</i>. Society for Industrial and Applied Mathematics. See section 6.7.<br>
<b>21.</b>Zupanski, M. (2005). <i>Maximum likelihood ensemble filter: Theoretical aspects</i>. Monthly
Weather Review, 133:1710–1726,
</div>

========================================================
### Numerical demonstrations -- nonlinear observations (SDA)

 <div style="float:left; width:100%">
<img style="width:100%", src="nonlinear_obs_heat_plot_sda.png" alt="Heat plot."/>
</div>


========================================================
### Numerical demonstrations -- nonlinear observations (MDA)

 <div style="float:left; width:100%">
<img style="width:100%", src="nonlinear_obs_heat_plot_mda.png" alt="Heat plot."/>
</div>


========================================================
### Numerical demonstrations -- nonlinear observations (SDA)

 <div style="float:left; width:100%">
<img style="width:100%", src="nonlinear_obs_versus_lag_05_tanl_005_sda.png" alt="Heat plot."/>
</div>

========================================================
### Numerical demonstrations -- nonlinear observations (MDA)

 <div style="float:left; width:100%">
<img style="width:100%", src="nonlinear_obs_versus_lag_05_tanl_005_mda.png" alt="Heat plot."/>
</div>




========================================================
### Numerical demonstrations -- lag versus shift (SDA)

<div style="float:left; width:100%">
<img style="width:100%", src="versus_shift_heat_plot_sda.png" alt="Heat plot."/>
</div>



========================================================
### Numerical demonstrations -- lag versus shift (MDA)

<div style="float:left; width:100%">
<img style="width:100%", src="versus_shift_heat_plot_mda.png" alt="Heat plot."/>
</div>


========================================================
### Numerical demonstrations -- lag versus shift (SDA)

<div style="float:left; width:100%">
<img style="width:100%", src="versus_shift_line_plot_sda.png" alt="Heat plot."/>
</div>



========================================================
### Numerical demonstrations -- lag versus shift (SDA)

<div style="float:left; width:100%">
<img style="width:100%", src="versus_shift_line_plot_mda.png" alt="Heat plot."/>
</div>




========================================================
## Summary of results and open questions

* The <b>single-iteration ensemble transform Kalman smoother (SIETKS)</b> is an <strong>outer loop optimization of iterative, fixed-lag smoothing</strong> for weakly nonlinear forecast error dynamics.

* This uses the <strong>lagged, marginal posterior of 4D iterative schemes</strong>, but <b>iterates in the filtering step of the classic EnKS</b>.

  * This transform is then applied as a <strong>retrospective analysis</strong> on the states at the beginning of the DAW.
  
* The <b>SIETKS</b> <strong>sequentially solves the filtering cost function</strong> instead of the 4D cost function.

  * One benefit is that iteratively solving the filtering cost function <strong>does not depend on the nonlinear forecast model</strong> $\mathcal{M}_{L:1}$
    * This provided a more <strong>precise forecast with adaptive inflation than the LIEnKS</strong>, in the <b>weakly nonlinear regime</b>.
  * Another benefit is that this makes <strong>long MDA windows more stable than the LIEnKS</strong>.
    * This is more costly than LIEnKS, but the <b>cost expands in eigen value decompositions</b> of the Hessian $\mathbf{H}_{\widetilde{\mathcal{J}}}\in \mathbb{R}^{N_e \times N_e}$.
    * The fully iterative IEnKS expands in the cost of ensemble simulations over the DAW.
  
* Key open questions include:
  
  * can single-iteration smoothing be effectively combined with <strong>localization / hybridization as in an operational setting</strong>?

  * what is the general Bayesian formulation for single-iteration smoothing with  <strong>stochastic and parametric model error</strong>?

* Results in this presentation are projected to be submitted to an open access journal late June / July for open review and discussion.<sup><b>22</b></sup>

<div style="width:100%;float:left;font-size:30px">
<b>22.</b> Grudzien, C. & Bocquet, M. (2021).  <i>A fast, single-iteration ensemble Kalman smoother for online, sequential data assimilation</i>. In Preparation.
</div>

