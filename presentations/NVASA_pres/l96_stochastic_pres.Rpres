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
date: 10/19/2019
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
  <li> The Lorenz-96 model</li>
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

## Data assimilation in the geosciences

<ul>
  <li>Data assimilation and ensemble-based forecasting are the prevailing modes of prediction and uncertainty quantification in geophysical modeling.</li>
  <li>Data assimilation <b>(DA)</b> refers to techniques from:</li>
  <ol>
    <li>statistical inference;</li>
    <li>numerical analysis and optimization;</li>
    <li>and dynamical systems and automatic control</li>
  </ol>
</ul>

* used to combine simulations from a physics-based numerical model and real-world observations of a physical process.

* The output of DA is an estimate of a posterior probability density for the numerically simulated physical state, or some statistic of it.  

* In this Bayesian framework, an ensemble-based forecast represents a sampling procedure for the forecast-prior probability density.  

* The process of sequentially and recursively estimating the distribution for the system's state by combining model forecasts and streaming observations is known as filtering.  

========================================================
## Observation-analysis-forecast cycle

 <div style="float:left; width:50%">
<img style="width:100%", src="DA_sequence_Filter_01.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
<p style="text-align:center;font-size:30px">From: Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.</p>
</div>
<div style="float:left; width:50%">
<ul>
  <li>Numerical weather prediction (NWP) uses filtering techniques to produce weather forecasts in an observation-analysis-forecast cycle.</li>
  <li>In the left, we assume that we have an initial forecast-prior for the physics-based numerical model state.</li>
  <li>This can represent, e.g., the forecasted state of the atmosphere in terms of temperature, pressure and humidity over Reno, six hours in the future.</li>
  <ul>
    <li>This is generated from the simulation of the geophysical fluid dynamics, as they evolve in time given the appropriate forcings and boundary conditions.</li>
    <li>Mathematically, this is described by a system of PDEs, discretized spatially over three dimensions of the atmosphere and surface topography.</li>
  </ul>
</ul>
</div>


========================================================
### Observation

 <div style="float:left; width:50%">
<img style="width:100%", src="DA_sequence_Filter_02.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
<p style="text-align:center;font-size:30px">From: Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>We suppose that the "true" physical process evolves in time to the end of the first forecast.</li>
  <li>This corresponds to our real atmosphere reaching the forecast state of plus six hours.</li>
  <li>We suppose that at this time, we receive an observation of the atmosphere's state variables.</li>
</ul>
</div>

========================================================
### Analysis

 <div style="float:left; width:50%">
<img style="width:100%" src="DA_sequence_Filter_03.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
<p style="text-align:center;font-size:30px">From: Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>The observation comes with a likelihood function;
  <ul>
    <li>with the likelihood function we compute the likelihood of the model forecast given the observation.</li>
  </ul>
  <li>Using the forecast-prior and the likelihood, we estimate the Bayesian update of the prior to the posterior conditioned on the observation.</li>
  <li>The posterior density is denoted the analysis.</li>
</ul>
</div>

========================================================
## Forecast

 <div style="float:left; width:50%">
<img style="width:100%", src="DA_sequence_Filter_04.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
<p style="text-align:center;font-size:30px">From: Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>The analysis is then used as the initialization of the next forecast.</li>
  <li>Forecasting the model state forward in time, we produce a new prior.</li>
    <li>Chaotic evolution (the butterfly effect) that is typical in geophysical problems causes the model forecast to drift from the true state.</li>
  <ul>
    <li>This is in addition to the errors in:</li> 
    <ol>
      <li>accurately representing the true physical process with the imperfect numerical model; and</li>
      <li>estimating the "true" initial condition from incomplete and noisy observations.</li>
    </ol>
  </ul>
</ul>
</div>

========================================================
## Observation


 <div style="float:left; width:50%">
<img style="width:100%", src="DA_sequence_Filter_05.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
<p style="text-align:center;font-size:30px">From: Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>When a new observation becomes available...</li>
</ul>
</div>




========================================================
## Analysis

 <div style="float:left; width:50%">
<img style="width:100%", src="DA_sequence_Filter_06.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
<p style="text-align:center;font-size:30px">From: Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>We produce a new analysis...</li>
</ul>
</div>

========================================================
## Twin experiments

 <div style="float:left; width:50%">
<img style="width:100%", src="DA_sequence_Filter_07.png" alt="Diagram of the filter observation-analysis-forecast cycle."/>
<p style="text-align:center;font-size:30px">From: Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>And the cycle continues ad-infinitum...</li>
  <li>When the time series of observations is artificially generated by a numerical model in parallel with the numerical model forecast, this is known as a <b>twin experiment</b>.</li>
  <li>In a twin experiment, a "truth-twin" is run to:
  <ol>
    <li>generate the artificial timeseries of observations; and
    <li>then to verify the accuracy of the filter's predictions and analysis.</li>
  </ol>
  <li>The "model-twin" refers to the simulated forecast used in the observation-analysis-forecast cycle.</li>
  <li>Typically, the accuracy of the observation-analysis-forecast cycle is described in the root-mean-square-error (RMSE) of the estimated mean state of the analysis posterior density.</li>
  <li>This is computed using the difference of the model-twin mean state with the known truth-twin state.</li>
