---

title: Lesson 0 - Introduction
layout: default
permalink: /hnc/lessons/0/

hero: You will need to download and familiarise yourselves with some software if you are to continue with this course. Below are instructions on which resources we will use and what you should download.</p><p>(adapted from <a href="http://vknight.org/cfm/labsheets/01-variables-conditionals-loops/" target="_blank">here</a>)
    
slideslink: https://docs.google.com/presentation/d/1T8QFNxsnDENPqWjo5lABjKcEHENp_4v1tNL_WK4AZ9M/export/pdf

fileslink: /assets/hnc/0.zip

diagnostic: https://docs.google.com/forms/d/e/1FAIpQLSdhsqomfk3uY7xQh6G_khFeuy4TH-wN35P-TD3N70amCcrIsw/viewform?usp=sf_link

---

<p>{{ page.hero }}</p>
<br/>

{% for block in site.data.common_lessons %}
  {% if block.hncshow != 'no' %}
  <h4 id="{{ block.idtag }}">{{ block.blockname }}:</h4>
  <ul>
    {{ block.blocktext | replace: 'slidesurl', page.slideslink | replace: 'filesurl', page.fileslink | replace: 'diagnosticurl', page.diagnostic}}
  </ul>
  <br/>
  {% endif %}
{% endfor %}

<br/>
