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

========================================================
autosize: true
incremental: true
width: 1920
height: 1080

<div style="text-align:center; width:100%; float:left;">
<h1>An open source framework for end-to-end<br> re-forecast studies in GSI-WRF-MET</h1>
<h3>By Colin Grudzien</h3>
<h4><b>With thanks to:</b></h4>
<h5>Minghua Zheng, Ivette Hern&aacute;ndez Ba&ntilde;os, CW3E's USAF Group and CW3E's AR-Recon Team for important discussions about the GSI-WRF-MET stack and sharing library implementation details.</h5>

<h4><b>With very special thanks to:</b></h4>
<h5>Caroline Papadopoulos, Rachel Weihs, Christopher Harrop, CW3E's West-WRF Team / NRT Team and CW3E's Forecast Verification Team for sharing code that formed the basis of these workflows</h5> 
<div style="float:left; width:100%; text-align:center; padding-top:20px;">
<div style="float:left; width:30%; text-align:center;  padding-top:40px">
</div>
<div style="float:left; width:40%; text-align:center; padding-top:20px">
<img style="width:100%", src="CW3E-Logo.png" alt="Center for Western Weather and Water Extremes."/>
</div>
<div style="float:left; width:30%; text-align:center;  padding-top:40px">
</div>
</div>

</div>

========================================================
## Introduction

* I am a <b>data assimilation research scientist</b> and <b>scientific software developer</b> at the <strong>Center for Western Weather and Water Extremes (CW3E)</strong>.

* One of CW3E's core programs is known as the <b>Atmospheric River Reconnaissance (AR-Recon) program</b>.

  * This is a <strong>research and operations partnership</strong> to <b>fill the gaps in the observations</b> of AR storm genesis and evolution in order to improve their predictability.
  
* <b>AR-Recon</b> is <strong>led by CW3E and the NWS/NCEP</strong>, with core partners including multiple academic institutions and:
  
  * the <strong>U.S. Navy</strong>;
  * the <strong>U.S. Airforce</strong>;
  * the <strong>National Center for Atmospheric Research (NCAR)</strong>; and
  * the <strong>European Centre for Medium Range Weather Forecasts (ECMWF)</strong>.
  
* I am a co-PI on projects in <b>collaboration with the U.S. Airforce</b>, leading efforts for the development and adoption of the novel <a href="https://www.jcsda.org" target="blank"><b>Joint Effort for Data Assimilation Integration (JEDI)</b></a> and <a href="https://ncar.ucar.edu/what-we-offer/models/model-prediction-across-scales-mpas" target="blank"><b>Model for Prediction Across Scales (MPAS)</b></a> framework.

* While the <b>JEDI Framework</b> will be adopted for operations in the future, it is still <strong>currently in a state of rapid development and extensive testing</strong>.

  * Much of the <b>research in JEDI currently is about JEDI itself</b>, understanding / improving its functionality and <strong>bringing it to the skill of legacy systems</strong>.
  
* However, there is currently a <b>major gap in open source software</b> for <strong>operating legacy data assimilation systems for benchmark studies</strong>.

========================================================
## Data assimilation as a workflow process
<div style="float:left; width:100%">
<ul>
  <li>CW3E currently has an <b>operational near-real-time ensemble forecast system</b>, and has been developing and <strong>experimental data assimilation re-forecast system</strong> based on the ensemble-forecast system.</li>
  <li> <b>Data assimilation</b> is a <strong>notoriously complex operational problem</strong>, which involves <b>interdependent steps</b> of:</li>
  <ul>
    <li><strong>procuring</strong>;</li>
    <li><strong>pre-processing</strong>;</li>
    <li><strong>generating</strong>; and</li>
    <li><strong>post-processing</strong>;</li>
    <li><b>large volumes of NWP data</b>.</li>
  </ul>
  <li>In order to <b>scale to operation</b>, data assimilation typically requires the use of a <strong>workflow manager to interface between the user's tasks and the super computer's job scheduler</strong>.</li>
  <li> From <b>Christopher Harrop (creator of Rocoto)</b>:</li>
  <div style="padding:25px;" class="fragment">
  <blockquote>
  <b>Workflow Management</b> is a concept that originated in the 1970's to handle business process management... to manage complex collections of business processes that need to be carried out in a certain way with <strong>complex interdependencies and requirements</strong>...
  </blockquote>
  </div>
  <div style="padding:25px;" class="fragment">
  <blockquote>
  ...scientific workflows are driven by the <strong>scientific data that "flows" through them</strong>... usually triggered by the availability of some kind of input data, and a task's result is usually... <b>fed as input to another task in the workflow</b>.
  </blockquote>
  </div>
  <li>The <b>complexity of data assimilation cycling</b> is demonstrated in the following <strong>data flow diagram</strong>...</li>