</ul>
</div>


========================================================

## Operational constraints on filtering

* Due to the large dimensionality and complexity of operational geophysical models, an accurate representation of the true Bayesian posterior is infeasible.  

  * The number of model state variables can be on the order of $\mathcal{O}\left(10^{9}\right)$ with the number of observations on the order of $\mathcal{O}\left(10^{8}\right)$<sup><b>1</b></sup>.

* Therefore, the DA cycles typically estimates the first two moments of the posterior, or its mode.

  * However, even the storage of the covariance matrix for the model state is infeasible,
  
  * thus empirical, low-rank covariance estimates are generated by the anomalies of the ensemble forecast.
  
* Due to the expense of generating model forecasts, the practical number of samples is typically on the order of $\mathcal{O}\left(10^2\right)$.

 * As such, a number of approximations are introduced in filtering schemes to compensate for the severe degeneracy in the sampling.

<div style="width:100%;float:left;font-size:30px">
<b>1.</b>Carrassi, A. et al. <em>Data assimilation in the geosciences: An overview of methods, issues, and perspectives.</em> Wiley Interdisciplinary Reviews: Climate Change 9.5 (2018): e535.
</div>


========================================================

## Toy models for benchmark twin experiments


* A Gaussian approximation for the prior, posterior and likelihoods is at the basis of all operational DA schemes, due to the operational constraints.
  
* In a linear-Gaussian model, the effect of estimating the mean or the mode would be the same;

  * however, in operational DA the true distributions are often non-Gaussian and the physical dynamics are highly nonlinear.

* Therefore, different filtering assumptions and approximations lead to dramatically different results in practice.

* Toy models are small-scale numerical analogues of full-scale geophysical dynamics which are used in twin experiments.

<ul>
  <li>Toy models:</li>
  <ol>
    <li>exhibit fundamental features of large-scale dynamics;</li>
    <li>are transparent in the model structure and assumptions;</li>
    <li>yet are also computationally simple to resolve and sample.</li>
  </ol>
  <li> Toy models are thus used for diagnostic purposes with filtering schemes;</li>
  <ul>
    <li> particularly, toy models help to determine the accuracy and robustness of the various approximations and assumptions in a learning scheme under a variety of configurations.</li>
  </ul>
</ul>

========================================================
## Single layer Lorenz-96 model

 <div style="float:left; width:50%">
<img style="width:100%", src="global_circulation.png" alt="Image of global atmospheric circulation."/>
<p style="text-align:center;font-size:30px">Courtesy of: Kaidor via Wikimedia Commons (CC 3.0)</p>
</div>
<div style="float:left;width:50%">
<ul>
  <li>Imagine a simplified 1-dimensional model of the atmosphere around a lattitude circle.</li>
  <li>We will suppose that this lattitude circle can be discretized into $n$ total longitude sectors;</li>
  <ul>
    <li>each sector $i$ is represented by a single state variable $x_i$.</li>
  </ul>
  <li>The classical Lorenz-96 model is given as,
  $\frac{\mathrm{d}\mathbf{x}}{\mathrm{d} t} \triangleq \mathbf{f}(\mathbf{x}),$ where,</li>
  <ul>
    <li>for each state component $i\in\{1,\cdots,n\}$,
    $$\begin{align}\large{f_i(\mathbf{x}) =-x_{i-2}x_{i-1} + x_{i-1}x_{i+1} - x_i + F}.\end{align}$$</li>
  </ul>
 <li>The state variables $x_i$ have periodic boundary conditions modulo $n$, $x_0=x_n$,  $x_{-1}=x_{n-1}$ and $x_{n+1}=x_{1}$.  </li>
  <li> The term $F$ in the Lorenz-96 system is the forcing parameter that injects energy to the model.</li>
  <li>The terms in the Lorenz-96 model, while not a true physics-based model, approximate geophysical behavior with:</li>
  <ol>
    <li>external forcing and internal dissipation with the linear terms; and</li>
    <li>advection and conservation of energy in the quadratic terms.</li>
  </ol>
</ul>
</div>


========================================================
## Two Layer Lorenz-96 Model

 <div style="float:left; width:40%">
<img style="width:100%", src="two_layer_lorenz.png" alt="Image of two-layer Lorenz-96 model coupling between fast and slow layers."/>
<p style="text-align:center;font-size:30px">From: Wilks, D. <em>Effects of stochastic parametrizations in the Lorenz'96 system.</em> Quarterly Journal of the Royal Meteorological Society 131.606 (2005): 389-407. </p>
</div>

