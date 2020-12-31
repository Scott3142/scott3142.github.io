---
title: "Career"
layout: default
permalink: "/career"
---

<div class="container">
  <h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>

  <div class="row gap-y listrecent listrecent listauthor">
      <div class="col-lg-12 col-md-12 mb-4">
        <div class="p-4 border rounded row">
          <div class="col-md-2 col-sm-3 mb-4 mb-md-0"><a href="{{ projectlink.url }}"><img href="#" alt="Bridgend College Logo" src="/assets/images/bclogo-circle.png" class="rounded-circle" height="80" width="80"></a></div>
          <div class="col-md-6 col-sm-6 mb-4 mb-md-0"><h4 class="text-dark mb-0 pt-4"> Bridgend College </h4><br></div>
          <div class="col-md-12 border rounded d-inline-block mt-1 mb-3 pt-2 pb-2 font-weight-normal">
            Curriculum Manager (IT) (2021 - Present)<br>
            Digital Lead (2018 - Present)<br>
            Lecturer (2016 - 2018)<br>
          </div>
          <div class="p-4 border rounded vdivide">
            <h5 class="text-dark">Publications</h5><br>
            {% for pubsitem in site.data.publications.bc %}
              <div class="row vdivide gap-y border rounded">
                <div class="col-md-12">
                {{ pubsitem.authors }}, {{ pubsitem.title }} ({{ pubsitem.year }}) | <em>{{ pubsitem.journal }}</em> {% if pubsitem.url %} | <a href="{{ pubsitem.url }}" target="blank">{{ pubsitem.url }}</a>{% endif %}
                </div>
              </div>
            {% endfor %}
          </div>
          <div class="p-4 border rounded vdivide">
            <h5 class="text-dark">Awards &amp; Achievements</h5><br>
            {% for awarditem in site.data.awards.bc %}
              <div class="row vdivide gap-y border rounded">
                <div class="col-md-4 text-center">
                  {{ awarditem.title }}
                </div>
                <div class="col-md-4 text-center">
                  {{ awarditem.year }}
                </div>
                <div class="col-md-4 text-center">
                  {{ awarditem.institution }}
                </div>
              </div>
            {% endfor %}
          </div>
          <div class="p-4 border rounded vdivide">
            <h5 class="text-dark">Conferences &amp; Workshops</h5><br>
            {% for conferenceitem in site.data.conferences.bc %}
              <div class="row vdivide gap-y border rounded">
                <div class="col-md-4 text-center">
                  {{ conferenceitem.title }}
                </div>
                <div class="col-md-4 text-center">
                  {{ conferenceitem.institution }}
                </div>
                <div class="col-md-4 text-center">
                  {{ conferenceitem.year }}
                </div>
              </div>
            {% endfor %}
          </div>
        </div>
      </div>
  </div>

  <div class="row gap-y listrecent listrecent listauthor">
      <div class="col-lg-12 col-md-12 mb-4">
        <div class="p-4 border rounded row">
          <div class="col-md-2 col-sm-3 mb-4 mb-md-0"><a href="{{ projectlink.url }}"><img href="#" alt="Cardiff University Logo" src="/assets/images/culogo.png" class="rounded-circle" height="80" width="80"></a></div>
          <div class="col-md-6 sol-sm-6 mb-4 mb-md-0"><h4 class="text-dark mb-0 pt-4"> Cardiff University </h4><br></div>
          <div class="col-md-12 border rounded d-inline-block mt-1 mb-3 pt-2 pb-2 font-weight-normal">
            Associate Lecturer (2018)<br>
            STEM Engagement Officer (2018)<br>
            PhD Student (2014 - 2018)<br>
            Masters Student (2013 - 2014)<br>
            Undergraduate Student (2010 - 2013)                
          </div>
          <div class="p-4 border rounded vdivide">
            <h5 class="text-dark">Publications</h5><br>
            {% for pubsitem in site.data.publications.cu %}
              <div class="row vdivide gap-y border rounded">
                <div class="col-md-12">
                {{ pubsitem.authors }}, {{ pubsitem.title }} ({{ pubsitem.year }}) | <em>{{ pubsitem.journal }}</em> {% if pubsitem.url %} | <a href="{{ pubsitem.url }}" target="blank">{{ pubsitem.url }}</a>{% endif %}
                </div>
              </div>
            {% endfor %}
          </div>

          <div class="p-4 border rounded">
            <h5 class="text-dark">Awards &amp; Achievements</h5><br>
            {% for awarditem in site.data.awards.cu %}
              <div class="row vdivide gap-y border rounded">
                <div class="col-md-4 text-center">
                  {{ awarditem.title }}
                </div>
                <div class="col-md-4 text-center">
                  {{ awarditem.year }}
                </div>
                <div class="col-md-4 text-center">
                  {{ awarditem.institution }}
                </div>
              </div>
            {% endfor %}
          </div>
          <div class="p-4 border rounded">
            <h5 class="text-dark">Funding</h5><br>
            {% for fundingitem in site.data.funding.cu %}
              <div class="row vdivide gap-y border rounded">
                <div class="col-md-4 text-center">
                  {{ fundingitem.title }}
                </div>
                <div class="col-md-4 text-center">
                  {{ fundingitem.value }}
                </div>
                <div class="col-md-4 text-center">
                  {{ fundingitem.year }}
                </div>
              </div>
            {% endfor %}
          </div>
          <div class="p-4 border rounded">
            <h5 class="text-dark">Conferences</h5><br>
            {% for conferenceitem in site.data.conferences.cu %}
              <div class="row vdivide gap-y border rounded">
                <div class="col-md-4 text-center">
                  {{ conferenceitem.title }}
                </div>
                <div class="col-md-4 text-center">
                  {{ conferenceitem.institution }}
                </div>
                <div class="col-md-4 text-center">
                  {{ conferenceitem.year }}
                </div>
              </div>
            {% endfor %}

          </div>
        </div>
      </div>
  </div>

</div>