</div>

========================================================

<div style="float:left; width:100%">
<h3>Data assimilation in a GSI-WRF-MET Stack</h3>

</div>
<div style="float:left; width:100%; text-align:center;" class="fragment">
<img style="width:85%", src="GSI-WRF-cycling.png" alt="Diagram of data flows in GSI-WRF-cycling."/>
</div>
<div style="float:left; width:100%">
</div>


========================================================
### Data assimilation as a statistical learning problem

* My own <b>methodological framework</b> of analyzing the data assimilation problem is of a <strong>statistical learning problem</strong>.

* I need to run <b>many simulations</b> to study:
  
  * <strong>hyper-parameter sensitivity</strong> in the learning problem; and
  * to generate a <strong>statistically relevant sample size</strong> for <b>hypothesis testing and/or Bayesian modelling</b> techniques.
  
* My <b>re-forecasting workflows</b> are also <strong>non-standard</strong> from the perspective of operational forecasting;

  * rather than generating, e.g., a 10-day forecast at every zero hour, I need to run a forecast up to a <b>specific valid time</b> for verification, with <strong>varying forecast length</strong> to optimize resources.
  
* I also perform simulations on <b>multiple HPC platforms</b> with different system architectures, job schedulers and software stacks, so I need to keep my <strong>software as portable and system-agnostic as possible</strong>.

* These demands have led me to develop an experimental <a href="https://github.com/CW3E/GSI-WRF-Cycling-Template" target="blank"><b>end-to-end data assimilation cycling system</b></a> in the <strong>GSI-WRF-MET stack</strong> using the <a href="https://christopherwharrop.github.io/rocoto/" target="blank"> <b>Rocoto Workflow Manager</b></a>.

  * This builds principally on <b>CW3E's NRT and Verification Teams' Rocoto / MET workflows</b>, that provided the basis for this framework.

  * <b>Christopher Harrop</b> shared open source workflow scripts for all WRF steps, and templates for GSI integration, that are <strong>used currently at CW3E for its operational NRT products</strong>.
  
  * As a byproduct of research efforts, I have integrated these codes into a <b>unified system for case-study analysis</b>, using a <strong>Bash / Python data science stack</strong>.

========================================================

<div style="float:left; width:100%">
<h2>CW3E's Open Source Institutional Code Base</h3>
<div style="float:left; width:65%; text-align:center;" class="fragment">
<img style="width:100%", src="Github.png" alt="CW3E Github."/>
</div>
<div style="float:right; width:35%; text-align:left;" class="fragment">
<ul>
  <li>These code repositories are available on the <a href="https://github.com/CW3E" target="blank"><b>CW3E Github</b></a>.</li>
  <li>Code is <strong>licensed for reuse, redistribution and modification</strong> under the <b>Apache 2.0 Open Source License</b>.</li>
  <li>This is a <strong>permissive license</strong> that has conditions familiar to an <b>academic environment</b>:</li>
  <ul>
    <li><strong>original authors are given attribution</strong>; and</li>
    <li><strong>redistributed code includes change logs</strong>.</li>
  </ul>
  <li><b>Derived products do not need to be made open source</b>;</li>
  <ul>
    <li>this can be <strong>reused for nearly any purpose</strong> by downstream users.</li>
  </ul>
  <li>This makes these codes suitable for <b>controlled information environments</b>, while still <strong>benefiting from community interaction</strong>.</li>