<div style="width:60%; float:left">
<ul>
  <li>A two layer version of the Lorenz-96 system also exists which simulates coupled, ocean-atmosphere dynamics.</li>
  <li>The inner circle represents oceanic variables evolving at a slow time scale;</li>
  <ul>
    <li>these are coupled to the outter circle of atmospheric variables evolving at a fast time scale.</li>
  </ul>
  <li>The two layer model is of particular interest for examining the effects of model uncertainty, </li>
  <ul>
    <li>e.g., when the fast variables are not evolved accurately in the model-twin.</li>
  </ul>
  <li> This is a common model to study stochastic model reduction.</li>
  <ul>
    <li>E.g., instead of simulating the fast-variable dynamics, one may parameterize their effect on the slow variables with a stochastic process.</li>
  </ul>
  <li>This kind of approximation can be justified mathematically due to the central limit theorem:</li>
  <ul>
    <li>in the asymptotic separation of the time scales for the fast and slow variables,</li>
    <li>the effect of the fast variables on the slow variables will reduce to additive, Gaussian noise which perturbs a mean-field ordinary differential equation<sup><b>2</b></sup>.</li>
  </ul>
</ul>
</div>
<div style="width:100%;float:left;font-size:30px">
<b>2.</b> Gottwald, G. et al. <em>Stochastic climate theory</em>. Nonlinear and Stochastic Climate Dynamics. 209--240. 2015. Cambridge University Press.
</div>

========================================================
## Bias in twin experiments

* The two layer Lorenz-96 model is commonly used in benchmark twin experiments thus to study the effects of model uncertainty and model reduction errors in multiscale dynamics.

  * This helps examine the effects of bias in the forecast prior when the physical process model that generates the model-twin does not match that of the truth-twin.
  
* It has recently been shown in a deterministic, biased-model setting that the numerical precision of the discretization of the ensemble forecast can be significantly reduced without a major deterioration of the DA cycle's (relative) predictive performance<sup><b>3</b></sup>.  

  * In this setting, the model bias overwhelms the errors that are introduced due to precision loss when the model-twin is resolved with a low order of accuracy.

* However, important differences in the statistical properties of model forecasts of stochastic dynamical systems have been observed due to the discretization errors of certain low-order schemes.  

  * For example, Frank & Gottwald develop an order 2.0 Taylor scheme to correct the bias in the drift term induced by the Euler-Maruyama scheme in their study system<sup><b>4</b></sup>. 

<div style="width:100%;float:left;font-size:30px">
<b>3.</b> Hatfield, S. et al.<em> Choosing the optimal numerical precision for data assimilation in the presence of model error</em>. Journal of Advances in Modeling Earth Systems, 10, 2177–2191, 2018.<br>
<b>4.</b> Frank, J. and Gottwald, G. A.<em> A Note on Statistical Consistency of Numerical Integrators for Multiscale Dynamics</em>. Multiscale Modeling &
Simulation, 16, 1017–1033, 2018.
</div>
  
========================================================
## L96-s Model

* We are interested in whether the bias of numerical solvers in stochastic dynamical systems also biases twin experiment statistics for, e.g., benchmarking filters.

<ul>
  <li>We define the L96-s model as follows,
  $$\begin{align}
\frac{\mathrm{d} \mathbf{x}}{\mathrm{d} t} \triangleq \mathbf{f}(\mathbf{x}) + s(t)\mathbf{I}_{n}\mathbf{W}(t),
\end{align}$$
  where</li>
  <ol>
    <li> $\mathbf{f}$ is defined as in the single layer Lorenz-96 model</li>
    <li>$\mathbf{I}_n$ is the $n\times n$ identity matrix,</li>
    <li>$\mathbf{W}(t)$ is an $n$-dimensional Wiener process; and</li>
    <li>$s(t):\mathbb{R}\rightarrow \mathbb{R}$ is a measurable function of (possibly) time-varying diffusion coefficients.</li>
  </ol>
  <li>We study the effect of bias in the numerical time-discretization of the evolution of L96-s when the truth and model twins are both run in this model.</li>
  <ul>
    <li>This is a toy model analogue to a geophysical problem where the numerical model is unbiased in representing the true physics, but where the physics are intrinsically random.</li>
  </ul>
  <li>"Physically", this represents an idealized two layer Lorenz-96 model in which the separation of the time scale of the atmosphere and ocean is taken to infinity.</li>
  <ul>
    <li>This is also a common model configuration for filter benchmarks in the geophysical DA community.</li>
  </ul>
</ul>

========================================================
## Strong versus weak convergence

