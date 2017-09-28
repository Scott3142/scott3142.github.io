---

title: Lesson 0 - Introduction
layout: default
permalink: /btec/lessons/0/

hero: You will need to download and familiarise yourselves with some software if you are to continue with this course. Below are instructions on which resources we will use and what you should download.</p><p>(adapted from <a href="http://vknight.org/cfm/labsheets/01-variables-conditionals-loops/" target="_blank">here</a>)
    
slideslink: https://docs.google.com/presentation/d/1fwrgcWGKFWEBcG_7cvWVXd3u40fIQP8XqWheDiwGZLk/export/pdf

fileslink: /assets/btec/0.zip

diagnostic: https://docs.google.com/forms/d/e/1FAIpQLSetPFHIrd_JR0GectsKPU794i4l3JD6d3JU0YYIFngxHtusUA/viewform?usp=sf_link

---

<p>{{ page.hero }}</p>
<br/>

{% for block in site.data.common_lessons %}
  {% if block.btecshow != 'no' %}
  <h4 id="{{ block.idtag }}">{{ block.blockname }}:</h4>
  <ul>
    {{ block.blocktext | replace: 'slidesurl', page.slideslink | replace: 'filesurl', page.fileslink | replace: 'diagnosticurl', page.diagnostic }}
  </ul>
  <br/>
  {% endif %}
{% endfor %}
<br/>
