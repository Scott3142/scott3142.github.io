---
title: "Career"
layout: default
permalink: "/career"
---

<div class="container">
  <h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>

  <div class="row gap-y listrecent listrecent listauthor">
      <div class="col-lg-12 col-md-12 mb-4">
        <div class="p-4 border rounded">
          <h4 class="text-dark mb-0"> Bridgend College </h4>
          <div class="d-inline-block mt-1 mb-3 font-weight-normal">2018 - Present</div>
            <div class="p-4 border rounded vdivide">
              <h5 class="text-dark">Publications</h5>
              {% for pubsitem in site.data.bc-publications %}
                <div class="row vdivide">
                  <div class="col-md-4 text-center">
                    {{ pubsitem.title }}
                  </div>
                  <div class="col-md-4 text-center">
                    {{ pubsitem.year }}
                  </div>
                  <div class="col-md-4 text-center">
                    {{ pubsitem.url }}
                  </div>
                </div>
              {% endfor %}
            </div>
        </div>
      </div>
  </div>

  <div class="row gap-y listrecent listrecent listauthor">
      <div class="col-lg-12 col-md-12 mb-4">
        <div class="p-4 border rounded">
          <h4 class="text-dark mb-0"> Cardiff University </h4>
          <div class="d-inline-block mt-1 mb-3 font-weight-normal">2010 - 2018</div>
            <div class="p-4 border rounded">
              <h5 class="text-dark">Awards &amp; Achievements</h5>
              {% for awarditem in site.data.cu-awards %}
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
              <h5 class="text-dark">Funding</h5>
              {% for fundingitem in site.data.cu-funding %}
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
              <h5 class="text-dark">Conferences</h5>
              <h6 class="text-dark">Organised</h6>
              {% for conferenceitem in site.data.cu-conferences.organised %}
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
              <h6 class="text-dark">Invited Talk</h6>
              {% for conferenceitem in site.data.cu-conferences.invitedTalk %}
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
                            <h6 class="text-dark">Contributed Talk</h6>
              {% for conferenceitem in site.data.cu-conferences.contributedTalk %}
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
                            <h6 class="text-dark">Contributed Poster</h6>
              {% for conferenceitem in site.data.cu-conferences.contributedPoster %}
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
                            <h6 class="text-dark">Attended</h6>
              {% for conferenceitem in site.data.cu-conferences.attended %}
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
