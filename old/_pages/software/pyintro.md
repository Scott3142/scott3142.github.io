---

title: Intorduction to Python
layout: default
permalink: /software/pyintro.html

hero: You will need to download and familiarise yourselves with some software if you are to continue with this course. Below are instructions on which resources we will use and what you should download.</p><p>(adapted from <a href="http://vknight.org/cfm/labsheets/01-variables-conditionals-loops/" target="_blank">here</a>)

---

<p>{{ page.hero }}</p>
<br/>

{% for block in site.data.common_lessons %}
  {% if block.softwareshow != 'no' %}
  <h4 id="{{ block.idtag }}">{{ block.blockname }}:</h4>
  <ul>
    {{ block.blocktext }}
  </ul>
  <br/>
  {% endif %}
{% endfor %}
<br/>
