---

title: Lesson 8 - HTML and CSS
layout: default
permalink: /hnc/lessons/8/
    
slideslink: https://docs.google.com/presentation/d/1tiLlsGUOpITnvU9s9YzZD0xJofumewUYxUBj4pQD9zo/export/pdf
fileslink: https://docs.google.com/presentation/d/1tiLlsGUOpITnvU9s9YzZD0xJofumewUYxUBj4pQD9zo/export/pdf

resourcetitle: Lesson Resources
hero: Below are some useful links for startying off with HTML and CSS. I <em>strongly</em> recommend working through the W3C tutorials, as they are some of the best around.<br/>
resource1: <center><a href="https://www.w3schools.com/" target="_blank" class="btn btn-ghost">W3Schools</a></center><br/><center><a href="https://learn.shayhowe.com/html-css/" target="_blank" class="btn btn-ghost">HTML &amp; CSS Tutorial</a></center><br/><center><a href="https://www.codecademy.com/en/tracks/web" target="_blank" class="btn btn-ghost">Codecademy</a></center><br/><center><a href="https://www.khanacademy.org/computing/computer-programming/html-css" target="_blank" class="btn btn-ghost">Khan Academy</a></center>
resource2: This is a tool for creating wireframes of site without any code. This will be useful for your site design.<br/> <center><a href="https://moqups.com/" target="_blank" class="btn btn-ghost">Moqup</a></center>
  
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
    {{ block.blocktext | replace: 'slidesurl', page.slideslink | replace: 'filesurl', page.fileslink}}
  </ul>
  <br/>
  {% endif %}
{% endfor %}

<h4>{{ page.resourcetitle }}:</h4>
<ul style="list-style-type:disc;">
  {{ page.hero }}
  <br/>
  {{ page.resource1 }}
  <br/>
  {{ page.resource2 }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
