---
title: BTEC Technicals
coursename: Digital Applications Development
layout: default
year: 2017/2018
permalink: /btec/index.html

hero: This page relates to the <em>BTEC Technicals</em> course <em>Digital Applications Development</em> running at Bridgend College during the academic year 2017/2018. Course notes and program files will be available to download here and will be updated as new material is added. Comments and questions welcome at any time.

contact: The main point of contact for all questions relating to this course will be <a href="/contact" target="_blank">Scott Morgan</a> (<a href="mailto:MorganSN@cardiff.ac.uk" target="_blank">MorganSN@cardiff.ac.uk</a>). Support will be provided via e-mail or during class.
---

<p>{{ page.hero }}</p>
<br/>

<h4>Lessons ({{ page.coursename }}):</h4>
<ul>
  {% for lesson in site.data.btec.lessons %}
    <li><a href="{{ lesson.url }}"><em>{{ lesson.text }}</em></a></li>
  {% endfor %}
</ul> 
<br/>

<h4>Quick Links:</h4>
<ul>
  {% for link in site.data.btec.links %}
    <li><a href="{{ link.url }}" target="_blank"><em>{{ link.text }}</em></a></li>
  {% endfor %}
</ul>
<br/>

<h4>Timetable ({{ page.year }}):</h4>
<ul>
  {% for ttable in site.data.btec.timetable %}
    <li><em>Group {{ ttable.group }}: {{ ttable.day }} ({{ ttable.time }}) - {{ ttable.location }}</em></li>
  {% endfor %}
</ul>
<br/>

<h4>Contact Info:</h4>
<ul>
  <li>{{ page.contact }}</li>
</ul>