</ul>
</div>
</div>

========================================================

<div style="float:left; width:100%">
  <h3>Data assimilation in a GSI-WRF-MET Stack</h3>
  <div style="float:left; width:45%; text-align:left;" class="fragment">
    <ul>
      <li>Includes an <a href="https://github.com/CW3E/GSI-WRF-Cycling-Template/blob/main/rocoto_utilities.py" target="blank"><b>IPython API for workflow commands</b></a>, and <strong>plotting results in Matplotlib</strong>.</li>
      <ul>
        <li>This is designed to <b>enable easy looping</b> of:</li>
        <ul>
          <li><strong>valid dates</strong>,</li>
          <li><strong>task indices</strong>,</li>
          <li><strong>control flows</strong>, and</li>
          <li><strong>case studies</strong>,</li>
        </ul>
        <li>as demonstrated to the right:</li>
      </ul>
    </ul>
  </div>
  <div style="float:right; width:55%; text-align:center;" class="fragment">
    <img style="width:100%", src="ipython.png" alt="Ipython API."/>
  </div>
<div style="float:left; width:45%; text-align:left;" class="fragment">
  <ul>
    <li>NOTE: there is <b>no documentation (outside of comments)</b>;</li>
    <ul>
      <li>a new version will be released ASAP, built on the <a href="https://cylc.github.io/" target="blank"><b>Cylc workflow system</b></a>.</li>
    </ul>
    <li> <b>Conversion to Cylc</b> is necessary for:</li>
    <ul>
      <li><strong>long-term support</strong>, and for</li>
      <li>developing a unified system for re-forecasting with <strong>formally "equivalent" experiments in GSI-WRF and JEDI-MPAS</strong> with verification performed on <b>common metrics in MET</b>.</li>
    </ul>
    <li>This intends to build on the open source <a href="https://github.com/NCAR/MPAS-Workflow" target="blank"><b>JEDI-MPAS workflow templates</b></a> developed at NCAR.</li>
  </ul>
</div>

========================================================


<div style="float:left; width:100%">
<h3>Data assimilation in a GSI-WRF-MET Stack</h3>
<ul>
  <li><b>Experiment settings</b> are currently <strong>configured using an XML file</strong> to instruct Rocoto as below:</li>
</ul>
<div style="float:left; width:100%; text-align:center;" class="fragment">
<img style="width:85%", src="ctr_flw_xml.png" alt="XML file controlling workflow."/>
</div>
<ul>
  <li>However, this will be <strong>replaced with an analogous YAML file</strong> for the <b>Cylc re-write</b>.</li>
</ul>
</div>


========================================================

<div style="float:left; width:100%">
<h3>Data assimilation in a GSI-WRF-MET Stack</h3>

</div>
<div style="float:left; width:100%; text-align:center;" class="fragment">
<img style="width:85%", src="GSI-WRF-cycling.png" alt="Diagram of data flows in GSI-WRF-cycling."/>
</div>
<div style="float:left; width:100%">
</div>

========================================================

<div style="float:left; width:100%">
<h3>Data assimilation in a GSI-WRF-MET Stack</h3>
<ul>
  <li>In the <b>Rocoto logs</b>, this workflow is presented in <strong>cycle order</strong> as in the following:</li>
</ul>
<div style="float:left; width:85%; text-align:center;" class="fragment">
<img style="width:100%", src="workflow0.png" alt="Rocoto logs for GSI-WRF-cycling."/>
</div>
<ul>
  <li>As a current limitation, <b>new cycles are triggered with the ad-hoc</b> `boot_next_cycle` task.</li>
  <li>This ad-hoc job was created due to cycles not triggering in Rocoto <strong>workflows containing complex, inhomogeneous cycles</strong>.</li>
  <li>This issue is planned to be <b>fixed in the Cylc re-write</b>.</li>
</ul>
</div>

========================================================

