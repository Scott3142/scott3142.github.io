---

title: Lesson 7 - Assignment Example Presentations
layout: default
permalink: /hnc/lessons/7/
    
slideslink: https://docs.google.com/presentation/d/1tmPAU0tQB0iDeSPXAyFKsVqUQ8x9KbUSx8vF9qPhG8A/export/pdf
fileslink: https://docs.google.com/presentation/d/1qxgPB77tw6QB5vSE4K-rliPoKH5d9wvFPa7Nq1cdFEo/export/pdf

resourcetitle: Lesson Resources
hero: Below are two example presentations, similar to that which you have been asked to do for your assignment. One would be much better than the other. Neither are designed to be perfect!!
resource1: <center><a href="https://docs.google.com/presentation/d/1tmPAU0tQB0iDeSPXAyFKsVqUQ8x9KbUSx8vF9qPhG8A/export/pdf" target="_blank" class="btn btn-ghost">Example Presentation 1</a></center>
resource2: <center><a href="https://docs.google.com/presentation/d/1qxgPB77tw6QB5vSE4K-rliPoKH5d9wvFPa7Nq1cdFEo/export/pdf" target="_blank" class="btn btn-ghost">Example Presentation 2</a></center>
  
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
  {{ page.hero }}
  <br/>
  {{ page.resource1 }}
  <br/>
  {{ page.resource2 }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
