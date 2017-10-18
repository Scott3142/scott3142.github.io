---

title: Lesson 2 - Content Management Systems
layout: default
permalink: /apps/lessons/2/
    
slideslink: https://docs.google.com/presentation/d/1etWUYrbbAR0sxFlkUj3dzrkd5DdFFKghySGqmG2wDQ0/export/pdf
fileslink: /assets/apps/2.zip

resourcetitle: Lesson Resources
resource: |
  <li>Before downloading the app files, make sure you have followed the instructions for creating an MIT App Inventor App from Lesson 1. | <a href="/apps/lessons/1/">Instructions</a></li>
  <br/>
  <ul>
    <li>Here is the example app which displays the current date and time. Play around with the code and make sure you understand what does what. Remember Read-Search-Ask! | <a href="/code/DateAndTime.aia" target="_blank">Download Code</a></li>
  </ul>

quicklinks: |
  <h4>Quick Links:</h4>
  <ul>
    <li>BTEC Technicals | <a href="/apps/">Homepage</a> | <a href="/apps/lessons/0/">Lesson 0 - Introduction</a></li>
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
