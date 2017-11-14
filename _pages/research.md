---
title: Research
layout: default
permalink: /research/
hero: My research is based primarily in fluid dynamics and in particular hydrodynamic stability theory. I am interested in laminar flow control techniques and have looked at oscillatory flows over rotating disks and flat plates.
---

<p>{{ page.hero }}</p>

<p>{{ site.cvlink }}</p>
<br>

<h4>Projects</h4>
<ul>
  {% for project in site.data.projects %}
    <li>{{ project.title }} | <em>{{ project.institution }} {{ project.year }}</em></li>
  <ul><br/>
    <li>{{ project.description }}</li><br/>
  </ul>
  {% endfor %}
</ul>

<br/>

<h4>Notable Contributions</h4>
<ul>
  {% for contribution in site.data.contributions %}
    <li>{{ contribution.title }} | <em>{{ contribution.institution }} {{ contribution.year }}</em></li>
  <ul><br/>
    <li>{{ contribution.description }}</li><br/>
  </ul>
  {% endfor %}
</ul>

<br/>

<h4>Academic Awards</h4>
<ul style="list-style-type:disc">
  {% for award in site.data.awards %}
    <li>{{ award.title }} | <em>{{ award.institution }} ({{ award.year }})</em></li>
  {% endfor %}
</ul>

<br/>

<h4>Funding Awarded</h4>
<ul>
  {% for fund in site.data.funding %}
    <li>{{ fund.amount }} {{ fund.duration }} | <em>{{ fund.type }} ({{ fund.year }})</em></li><br/>
  {% endfor %}
</ul>

<br/>

<h4>Conferences &amp; Workshops</h4>
<ul>
  <li>Hosted:</li>
  <ul>
    {% for hostedConference in site.data.conferences.hosted %}
      <li>{{ hostedConference.title }} | <em> {{ hostedConference.institution }} ({{ hostedConference.year }})</em> {{ hostedConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Invited Talk:</li>
    <ul>
    {% for talkConference in site.data.conferences.invitedTalk %}
      <li>{{ talkConference.title }} | <em> {{ talkConference.institution }} ({{ talkConference.year }})</em> {{ talkConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Contributed Talk:</li>
    <ul>
    {% for talkConference in site.data.conferences.contributedTalk %}
      <li>{{ talkConference.title }} | <em> {{ talkConference.institution }} ({{ talkConference.year }})</em> {{ talkConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Contributed Poster:</li>
    <ul>
    {% for posterConference in site.data.conferences.contributedPoster %}
      <li>{{ posterConference.title }} | <em> {{ posterConference.institution }} ({{ posterConference.year }})</em> {{ posterConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
  <li>Attended:</li>
    <ul>
    {% for attendedConference in site.data.conferences.attended %}
      <li>{{ attendedConference.title }} | <em> {{ attendedConference.institution }} ({{ attendedConference.year }})</em> {{ attendedConference.extra }}</li>
    {% endfor %}
  </ul>
  <br/>
</ul>

<br/>

<h4>Society Membership</h4>
<ul>
  {% for society in site.data.memberships %}
    <li><a href="{{ society.url }}" target="_blank">{{ society.name }}</a></li>
  {% endfor %}
</ul>
