---
title: BTEC Firsts
coursename: Mobile Apps Development
layout: default
year: 2017/2018
permalink: /btec/index.html

hero: |
  This page relates to the <em>BTEC Firsts</em> course <em>Mobile Apps Development</em> running at Bridgend College during the academic year 2017/2018. Course notes and program files will be available to download here and will be updated as new material is added. Comments and questions welcome at any time. <em>N.B. The first 4 lessons relate to a former course - BTEC Technicals Level 2: Digital Applications Development.</em>

contact: The main point of contact for all questions relating to this course will be <a href="/contact" target="_blank">Scott Morgan</a> (<a href="mailto:smorgan@bridgend.ac.uk" target="_blank">smorgan@bridgend.ac.uk</a>). Support will be provided via e-mail or during class.
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

<h4>Templates and Examples:</h4>
<ul style="margin-top:3%;">
  {% for template in site.data.teaching_resources.templates %}
    {% if template.course contains "btec" %}
      <center><a href="{{ template.url }}" class="btn btn-ghost" target="_blank">{{ template.text }}</a></center>
    {% endif %}
  {% endfor %}
</ul>
<br/>

<h4>Resources &amp; Useful Links:</h4>
<ul>
  <li>App Development Related:</li>
  <ul>
    {% for resource in site.data.teaching_resources.btec %}
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