<div style="float:left; width:100%">
<h3>Data assimilation in a GSI-WRF-MET Stack</h3>
<ul>
  <li>However, this currently allows the <strong>mixing of asynchronous jobs in heterogeneous cycles</strong>, with specific settings <b>depending on the forecast zero-hour</b>.</li>
</ul>
<div style="float:left; width:85%; text-align:center;" class="fragment">
<img style="width:100%", src="workflow1.png" alt="Rocoto logs for GSI-WRF-cycling."/>
</div>
<ul>
  <li>For a <b>verification at a specified valid date</b> of `2019-02-15_00_00`, the above cycle needs a <strong>4-day forecast</strong>.</li>
  <li>However, the following cycle will only require a <strong>3-day forecast</strong>.</li>
</ul>
<div style="float:left; width:85%; text-align:center;" class="fragment">
<img style="width:100%", src="workflow2.png" alt="Rocoto logs for GSI-WRF-cycling."/>
</div>
<ul>
  <li>For <b>offline, re-forecast studies</b>, this allows significant <strong>performance optimization of the workflow</strong>, eliminating the need to call unnecessary resources.</li>
</ul>
</div>

========================================================

### Data assimilation in a GSI-WRF-MET Stack

* Each of these tasks is called as a <a href="https://github.com/CW3E/GSI-WRF-Cycling-Template/tree/main/scripts/drivers" target="blank"><b>scripted job</b></a>, with <strong>run-time settings defined by the cycling workflow</strong>.

  * These scripts are <b>workflow manager agnostic</b>, as they simply require one's workflow to <strong>export Bash variables at run-time</strong>.

  * These scripts have been <strong>homogenized to handle the data flows</strong> with <b>switches to determine sources of data</b>.
  
* E.g., the <a href="https://github.com/CW3E/GSI-WRF-Cycling-Template/blob/main/scripts/drivers/wrf.sh" target="blank"><b>WRF driver script</b>, `wrf.sh`,</a> runs differently depending on whether it is:
  
    * a <strong>fresh forecast</strong> down-scaling a global background model;
    * a forecast with initial conditions generated from a <strong>data assimilation cycle</strong>; or
    * a <strong>restart run</strong> from a previous 6-hour, 1-way nested run, generating an extended forecast.

* Currently, <b>experiments are organized in a case study / control flow hierarchy</b>:

  * one will <strong>name the case study</strong> under consideration, and
  * define a <strong>control flow name with all tuned settings</strong>, e.g., for the data assimilation method, WRF tunings, etc.

* All associated settings are written to a <a href="https://github.com/CW3E/GSI-WRF-Cycling-Template/tree/main/simulation_settings/archive/case_examples" target="blank"><b>static directory</b></a> which is <b>sourced by the Rocoto workflow</b>;

  * this is designed so that <strong>all tuned settings are centrally archived</strong> for <b>case study / configuration reproducibility</b>.

========================================================
## MET Verification of 2022-2023 AR Season

* <b>MET forecast verification</b> is a key aspect of this workflow used to <strong>objectively assess forecast skill</strong>.

* We shift focus now to the <a href="https://github.com/CW3E/MET-tools" target="blank"><b>MET verification tools</b></a> in this workflow with the <b>2022 - 2023 AR Season</b> as a <strong>highly applicable use-case</strong> for these codes.

* This is a perfect example of where one needs to <b>analyze data from multiple</b>:

  * <strong>valid dates</strong>;
  * <strong>forecast leads</strong>;
  * <strong>models</strong>; and
  * <strong>sub-domains</strong>.

* <b>Batch processing</b> all this data is a non-trivial task, as a workflow should:
  
  * <strong>handle maps of hyper-parameter configurations</strong>,
  * <strong>systematically organize outputs</strong>,
  * be <strong>robust to missing data</strong> in the workflow stream,
  * perform <strong>error checks and exception handling</strong>,
  * generate <strong>traceable logs for debugging</strong>,
  * <strong>automate plotting axes / labels / legends</strong>, and
  * require <strong>minimal hard-coded configurations</strong>.

* This problem arises frequently with <b>tuning the GSI-WRF-Cycling-Template</b>.

