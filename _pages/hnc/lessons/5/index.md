---

title: Lesson 5 - Search Engine Optimisation
layout: default
permalink: /hnc/lessons/5/
    
slideslink: https://docs.google.com/presentation/d/18to-5XWerZrS5yIetzFZrXl7BaVSudATinlDSZptKdc/export/pdf

resourcetitle: Lesson Resources
resource1: <a href="https://moz.com/beginners-guide-to-seo" target="_blank" class="btn btn-ghost">Beginners' Guide to SEO</a>
  
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
