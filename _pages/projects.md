---
title: "Projects"
layout: default
permalink: "/projects"
---

<div class="container">
<h4 class="font-weight-bold spanborder"><span>{{page.title}}</span></h4>
  <div class="row gap-y listrecent listrecent listauthor">
    {% for projectlink in site.data.projects %}

      <style> #more{{ forloop.index }} { display:none; }</style>

      <div class="col-lg-6 col-md-6 mb-4">
        <div class="p-4 border rounded">
          <div class="row">
            <div class="col-md-3 mb-4 mb-md-0"><a href="{{ projectlink.url }}"><img href="{{ projectlink.url }}" alt="{{ projectlink.title }}" src="{{ projectlink.image }}" class="rounded-circle" height="80" width="80"></a></div>
            <div class="col-md-9">
              <a href="{{ projectlink.url }}" {% if projectlink.url contains 'http' %} target="blank" {% endif %}>
                <h4 class="text-dark mb-0"> {{ projectlink.title }} </h4>  
                <div class="excerpt mb-2" id="less{{ forloop.index }}">
                  {{ projectlink.description | slice: 0, 100 }}...                  
                </div>                
                <div class="excerpt mb-2" id="more{{ forloop.index }}">
                  {{ projectlink.description }}                  
                </div>              
              </a>
              <a href="#" onclick="readMore{{ forloop.index }}()" id="readMoreLink{{ forloop.index }}">Read more...</a>              
            </div>
          </div>
        </div>
      </div>

      <script>
        function readMore{{ forloop.index }}() {
          var moreText = document.getElementById("more{{ forloop.index }}");
          var lessText = document.getElementById("less{{ forloop.index }}");
          var linkText = document.getElementById("readMoreLink{{ forloop.index }}");

          if (linkText.innerHTML === "Read more...") {
            linkText.innerHTML = "Read less...";
            moreText.style.display = "block";
            lessText.style.display = "none";
          } else {
            linkText.innerHTML = "Read more...";
            moreText.style.display = "none";
            lessText.style.display = "block";
          }
        }
      </script>

    {% endfor %}

  </div>

  <style> #iconHidden { display:none; }</style>

  <div>
    <a href="#iconHidden" onclick="readMoreIconCredit()" id="iconVisible">Icon credit...</a>
    <span id="iconHidden">
      Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>, licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="blank">CC 3.0 BY</a>
    </span>
  </div>

  <script>
    function readMoreIconCredit() {
      var moreText = document.getElementById("iconHidden");
      var lessText = document.getElementById("iconVisible");

      moreText.style.display = "block";
      lessText.style.display = "none";
    }
  </script>

</div>