<ul>
  <li>We only study numerical integration schemes which converge in the strong sense;</li>
  <ul>
    <li>strong convergence measures the expected path-discretization errors over all possible Wiener processes starting at an initial condition.</li>
    <li>This is the analogue of the usual discretization error in deterministic integration.</li>
  </ul>
  <li> Particularly, if $\mathbf{x}_\mathrm{SP}$ is an exact sample path, evolving with respect to a particular Wiener process;</li>
  <li> and $\mathbf{x}$ is an approximation of this path, discretized at a maximum step size of $\Delta$;</li>
  <li>loosely, we say the approximate $\mathbf{x}$ converges strongly to $\mathbf{x}_\mathrm{SP}$ at order $\gamma$ if:
  </li>
  <ul>
    <li>there exists a $\Delta_0$ and a constant $C>0$ such that for every $\Delta &lt; \Delta_0$
  </ul>
  <li>then the expected discretization error is bounded as
    $$\begin{align}
\mathbb{E}\left[\left\Vert \mathbf{x}(T) - \mathbf{x}_\mathrm{SP}(T)\right\Vert\right] \leq C \Delta^\gamma
\end{align}$$
where these are the states, evolved from time $0$ to time $T$.
</li>
<li>Weak convergence measures the error in representing some statistic of the forward distribution given the evolution an initial point Dirac-delta distribution over all possible realizations of the Wiener process.</li>
  <ul>
    <li>Particularly, if $g$ is a $2(\gamma +1)$ continuously differentiable function of at most polynomial growth;</li>
    <li> we say that $\mathbf{x}$ converges weakly to $\mathbf{x}_\mathrm{SP}$ at order $\gamma$ if for all $\Delta< \Delta_0$, 
      $$\begin{align}
\left\Vert \mathbb{E}\left[ g(\mathbf{x}(T)) - g(\mathbf{x}_\mathrm{SP}(T))\right] \right\Vert \leq C \Delta^\gamma,
\end{align}$$
for any such statistic $g$.
    </li>
  </ul>
  <li>Loosely, strong convergence measures the mean of the path-discretization errors, while weak convergence can measure the error in representing the mean over all paths.</li>
</ul>

========================================================
## Strong versus weak convergence in twin experiments

<ul>
  <li>Note: integration schemes that converge in the strong sense also converge in the weak sense,</li>
  <ul>
    <li>however, weak schemes aren't guaranteed to converge in the strong sense.</li>
  </ul>
  <li>For twin experiments, there is an important distinction between these modes of convergence:</li>
  <ul>
    <li>The truth-twin should be generated by a simulation which is precise in the strong sense,</li>
    <ul>
      <li>here we assume we have observations of a path that is consistent with the governing dynamics <sup><b>5</b></sup>.</li>
    </ul>
    <li>On the other hand, an ensemble forecast representation of the prior needs to converge in the weak sense alone;</li>
    <li>indeed, the forecast represents the sampling of the prior density, and we do not need to ensure the precision of each path solution if the density is accurate.</li>
    <ul>
      <li>Therefore, the model-twin should be evaluated in terms of the precision in the weak sense.</li>
    </ul>
  </ul>
</ul>

<div style="width:100%;float:left;font-size:30px">
<b>5.</b>Hansen, J. A. and Penland, C. <em>Efficient approximate techniques for integrating stochastic differential equations</em>. Monthly weather review. 134, 3006–3014, 2006.
</div>

========================================================
## Integration schemes

<ul>
  <li>We study three commonly used numerical integration schemes for stochastic differential equations (SDEs):</li>
  <ol>
    <li>Euler-Maruyama -- a simple extension of the deterministic Euler scheme, order 1.0 strong convergence in L96-s.</li>
    <li>4-stage Runge-Kutta -- a simple extension of the determinstic 4-stage Runge-Kutta scheme<sup><b>6</b></sup>, order 1.0 strong convergence in L96-s</li>
    <li>Second order Taylor -- an integration scheme based on the Taylor-Stratonovich expansion<sup><b>7</b></sup>, order 2.0 strong convergence in L96-s.</li>
  </ol>
  <li>The derivation of the order 2.0 strong Taylor scheme for the Lorenz-96 model is nontrivial and has not appeared earlier in the literature to the authors' knowledge.</li>
  <ul>
    <li>Because L96-s model has:</li>
    <ol>
      <li> constant or vanishing second derivatives in the deterministic component;</li>
      <li>periodic boundary conditions; and</li> 
      <li>additive scalar noise;</li> 
    </ol>
    <li>we can compute this scheme efficiently, with complexity growing linearly in the system dimension $n$.</li>
  </ul>
<ul>
<div style="width:100%; float:left; font-size:30px"/>
<b>6.</b> Rüemelin, W.<em> Numerical treatment of stochastic differential equations</em>, SIAM Journal on Numerical Analysis, 19, 604–613, 1982.
 <br>
