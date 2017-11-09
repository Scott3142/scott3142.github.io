---

title: Lesson 6 - Assignment
layout: default
permalink: /hnc/lessons/6/
    
slideslink: https://docs.google.com/presentation/d/1mZ7Yny-_FtMS0-SWk2-jfkSWaHNHOZqEQgsCEuFgpEQ/export/pdf
fileslink: https://docs.google.com/document/d/15C5Dno3KuHrt2uTKyiQkNXqn-7BY6vkMkJHeOadQPR8/edit?usp=sharing

resourcetitle: Lesson Resources
resource1: <center><a href="https://docs.google.com/document/d/197Gae0uZTyUY6bkJjZh0LsGjUoCA5AIKHUPEoCyBnAA/edit?usp=sharing" target="_blank" class="btn btn-ghost">Assignment 1</a></center>
resource2: <center><a href="https://docs.google.com/document/d/15C5Dno3KuHrt2uTKyiQkNXqn-7BY6vkMkJHeOadQPR8/edit?usp=sharing" target="_blank" class="btn btn-ghost">Hints & Tips</a></center>
  
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
  {{ page.resource2 }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
