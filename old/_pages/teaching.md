---
title: Teaching
layout: default
permalink: /teaching/

hero: I have a passion for education and firmly believe that teaching is one of the world's most important professions. I have experience teaching at all levels of education from primary school through to University and I am always interested in novel teaching methods and practises. Additionally I am also a fully qualified Tang Soo Do Karate Instructor, and have over 5 years experience in teaching and coaching martial arts.
---

<p>{{ page.hero }}</p><br>

<p>{{ site.cvlink }}</p>
<br>

<center><h4>Courses</h4><br></center>
<ul>
  <!--<h5>Current</h5><br/>
  <ul>
    {% for currentCourse in site.data.courses.current %}
      <li><center><a href ="{{ currentCourse.url }}" class="btn btn-ghost">{{ currentCourse.title }} | <em>{{ currentCourse.institution }}</em></a></center></li><br/>
    {% endfor %}
  </ul>-->

  <!--<h5>Previous</h5>-->
  <ul>
    {% for previousCourse in site.data.courses.previous %}
      <li>{{ previousCourse.title }} | <em>{{ previousCourse.institution }}</em> {% if previousCourse.url %} | <a href="{{ previousCourse.url }}"><em>Course Page</em></a>{% endif %}</li>
    {% endfor %}
  </ul>
</ul>

<br/><br>

<center><h4>Teaching Experience</h4></center><br>
<ul>
  {% for job in site.data.teaching_experience %}
    <li><b style="font-weight:bold;">{{ job.title }}</b> | <em>{{ job.institution }} {{ job.year }}</em></li>
  <ul><br/>
    <li><em>{{ job.description }}</em></li><br/>
  </ul>
  {% endfor %}
</ul>