<b>7.</b> Kloeden, P. and Platen, E. Numerical Solution of Stochastic Differential Equations, Stochastic Modelling and Applied Probability, Springer
Berlin Heidelberg, page 359. 2013.
</div>


========================================================
## Strong convergence benchmarks

 <div style="float:left; width:50%">
<img style="width:100%", src="strong_convergence_5_pane.png" alt="Plot of strong convergence discretization error versus step size."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>In the left, we plot the estimated strong convergence discretization error in the vertical axis versus the time-discretization size in log-log base 10 scale.</li>
  <li>The point estimates are given by the average estimated discretization error over 500 independent batches of simulations.</li>
  <ul>
    <li>Each batch simulates the evolution of an initial condition with respect to 100 independent Wiener processes.</li>
    <li>For each Wiener process, we simulate a finely discretized path solution $\mathbf{x}_\mathrm{SP}$ with error on $\mathcal{O}\left(10^{-7}\right)$, and a coarser approximation by one of the tested methods.</li>
    <li>We estimate the quantity,
    $$\begin{align}
    \mathbb{E}\left[\left\Vert \mathbf{x}(T) - \mathbf{x}_\mathrm{SP}(T)\right\Vert\right]
    \end{align}$$
    as the mean difference of the finely discretized solution versus the coarse discretization over all Wiener processes in the batch.</li>
  </ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>It is known that these batch-mean estimates are realizations of Gaussian random variables distributed around the true expectation for sufficiently many samples of Wiener processes.</li>
  <li>Therefore, the slope (order of convergence) is estimated with weighted least squares with weights proportional to the inverse standard deviation of the batch realizations.</li>
</ul>
</div>

========================================================
## Strong convergence benchmarks continued

 <div style="float:left; width:50%">
<img style="width:100%", src="strong_convergence_5_pane.png" alt="Plot of strong convergence discretization error versus step size."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>The parameter $s$, fixed for each panel, is the diffusion level in the L96-s model.</li>
  <li>We note that all the orders of convergence are empirically verified here.</li>
  <ul>
    <li>However, the constant $C$ in the bound $C\Delta^\gamma$ has a large impact on the overall strong discretization error.</li>
  </ul>
  <li>Particularly, we see that in the low diffusion regime, the order 1.0 Runge-Kutta scheme has an overall discretization error comparable to the order 2.0 Taylor scheme.</li>
  <li>The performance of the Runge-Kutta scheme varies significantly, however, between low and high diffusion levels.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>While the order of convergence remains the same in all diffusion regimes, the difference in performance is reflected in the constant $C$.</li>
</ul>
</div>

========================================================
## Weak convergence

 <div style="float:left; width:50%">
<img style="width:100%", src="weak_convergence_5_pane.png" alt="Plot of weak convergence discretization error versus step size."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>


<div style="float:left; width:50%">
<ul>
  <li>The effect of the constant is even more pronounced in the weak convergence metric.</li>
  <li>We see that the order 2.0 Taylor scheme fails to outperform the order 1.0 Runge-Kutta scheme in this metric for the low diffusion regime.</li>
  <li>Moreover, the overall weak discretization error varies on an order of magnitude between low and high diffusion levels.</li
  </ul>
  <li>The high precision in the strong sense across all diffusion regimes makes the Taylor scheme a natural choice for generating the truth-twin.</li>
  <li>On the other hand, the Runge-Kutta scheme is appealing to generate the ensemble forecast of the model-twin, due to its accuracy in the weak sense.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>However, because the weak convergence of the Runge-Kutta scheme varies by an order of magnitude between diffusion levels, we use the Taylor scheme as a benchmark in the following experiments.</li>
  <li>We study how the ensemble forecast statistics of the Euler-Maruyama and the Runge-Kutta scheme differ from those generated by the Taylor scheme.</li>
</ul>
</div>

========================================================
## Ensemble forecast statistics -- fine discretization

 <div style="float:left; width:50%">
<img style="width:100%", src="ensemble_stats_4_times_5_fine.png" alt="Plot ensemble forecast bias versus time."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>

<div style="float:left; width:50%;">
<ul>
  <li>In the left plot, we generate 500 initial conditions of the L96-s model and forecast the initial condition with 100 independent Wiener processes to time plus 10 (horizontal axis).</li>
  <li>This ensemble of evolved states is then used to compute the empirical, ensemble-estimated mean and ensemble-estimated spread of the forward distribution.</li>
  <li>This is performed over each of the integration schemes:</li>
  <ol>
    <li>order 2.0 Taylor</li>
    <li>Euler-Maruyama</li>
    <li>4-stage Runge-Kutta</li>
  </ol>
  <li>In the top panels, we compute the root-mean-square-deviation of the ensemble mean of either the Euler-Maruyama scheme or the Runge-Kutta scheme from the ensemble mean of the Taylor scheme as a base of comparison.</li>
  <li>In the bottom panels, we compute the ratio of the ensemble spread of either the Euler-Maruyama scheme or the Runge-Kutta scheme with the ensemble spread of the Taylor scheme as a basis of comparison.</li>
  <li>Here, the Taylor scheme uses a step size of $\Delta=10^{-3}$ and the same step size is used for each the Euler-Maruyama and Runge-Kutta schemes.</li>
