---
title: "Teaching"
layout: default
permalink: "/teaching"
---

<div class="container">
  <h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>

  <div class="row gap-y listrecent listrecent listauthor">
    <div class="col-lg-12 col-md-12 mb-4">
      <div class="p-4 border rounded">
        <h4 class="text-dark mb-0"> Courses </h4><br>
        <div class="p-4 border rounded vdivide">
          {% for courseitem in site.data.courses.previous %}
            <div class="row vdivide gap-y border rounded">
              <div class="col-md-6 text-center">
                {% if courseitem.url %}
                  <a href="{{ courseitem.url}}">{{ courseitem.title }}</a>
                {% else %}
                  {{ courseitem.title }}
                {% endif %}
              </div>
              <div class="col-md-6 text-center">
                {{ courseitem.institution }}
              </div>
            </div>
          {% endfor %}
        </div>
      </div>
      <div class="p-4 border rounded">
        <h4 class="text-dark mb-0"> Teaching Experience </h4><br>
        <div class="p-4 border rounded vdivide">
          {% for teachingitem in site.data.teaching_experience %}
            <div class="row vdivide gap-y border rounded">
              <div class="col-md-4 text-center">
                {{ teachingitem.title }}
              </div>
              <div class="col-md-4 text-center">
                {{ teachingitem.year }}
              </div>
              <div class="col-md-4 text-center">
                {{ teachingitem.institution }}
              </div>
             </div>
             <div class="row gap-y border rounded">
              <div class="col-md-12 mb-5">
                {{ teachingitem.description }}
              </div>
            </div>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>
</div>
