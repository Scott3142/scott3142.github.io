---

title: Lesson 3 - Research
layout: default
permalink: /btec/lessons/3/
    
slideslink: https://docs.google.com/presentation/d/1Gdyd04QrqJsIralBOpXm2n9aO6rqL-b95p5grqqIiQU/export/pdf
fileslink: /assets/btec/3.zip

resourcetitle: Lesson Resources
resource: |
  <li>The following files will help you with this class:</li>
  <br/>
  <ul>
    <li><center><a href="/assets/btec/3/3.docx" target="_blank" class="btn btn-ghost">Download Documents</a></center></li>
  </ul>
  <br/>
  <li>This class is centered around <em>research</em>. Your assignment will be set next week, and will be based around explaining to a group of small business leaders why they should hire you to create an app for their business. Start to think about what you will tell them. Below is a list of a few things to consider:</li>
  <br/>
  <ul style="list-style-type:disc;">
    <h6>Costing:</h6> 
    <li>What are the financial constraints of your client's business? How will you, the developer, make money as well?</li>
    <br/>
    <h6>Time:</h6> 
    <li>How long will your app take to develop? Does your client have a time limit?</li>
    <br/>
    <h6>Benefits to the Client:</h6> 
    <li>Why does your client need this? What if the business were a local plumber or a local sports club? How would the business benefit from your application?</li>
    <br/>
    <h6>Audience:</h6>
    <li>Who is your audience? Who will you be catering your app towards? Will it be for children or adults, tech-savvy or not?</li>
    <br/>
    <h6>Software & Hardware:</h6>
    <li>Which software will you use to create your app? How will you develop and test it? What are your hardware requirements? Does your app need <em>hosting</em> services? Is there an ongoing cost for this?</li>
    <br/>
    <h6>Platform:</h6>
    <li>Which platform will your application run on? Will it have to run on a web browser as well as a phone/tablet? Will it have an Alexa/Google Home skill attached to it?</li>
    <br/>
    <h6>Content Management System:</h6>
    <li>Your app <em>must</em> make use of a CMS. Decide which one you are likely to use. Think about usability and ease of use for your client. The idea is for the client to <em>maintain the app themselves after you have developed it!!</em> Therefore, you should choose a CMS which is easy to use and has lots of features.</li>
    <br/>
    <h6>Other Features:</h6>
    <li>Are there any other features your website will need which are not mentioned here? List them and discuss them in your document.</li>
    <br/>
  </ul>

quicklinks: |
  <h4>Quick Links:</h4>
  <ul>
    <li>BTEC Firsts | <a href="/btec/">Homepage</a> | <a href="/btec/lessons/0/">Lesson 0 - Introduction</a></li>
    <li><a href="/contact">Contact Me</a></li>
  </ul> 

---

{% for block in site.data.common_lessons %}
  {% if block.common == 'yes' %}
  <h4 id="{{ block.idtag }}">{{ block.blockname }}:</h4>
  <ul>
    {{ block.blocktext | replace: 'slidesurl', page.slideslink | replace: 'filesurl', page.fileslink }}
  </ul>
  <br/>
  {% endif %}
{% endfor %}

<h4>{{ page.resourcetitle }}:</h4>
<ul>
  {{ page.resource }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