</ul>
</div>


========================================================
## Ensemble forecast statistics -- fine discretization continued

 <div style="float:left; width:50%">
<img style="width:100%", src="ensemble_stats_4_times_5_fine.png" alt="Plot of ensemble forecast bias versus time."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>

<div style="float:left; width:50%;">
<ul>
  <li>We plot the summary statistics versus forecast time over the 500 initial conditions, where:</li>
  <ul>
    <li>the median is plotted as a solid line;</li>
    <li>the inner 80 percentile is plotted shaded;</li>
    <li>the min/ max values are plotted in dashed.</li>
  </ul>
  <li>We note, the ensemble statistics of the Runge-Kutta scheme have almost no appreciable difference from the Taylor scheme for forecast times of up to almost $T=3$.</li> 
  <li>On the other hand, there is a rapid divergence of the ensemble mean and a bias in the ensemble spread of the Euler-Maruyama, with the median spread ratio above 1.0 asymptotically.</li>
</ul>
</div>

========================================================
## Ensemble forecast statistics -- coarse discretization

 <div style="float:left; width:50%">
<img style="width:100%", src="ensemble_stats_4_times_5_coarse.png" alt="Plot of ensemble forecast bias versus time."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>


<div style="float:left; width:50%;">
<ul>
  <li>On the left, we evaluate the same plot except where the Rung-Kutta and Euler scheme use a step size of $\Delta=10^{-2}$ while the benchmark Taylor scheme uses a step size of $\Delta=10^{-3}$.</li>
  <li>In this case, there is a more rapid onset of the divergence of the ensemble means for both schemes, as well as differences induced in the ensemble spread.</li>
  <li>The Euler-Maruyama scheme in particular goes through extreme divergence of the ensemble means, especially in the low difussion regimes.</li>
  <li>Likewise, the ensemble spread is extremely biased for the Euler-Maruyama scheme, where the ensemble spread ratio has a miniumum value consistently above 1.0.</li>
  <li>On the other hand, the Runge-Kutta scheme does not have such extreme divergence of trajectories, and the spread remains unbiased asymptotically.</li>
</ul>
</div>


========================================================
## Summary of bias in ensemble forecast

* We confirm the overall robustness of the Runge-Kutta scheme in generating ensemble-forecast statistics in the L96-s model.

* We note that even for a coarse time step of $\Delta=10^{-2}$, the Runge-Kutta scheme has an unbiased spread compared with the Taylor scheme using a step size of $\Delta=10^{-3}$.
  
  * Even if the divergence of the Runge-Kutta trajectories from the Taylor trajectories occurs earlier with the coarse time step, 
  
  * the divergence of their ensemble means matches the asymptotic divergence of the finely resolved Runge-Kutta scheme when using a time-step of $\Delta=10^{-3}$.
  
* On the other hand, the Euler-Maruyama scheme introduces systematic biases into ensemble forecast statistics.

  * Firstly, the asymptotic ensemble spread is artifically larger, due to the innacuracy in the numerical integration.
  
  * Secondly, there is extreme divergence of trajectories which causes the ensemble mean to depart from that of the benchmark Taylor scheme, with over an order of magnitude difference compared with the Runge-Kutta scheme.

* This is concerning as the Euler-Maruyama scheme is commonly used to simulate systems of SDEs for twin experiments.

* While this indicates the biasing of ensemble forecast statistics, this doesn't yet demonstrate the effect of this bias on a filter twin experiment.

  * This is demonstrated in the following experiements.


========================================================
## Taylor benchmark configuration -- filter statistics

 <div style="float:left; width:50%">
<img style="width:100%", src="ty_fine_obs_fine_ens.png" alt="Plot of benchmark Taylor configuration filtering statistics."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>On the left, we plot the twin-experiment RMSE and ensemble spread for an ensemble Kalman filter, in which both the truth-twin and model-twin are generated with the order 2.0 Taylor scheme, each with step size $\Delta=10^{-3}$.</li>
  <li>The vertical axis is the diffusion level $s$ while the horizontal axis is the variance of the error in the observations given to the ensemble Kalman filter.</li>
  <li>We take $N=10^2$ samples in the ensemble Kalman filter, while the state dimension is $n=10$ to guarantee convergence of the filtering statistics without additional techniques (inflation/ localization).</li>
  <li>The RMSE and spread are computed as the asymptotic average over $2.5\times 10^{4}$ analysis cycles.</li>
  </ul>
