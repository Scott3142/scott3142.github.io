---

title: Lesson 4 - Design
layout: default
permalink: /btec/lessons/4/
    
slideslink: https://docs.google.com/presentation/d/1mTJMArn6F6GFefTKCfcXHOoKU7Yteg0bLEj3TEuDoZk/export/pdf

resourcetitle: Lesson Resources
resource: <center><a href="https://app.moqups.com/scott.morgan3142@gmail.com/3DCXzWsOoQ/view/page/aa9df7b72" class="btn btn-ghost" target="_blank"><em>Moqup</em> Example</a></center>

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
