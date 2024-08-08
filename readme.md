<h1>Network Analysis</h1>
<p>Network analysis is the process of investigating social structures through the use of networks and graph theory. It characterizes networked structures in terms of nodes (individual actors, people, or things within the network) and the ties, edges, or links (relationships or interactions) that connect them. Examples of social structures commonly visualized through social network analysis include social media networks, memes spread, and information transfer.</p>
<p>This course is part of Master degree in Computer Science (Software & Security Engineering) at University of Genoa.</p>
<p>Course Instructor: Prof. <a href="https://www.linkedin.com/in/marina-ribaudo-434aa32/">Marina Ribaudo</a></p>

<h2>Course Objectives</h2>
<p>In this course, we have learned the fundamental concepts of network analysis, including:</p>
<ul>
  <li>Graph theory and its applications in network analysis</li>
  <li>Different types of networks (e.g., social networks, information networks)</li>
  <li>Methods for analyzing network structures and properties</li>
  <li>Tools (such as Gephi for visualization) and software used for network analysis</li>
  <li>Case studies and practical applications of network analysis</li>
</ul>
<h2>Practical Assignments</h2>
<p>Throughout the course, we have completed three different practical assignments to apply the concepts learned in class. These assignments have included:</p>
<h3>Assignment 1: Data Analysis with Python</h3>
<h4>Objective:</h4>
<p>Perform data analysis using Python libraries such as Pandas, Numpy, and Matplotlib.</p>
<h4>Tasks:</h4>
<ol>
<li><b>Data Cleaning</b></li>
<ul>
<li>Load the dataset.</li>
<li>Calculating the giant component.</li>
<li>Data normalization.</li>
</ul>

<li><b>Exploratory Data Analysis (EDA)</b></li>
<ul>
<li>Generate summary statistics.</li>
<li>Create visualizations (e.g., histograms, scatter plots) to understand data distributions and relationships.</li>
</ul>

<li><b>Data Transformation</b></li>
<ul>
<li>Apply necessary transformations (e.g., log transformation, scaling).</li>
<li>Create new features if needed.</li>
</ul>

<li><b>Reporting</b></li>
<ul>
<li>Summarize findings and insights.</li>
<li>Include visualizations and model performance metrics in the report.</li>
</ul>

</ol>

<h4>Files:</h4>
<ul>
<li><b><a href="https://github.com/parsamlm/NetworkAnalysis/blob/main/Step%201/measures_computation.ipynb">measure_computation.ipynb:</a></b> Main python notebook file which consists of the whole logic.</li>
<li><b><a href="https://github.com/parsamlm/NetworkAnalysis/blob/main/Step%201/report.pdf">report.pdf:</a></b> This file includes the insights and understandings of the network.</li>
</ul>

<h3>Assignment 2: Information broadcasting</h3>
<h4>Objective:</h4>
<p>In this assignment, we have explored how the network behavior when there is a data that is needed to be shared.</p>

<h4>Tasks:</h4>
<p>We have developed several nodes designed to transmit data, some of which will modify the data. Ultimately, the data will be disseminated within the network of Twitter's Circles.</p>

<h4>Files:</h4>
<ul>
<li><b><a href="https://github.com/parsamlm/NetworkAnalysis/blob/main/Step%202/sending_info.ipynb">sending_info.ipynb:</a></b> Main python notebook file which consists of the whole logic.</li>
<li><b><a href="https://github.com/parsamlm/NetworkAnalysis/blob/main/Step%202/report.pdf">report.pdf:</a></b> This file includes the insights and understandings of the network.</li>
</ul>


<h3>Assignment 3: Network Robustness</h3>
<h4>Objective:</h4>
<p>Investigate the robustness of a network by analyzing its structural properties and simulating failures.</p>
<p>In this assignment, we had three different parts:</p>
<ol>
<li><b>Step 1:</b> Apply some simulated attacks on two random networks (Erdos-Renyi & Barabasi-Albert) to see how they affect the network robustness. The attacks are listed below:</li>
<ul>
<li>Highest Degree Node Removal Attack</li>
<li>Highest Betweenness Node Removal Attack</li>
<li>Highest PageRank Node Removal Attack</li>
<li>Random Node Removal Attack</li>
</ul>
<li><b>Step 2:</b> Apply the mentioned attacks (except Highest Betweenness Node Removal Attack) on the network of Twitter's Circles.</li>
<li><b>Step 3:</b> After finding the most effective attack on the Twitter's Circles network, we have worked on making an improvement of network's robustness.</li>
</ol>
<h4>Files:</h4>
<ul>
<li><b><a href="https://github.com/parsamlm/NetworkAnalysis/blob/main/Step%203/helper.py">helper.py:</a></b> This python file includes the simulated attacks' functions.</li>
<li><b><a href="https://github.com/parsamlm/NetworkAnalysis/blob/main/Step%203/network_robustness.ipynb">network_robustness.ipynb:</a></b> Main python notebook file which consists of the whole logic.</li>
<li><b><a href="https://github.com/parsamlm/NetworkAnalysis/blob/main/Step%203/report.pdf">report.pdf:</a></b> This file includes the insights and understandings of the network.</li>
</ul>

<h2>Data</h2>
<p>The data which is Twitter's Circles is downloaded from <a href="https://snap.stanford.edu/data/egonets-Twitter.html">Stanford</a> website.</p>