</div>
<div style="float:left; width:100%;">
<ul>
  <li>We see that the analysis RMSE is comparable to the analysis spread, and lower than the standard deviation of the error in the observations.</li>
  <ul>
    <li>This indicates that this is indeed represents the stable filter statistics.</li>
  </ul>
  <li>In the following, we demonstrate the effect of varying the model-twin integration scheme.</li>
  <li>We will vary the method of ensemble integration between the Runge-Kutta scheme and the Euler-Maruyama scheme, each with a step size between $\Delta\in\left\{10^{-3},10^{-2}\right\}$.</li>
</ul>
</div>

========================================================
## Filter benchmark -- Runge-Kutta model-twin, coarse discretization

 <div style="float:left; width:50%">
<img style="width:100%", src="rk_fine_obs_coarse_ens.png" alt="Plot of coarse Runge-Kutta filter simulation versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li>As was indicated with the ensemble statistics, the difference between generating the ensemble with the Runge-Kutta with a step size $\Delta= 10^{-3}$ scheme and the benchmark Taylor scheme is negligible.</li>
  <li>The difference in the filtering statistics for these two configurations is on the order of $10^{-6}$.</li>
  <li>We increase the step size of the Runge-Kutta scheme to $\Delta=10^{-2}$ and plot the differences between the RMSE and the ratio of the ensemble spread, versus the benchmark Taylor configuration.</li>
  <li>When we increase the step size of the Runge-Kutta scheme to $\Delta=10^{-2}$, we introduce small errors,</li>
  <ul>
    <li>however, the residuals are unstructured in sign or magnitude.</li>
  </ul>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>Indeed, the mean of the difference in the RMSE is approximately $8\times 10^{-5}$ though with a standard deviation of approximately $10^{-3}$ (on the order of the weak-discretization error).</li>
  <li>This indicates that the observed differences in the filtering statistics can be attributed to random numerical errors, which are themselves unbiased.</li>
</ul>
</div>

========================================================
## Filter benchmark -- Euler-Maruyama model-twin, fine discretization

 <div style="float:left; width:50%">
<img style="width:100%", src="em_fine_obs_fine_ens.png" alt="Plot of of coarse Runge-Kutta filter simulation versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>
<div style="float:left; width:50%">
<ul>
  <li>In contrast, when we generate the ensemble forecast with the Euler-Maruyama scheme with time step $\Delta=10^{-3}$, we notice structure in the residuals.</li>
  <li>For low diffusion regimes, the RMSE of the ensemble Kalman filter using the Euler-Maruyama scheme suffers from the bias observed in the ensemble forecast.</li>
  <li>Likewise, the spread in the ensemble Kalman filter suffers from this artificial inflation observed earlier.</li>
  <li>However, it is important to note that in high diffusion regimes, the RMSE and spread of the ensemble are nearly identical for the ensemble Kalman filter when using either the Taylor or Euler-Maruyama scheme.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>Particularly, the level at which the bias impacts the twin experiment statistics depends strongly on the observation uncertainty, and most especially on the model uncertainty.</li>
  <li>We investigate next the effect of increasing the step size of the Euler-Maruyama scheme to $\Delta=10^{-2}$ when generating the ensemble.</li>
</ul>
</div>



========================================================
## Filter benchmark -- Runge-Kutta model-twin, coarse discretization

 <div style="float:left; width:50%">
<img style="width:100%", src="em_fine_obs_coarse_ens.png" alt="Plot of coarse Euler-Maruyama filter simulation versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>
<div style="float:left; width:50%">
<ul>
  <li>On the left, we plot the differences in the RMSE and the ensemble spread when generating the ensemble with the Euler-Maruyama scheme with the coarse step-size.</li>
  <li>The structure of the residuals remains largely the same, but the magnitude changes dramatically.</li>
  <li>In particular, for low diffusion regimes we see that the discretization error is sufficient to introduce filter divergence.</li>
  <li>However, the effect of this bias on the filtering statistics is once again relaxed in the presence of high model uncertainty.</li>
  <ul>
    <li>For high levels of diffusion, $s\geq 0.5$, the difference of the RMSE with that when the ensemble is generated with the benchmark Taylor scheme is on the order of $10^{-2}$.</li>
  </ul>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>However, we consistently see the bias in the ensemble spread, present once again from the earlier ensemble forecast statistics.</li> 
</ul>
</div>

========================================================
## Filter benchmark -- Runge-Kutta model-twin, coarse discretization, coarse truth-twin

 <div style="float:left; width:50%">
<img style="width:100%", src="rk_coarse_obs_coarse_ens.png" alt="Plot of of coarse Runge-Kutta filter simulation with coarse truth-twin versus Taylor benchmark."/>
<p style="text-align:center;font-size:30px">From: Grudzien et al. <em>On the numerical integration of the Lorenz-96 model, with scalar additive noise, for benchmark twin experiments</em>. In submission.</p>
</div>

