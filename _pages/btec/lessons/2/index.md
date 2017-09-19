---

title: Lesson 2 - Programming
layout: default
permalink: /btec/lessons/2/
    
slideslink: https://docs.google.com/presentation/d/1etWUYrbbAR0sxFlkUj3dzrkd5DdFFKghySGqmG2wDQ0/export/pdf

resourcetitle: Lesson Resources
resource: |
  <li>Before downloading the notebook, make sure you have followed the instructions for installing Python and opening a Jupyter notebook from Lesson 0. | <a href="/btec/lessons/0/index.html#jupyter">Instructions</a></li>
  <br/>
  <ul>
    <li>We will be using a pre-prepared notebook to introduce some basic Python concepts, building on Lesson 0. | <a href="/code/python2.ipynb">Download notebook</a></li>
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
