---
title: Introduction to Matlab
layout: default
permalink: /ugmatlab/

hero: This page relates to the <em>Introduction to Matlab</em> course running at Cardiff School of Maths since 2016. Course notes and program files are currently available to download via the repository and will be updated as new material is added. Students are encouraged to download and edit the files as they see fit, but solutions should always be attempted first before peeking at the answers!

diagnosticlink: https://goo.gl/forms/cn14kLO6v50vjNSg2

contact: The main point of contact for all questions relating to this course will be <a href="/contact" target="_blank">Alex Mackay</a> (<a href="mailto:MackayA1@cardiff.ac.uk" target="_blank">MackayA1@cardiff.ac.uk</a>). Support will be provided via the Maths Support service which runs 11am-1pm every day during term-time in M/0.37.

semester: 2017/2018

timetable: 13:10-14:00 (M/1.05)

notes: The notes for this course are available on <a href="https://github.com/Scott3142/ugmatlab" target="_blank">github</a> where you will find main.pdf in the docs/ directory. The Matlab program files which relate to the tasks in the notes are included in the programs/ directory. These programs have been tested on Matlab R2016a but should work on all other versions of Matlab. They should also work on GNU Octave, but this is untested.
---

<p>{{ page.hero }}</p>
<br/>

<center>
<a href="{{ page.diagnosticlink }}" target="_blank" class="btn btn-ghost">Initial Questionnaire</a>
<br/><br/>
</center>

<h4>Contact Info:</h4>
<ul>
  <li>{{ page.contact }}</li>
</ul>
<br/>

<h4>Timetable ({{ page.semester }}):</h4>
<ul>
<li><em>{{ page.timetable }}</em></li>
</ul>
<br/>

<h4>Course Notes and Program Files:</h4>
<ul>
  <li>{{ page.notes }}</li>
</ul>
<br/>
<h4>Quick Links:</h4>
<ul>
  {% for link in site.data.ugmatlab.links %}
    <li><a href="{{ link.url }}" target="_blank">{{ link.text }}</a></li>
  {% endfor %}
</ul>
<br/>

<h4>Course Tutors:</h4>
<ul>
  {% for link in site.data.ugmatlab.tutors %}
    <li>{{ link.name }} (<a href="{{ link.url }}">{{ link.text }}</a>)</li>
  {% endfor %}
</ul>