<div style="float:left; width:50%">
<ul>
  <li> As an additional check, we test the benchmark configuration versus using:</li>
  <ul>
    <li>the Runge-Kutta scheme with step size $\Delta=10^{-2}$ to generate the model-twin; and</li>
    <li>the Taylor scheme with step size $\Delta = 5 \times 10^{-3}$ to generate the truth-twin.</li> 
  </ul>
  <li>The configuration ensures that the expected discretization error is less than $10^{-3}$ over all diffusion regimes.</li>
  <li>While it is possible that the innacuracies in the truth-twin have now added some structure in the residuals, the results are largely the same as in the configuration with the more accurate truth-twin.</li>
</ul>
</div>
<div style="float:left; width:100%">
<ul>
  <li>When increasing the step size of the truth-twin with the model-twin generated by the Euler-Maruyama scheme the results are also largely the same.</li>
  <ul>
    <li>This has the effect of relaxing the issues in the Euler-Maruyama scheme when the model-twin uses a step size of $\Delta=10^{-3}$.</li>
    <li>However, there is still filter divergence when the model-twin uses a step size of $\Delta=10^{-2}$.</li>
  </ul>
  <li>These results thus suggest a computationally efficient and statistically robust configuration for twin experiments using the Taylor scheme for the truth-twin and the Runge-Kutta scheme for the model-twin.</li>
  <ul>
    <li>The step size of the truth-twin can be taken as large as $\Delta=5\times 10^{-3}$ and the step size of the model-twin as large as $\Delta=10^{-2}$ without biasing the benchmark statistics.</li>
  </ul>
</ul>
</div>


========================================================
## Conclusions

* Typically, the classical Lorenz-96 system is simulated with a 4-stage Runge-Kutta scheme with step size up to $0.5$ in deterministic settings.

  * We have shown that the same standards cannot apply to twin experiments in the commonly used form of the L96-s.
  
* Particularly, we must make a distinction between strong and weak convergence, and its impact on the truth-twin and the model-twin-respectively.

* While Euler-Maruyama is a commonly used integration scheme for SDEs, we find that it introduces strong, systematic bias into twin experiments when the step size is greater than or equal to $\Delta=10^{-2}$.

  * The effect of the bias depends strongly on the observation and especially model uncertainty in a twin experiment;
  
  * however, the bias is sufficient to cause filter divergence in weak diffusion regimes.
  
* On the other hand, we find that the 4-stage Runge-Kutta scheme is a statistically robust solver, without the systematic biases encountered in the Euler-Maruyama scheme.

  * For small step sizes $\Delta$ on $\mathcal{O}\left(10^{-3}\right)$, we find virtually no difference between the Runge-Kutta scheme and the higher order Taylor scheme.
  
  * Even while a step size of $\Delta=10^{-2}$ introduces additional discretization error, this error doesn't significantly influence the RMSE or spread of the ensemble Kalman filter in twin experiments.
  
========================================================
## Conclusions -- continued

<ul>
  <li>However, due to the computational constraints in running twin experiments, a step size of $\Delta=10^{-3}$ is often unreasonable for generating the truth-twin or model-twin.</li>
  <li> Often, a step size on $\mathcal{O}\left(10^{-2}\right)$ is what can be afforded in a typical benchmark study.</li>
  <li> This excludes the use of Euler-Maruyama from statistically robust twin experiments entirely. </li>
  <li> However, we demonstrate in our work that an overall discretization error can be bounded by $10^{-3}$, using:</li>
  <ol>
    <li>the 4-stage Runge-Kutta scheme with step size $\Delta=10^{-2}$ to generate the model-twin; and</li>
    <li> the order 2.0 Taylor scheme with step size $\Delta=5\times 10^{-3}$.</li>
  </ol>  
  <li>As the greatest expense is in generating the model-twin, this forms a practical compromise, which our diagnostics demonstrate does not bias the outcomes of the filtering statistics.</li>
  <li>In our work, we thus provide a computationally efficient framework for statistically robust twin experiments in the L96-s model.</li>
  <li>Pursuant to this framework, we have provided a novel derivation of ther order 2.0 Taylor scheme for the L96-s model.</li>
  <ul>
    <li>This derivation has not previously appeared in the literature to the authors' knowledge, and we moreover provide benchmarks on the convergence of this and other schemes.</li>
  </ul>
  <li> As an open question, it is yet to be determined more generally:</li>
  <ul>
    <li><strong>Can using weak integration schemes (which may not converge to any sample path) reduce the computational burden of ensemble-based forecasts in geophysical models?</strong></li>
  </ul>
  <li>If the goal of the forecast is to converge in distribution alone, this may be a viable alternative to traditional geophysical modeling paradigms.</li>
</ul>

