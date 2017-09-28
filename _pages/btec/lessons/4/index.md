---

title: Lesson 4 - Design
layout: default
permalink: /btec/lessons/4/
    
slideslink: 

resourcetitle: Lesson Resources
resource: |
  <li>The following files will help you with this class:</li>
  <br/>
  <ul>
    <li>None yet!</li>
  </ul>

quicklinks: |
  <h4>Quick Links:</h4>
  <ul>
    <li>BTEC Technicals | <a href="/btec/">Homepage</a> | <a href="/btec/lessons/0/">Lesson 0 - Introduction</a></li>
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
<ul>
  {{ page.resource }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
