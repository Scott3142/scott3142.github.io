---
title: Outreach
layout: default
permalink: /outreach/

hero: Over the past few years I have been involved in a number of outreach and schools engagement events both through Cardiff University and Bridgend College and this page details a few of these projects - if you are interested in finding out more about my outreach work, please <a href="/contact">get in touch</a>!

---

<p>{{ page.hero }}</p><br>

<center><h4>Projects</h4></center><br>
<ul>
  {% for event in site.data.outreach %}
    <li><b style="font-weight:bold;">{{ event.title }}</b> | <em>{{ event.institution }}</em> <em>({{ event.year }})</em> {{ event.extra }}</li>
    <ul><br>
      <li>{{ event.description }}</li> {%if event.partners %}<br>
      <li><b style="font-weight:bold;">Partners:</b> {{ event.partners }} </li>{% endif %}
    </ul>
    <br><br>
   {% endfor %}
</ul>

<br>

<center><h4>Outreach Funding</h4><br>
<ul>
  {% for fund in site.data.funding %}
    {% if fund.type contains "outreach" %}
      <li>{{ fund.amount }} {{ fund.duration }} | <em>{{ fund.title }} ({{ fund.year }})</em></li><br/>
    {% endif %}
  {% endfor %}
</ul></center>

<br/>

<center><h4>Notable Contributions</h4></center><br>
<ul>
  {% for contribution in site.data.contributions %}
    {% if contribution.type contains "outreach" %}
      <li>{{ contribution.title }} | <em>{{ contribution.institution }} {{ contribution.year }}</em></li>
      <ul>
        <li>{{ contribution.description }}</li><br/>
      </ul>
    {% endif %}
  {% endfor %}
</ul>