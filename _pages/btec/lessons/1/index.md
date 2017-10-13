---

title: Lesson 1 - Basic Concepts
layout: default
permalink: /btec/lessons/1/
    
slideslink: https://docs.google.com/presentation/d/1dYJlTVp7HsP3RZLejXqrP4c_5B8Hg4P9u2QbhsYQnC0/export/pdf
fileslink: /assets/btec/1.zip

resourcetitle: Lesson Resources
resource: |
  <li>Before downloading the files, make sure you have followed the instructions for downloading and installing installing MIT App Inventor Companion from Lesson 0. | <a href="/btec/lessons/0/index.html#android">Instructions</a></li>
  <br/>
  <ul style="list-style-type:disc">
    <li>We will be using pre-prepared app code to introduce some basic concepts about app development, building on Lesson 0. | <a href="/code/HelloWorld.aia">Download app files</a></li>
    <br/>
    <li>Unzip the downloaded file and save the contents somewhere sensible.</li>
    <br/>
    <li>Navigate to <a href="http://appinventor.mit.edu/explore/" target="_blank">MIT App Inventor</a> in your browser.</li>
    <br/>
    <li>Click Create apps! in the top right hand corner.</li>
    <br/>
    <li>Click Projects in the navigation bar and click 'Import project from my computer (.aia). Select the file that you downloaded.</li>
    <br/>
    <li>Click Connect -> Emulator in the toolbar. If you get an error at this step, make sure you have followed the instructions <a href="http://appinventor.mit.edu/explore/ai2/windows.html" target="_blank">here</a>.</li>
    <ul>
      <li><em>You may have to update some software on the emulator at this stage. Accept the updates and follow the instructions.</em></li>
    </ul>
    <br/>
  </ul>
  <li>Congratulations! You have just created an app!</li>

quicklinks: |
  <h4>Quick Links:</h4>
  <ul>
    <li>BTEC Firsts | <a href="/btec/">Homepage</a> | <a href="/btec/lessons/0/">Lesson 0 - Introduction</a></li>
    <li><a href="/contact">Contact Me</a></li>
  </ul> 

---

{% for block in site.data.common_lessons %}
  {% if block.common == 'yes' %}
  <h4 id="{{ block.idtag }}">{{ block.blockname }}:</h4>
  <ul>
    {{ block.blocktext | replace: 'slidesurl', page.slideslink | replace: 'filesurl', page.fileslink }}
  </ul>
  <br/>
  {% endif %}
{% endfor %}

<h4>{{ page.resourcetitle }}:</h4>
<ul>
  {{ page.resource }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