========================================================

<h2>Output Directory Organization</h2>

<div style="float:left; width:100%; text-align:center;">
  <div style="float:left; width:25%;" class="fragment">
    <img style="width:100%" src="top_dir.png" alt="Output directory tree."/>
  </div>
  <div style="float:left; width:25%;" class="fragment">
   <img style="width:100%" src="figs.png" alt="Output directory tree."/>
  </div>
  <div style="float:left; width:25%;" class="fragment">
    <img style="width:100%", src="NRT_ecmwf.png" alt="Output directory tree."/>
  </div>
  <div style="float:left; width:25%;" class="fragment">
    <img style="width:100%" src="NRT_gfs.png" alt="Output directory tree."/>
  </div>
</div>

========================================================

<h2>Multidate / Multilead Heatplot Templates</h2>

<div style="float:left; width:110%; text-align:center;">
  <div style="float:left; width:50%;" class="fragment">
    <img style="width:100%" src="rmse_heatplot.png" alt="CW3E Github."/>
  </div>
  <div style="float:left; width:50%;" class="fragment">
   <img style="width:100%" src="fss_heatplot.png" alt="CW3E Github."/>
  </div>
</div>
<div style="float:left; width:100%;">
  <ul>
    <li><b>Grid-Stat outputs</b> are parsed, filtered and converted into <a href="https://pandas.pydata.org/" target="blank"><b>Pandas dataframes for plotting and diagnostics</b></a>.</li>
    <li>Templates are designed for <strong>multidate / multilead heatplots</strong> for diagnostics over <b>ranges of valid dates</b>.</li>
    <li><b>Missing / erroneous data</b> is <strong>filtered by the workflow post-processing routines</strong>.</li>
  </ul>
</div>

========================================================

<h2>Multi-lead Lineplot Templates</h2>

<div style="float:left; width:110%; text-align:center;">
  <div style="float:left; width:50%;" class="fragment">
    <img style="width:100%" src="rmse_lineplot.png" alt="CW3E Github."/>
  </div>
  <div style="float:left; width:50%;" class="fragment">
   <img style="width:100%" src="fss_lineplot.png" alt="CW3E Github."/>
  </div>
</div>
<div style="float:left; width:100%">
  <ul>
    <li>Templates are designed for <strong>multilead / multimodel / multidomain lineplots</strong> for diagnostics for <b>particular valid dates</b>.</li>
    <li><b>Axes scale</b> depending on the available forecast data, and plot configurations with <strong>different lead hours together</strong>.</li>
    <li>These templates are designed for <b>batch analysis of large hyper-parameter grids</b>.</li>
    <li>New tools and templates are under <b>continuous development</b>, with <strong>research tools polished for re-use incrementally</strong>.</li>
  </ul>
</div>

========================================================
## Conclusions

* This is an ongoing <strong>research-to-operation project at CW3E</strong>, to generate open source tools for both purposes.

* This <b>benefits from community interaction</b>, especially with <strong>collaboration with the NRT and Verification Teams</strong> on on workflow and research tool development.

  * However, this also <b>supports scientific objectives</b> for specific projects that are performed in <strong>controlled information environments</strong>.
  
* As such, this <b>infrastructure project</b> presents <strong>opportunities for wider collaboration</strong> where scientific dissemination may be restricted.

  * This infrastructure talk highlights some of the <strong>benefits and flexibility</strong> of an <b>open source model</b> for infrastructure development.

* Folks who are interested in collaborating on these tools are <b>encouraged to reach out</b>,
  
  * more users of the same code leads to <strong>more bug-fixes and development scalability</strong>.
  
* A late colleague of mine from when I was a postdoc in Norway, <b>Yongqi Gao</b>, liked to reference a proverb that is <strong>applicable to open source development</strong>:

  <blockquote>
  "If you want to go fast, go yourself. <b>If you want to go far, go together</b>".
  </blockquote>
  
<div style="float:left; width:100%; text-align:center; padding-top:100px" class="fragment">
  <b style="font-size:80px;">Thank you!</b>
</div>
