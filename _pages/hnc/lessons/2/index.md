---

title: Lesson 2 - Servers and Hosting
layout: default
permalink: /hnc/lessons/2/
    
slideslink: https://docs.google.com/presentation/d/1eKLDv6LsBv0Me3HaVnPnhBbizXLVVV5LCPh574bbLP8/export/pdf

fileslink: /assets/hnc/2.zip

resourcetitle: Lesson Resources
resource1: |
  <li>The following files will help you with this class:</li>
  <br/>
  <ul>
    <li><li><center><a href="/assets/hnc/2/hnc-sample-site-lesson2.zip" target="_blank" class="btn btn-ghost">Download Sample Site</a></center></li></li>
  </ul>
  
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
    {{ block.blocktext | replace: 'slidesurl', page.slideslink | replace: 'filesurl', page.fileslink }}
  </ul>
  <br/>
  {% endif %}
{% endfor %}

<h4>{{ page.resourcetitle }}:</h4>
<ul>
  {{ page.resource1 }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
