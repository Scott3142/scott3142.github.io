---
title: WJEC A-Level Further Mathematics
coursename: Further Mathematics
layout: default
year: 2018
permalink: /fmsp/index.html

hero: This page relates to the <em>Further Mathematics Support Programme</em> course <em>WJEC A-Level Further Mathematics</em> running at Cardiff University during 2018. Course notes and program files will be available to download here and will be updated as new material is added. Comments and questions welcome at any time.

contact: The main point of contact for all questions relating to this course will be <a href="/contact" target="_blank">Scott Morgan</a> (<a href="mailto:MorganSN@cardiff.ac.uk" target="_blank">MorganSN@cardiff.ac.uk</a>). Support will be provided via e-mail or during class.
---

<p>{{ page.hero }}</p>
<br/>

<h4>Lessons:</h4>
<ul>
  {% for lesson in site.data.fmsp.lessons %}
    <li><a href="{{ lesson.url }}"><em>{{ lesson.text }}</em></a></li>
  {% endfor %}
</ul>
<br/>

<h4>Resources &amp; Useful Links:</h4>
<ul>
  {% for resource in site.data.teaching_resources.fmsp %}
    <li><a href="{{ resource.url }}" target="_blank"><em>{{ resource.text }}</em></a></li>
  {% endfor %}
</ul>
<br/>

<h4>Quick Links:</h4>
<ul>
  {% for link in site.data.fmsp.links %}
    <li><a href="{{ link.url }}" target="_blank"><em>{{ link.text }}</em></a></li>
  {% endfor %}
</ul>
<br/>

<h4>Timetable:</h4>
<ul>
  {% for ttable in site.data.fmsp.timetable %}
    <li><em>{{ ttable.day }} ({{ ttable.time }}) - {{ ttable.location }}</em></li>
  {% endfor %}
</ul>
<br/>

<h4>Contact Info:</h4>
<ul>
  <li>{{ page.contact }}</li>
</ul>
