---

title: Lesson 1 - Basic Concepts
layout: default
permalink: /hnc/lessons/1/
    
slideslink: https://docs.google.com/presentation/d/1xYadXg_tskYnWMLbuM9mcF7JaQKVGgBmVIpM2TWEMkE/export/pdf

resourcetitle: Lesson Resources
resource1: |
    <li>You can download the source code for our sample website (gjlandscapemaintenance.co.uk) here | <a href="/assets/hnc/hnc-sample-site-lesson1.zip">Download code</a></li>
    <br/>
    <ul>
      <li> -- Unzip the folder</li>
      <br/>
      <li> -- Open the file index.html in your browser.</li>
      <br/>
      <li> -- Also open it in a text editor.</li>
      <br/>
      <li> -- See if you can match up the parts with the site. Is anything unclear?</li>
    </ul>
resource2: |
  <li>Before continuing, make sure you have followed the instructions for creating a Github account from Lesson 0. | <a href="/hnc/lessons/0/index.html#github">Instructions</a></li>
  <br/>
  <ul>
    <li> -- Go to your profile on Github, and click the Repositories tab.</li>
    <br/>
    <li> -- Click New.</li>
    <br/>
    <li> -- For the repository name, enter exactly <em>username.github.io</em> where username is your Github username.</li>
    <br/>
    <li> -- Give a description. Something like 'Repo for my personal webpage'.</li>
    <br/>
    <li> -- Leave the repo as public.</li>
    <br/>
    <li> -- Click Create Repository.</li>
    <br/>
    
    <li> -- Once the repository is created, click <em>Create a new file</em> and call it index.html.</li>
    <br/>
    <li> -- In the file, write <br/>
    <div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="s">Hello world</span></code></pre></div>
    </li>
    <li> -- Commit the file, leaving a message explaining what you did. Something like 'Created index file' is good enough.</li>
    
    <br/>
    <li> -- Go back to the main page of your repository <em>username.github.io</em></li>
    <br/>
    <li> -- Click the Settings tab.</li>
    <br/>
    <li> -- Scroll down to the Github Pages section and click None.</li>
    <br/>
    <li> -- Select master and click save.</li>
    <br/>
    <li> -- Wait a few moments and then go to https://username.github.io</li>
    <br/>
    <li> -- You should see your website!</li>
  </ul>
  
quicklinks: |
  <h4>Quick Links:</h4>
  <ul>
    <li>BTEC Higher Nationals - Computing | <a href="/hnc">Homepage</a> | <a href="/hnc/lessons/0/">Lesson 0 - Introduction</a></li>
    <li><a href="/contact">Contact Me</a></li>
  </ul> 

---

{% for block in site.data.common_lessons %}
  {% if block.common == 'yes' %}
  <h4 id="{{ block.idtag }}">{{ block.blockname }}:</h4>
  <ul>
    {{ block.blocktext | replace: 'slidesurl', page.slideslink}}
  </ul>
  <br/>
  {% endif %}
{% endfor %}

<h4>{{ page.resourcetitle }}:</h4>
<ul style="list-style-type:disc;">
  {{ page.resource1 }}
  <br/>
  <center><p>- - - - - - - - - - - - - - - - - -</p></center>
  <br/>
  {{ page.resource2 }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
