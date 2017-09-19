---
title: BTEC Higher Nationals
coursename: Website Design &amp; Development
layout: default
year: 2017/2018
permalink: /hnc/index.html

hero: This page relates to the <em>BTEC Higher Nationals</em> course <em>Website Design &amp; Development</em> course running at Bridgend College during the academic year 2017/2018. Course notes and program files will be available to download here and will be updated as new material is added. Comments and questions welcome at any time.

contact: The main point of contact for all questions relating to this course will be <a href="/contact" target="_blank">Scott Morgan</a> (<a href="mailto:MorganSN@cardiff.ac.uk" target="_blank">MorganSN@cardiff.ac.uk</a>). Support will be provided via e-mail or during class.
---

<p>{{ page.hero }}</p>
<br/>

<h4>Lessons ({{ page.coursename }}):</h4>
<ul>
  {% for lesson in site.data.hnc.lessons %}
    <li><a href="{{ lesson.url }}"><em>{{ lesson.text }}</em></a></li>
  {% endfor %}
</ul> 
<br/>

<h4>Resources &amp; Useful Links:</h4>
<ul>
  <li>Web Development Related:</li>
  <ul>
    {% for resource in site.data.teaching_resources.hnc %}
      <li><a href="{{ resource.url }}" target="_blank"><em>{{ resource.text }}</em></a></li>
    {% endfor %}
  </ul>
  <br/>
  <li>General:</li>
  <ul>
    {% for resource in site.data.teaching_resources.common %}
      <li><a href="{{ resource.url }}" target="_blank"><em>{{ resource.text }}</em></a></li>
    {% endfor %}
  </ul>
</ul>
<br/>

<h4>Quick Links:</h4>
<ul>
  {% for link in site.data.hnc.links %}
    <li><a href="{{ link.url }}" target="_blank"><em>{{ link.text }}</em></a></li>
  {% endfor %}
</ul>
<br/>

<h4>Timetable ({{ page.year }}):</h4>
<ul>
  {% for ttable in site.data.hnc.timetable %}
    <li><em>{{ ttable.day }} ({{ ttable.time }}) - {{ ttable.location }}</em></li>
  {% endfor %}
</ul>
<br/>

<h4>Contact Info:</h4>
<ul>
  <li>{{ page.contact }}</li>
</ul>
