---

title: Lesson 3 - Research
layout: default
permalink: /hnc/lessons/3/
    
slideslink: https://docs.google.com/presentation/d/1UPt0cRnm5NshuwtLi9AeEEDXJG912MFtGygqC8piVAg/export/pdf
fileslink: /assets/hnc/3.zip

resourcetitle: Lesson Resources
resource: |
  <li>The following files will help you with this class:</li>
  <br/>
  <ul>
    <li><center><a href="/assets/hnc/3/3.docx" target="_blank" class="btn btn-ghost">Download Documents</a></center></li>
  </ul>
  <br/>
  <li>This class is centered around <em>research</em>. Your assignment will be set next week, and will be based around explaining to a group of junior software engineers the features and functions of a website. Start to think about what you will tell them. Below is a list of a few things to consider:</li>
  <br/>
  <ul style="list-style-type:disc;">
    <h6>Server Technologies:</h6> 
    <li>How does a server host a site? What are the costings involved?</li>
    <li>Is there a restriction on file sizes/upload speed/access speeds for different servers? Will you get more if you pay more, or would something like Github be sufficient?</li>
    <br/>
    <h6>Website Creation Techniques:</h6> 
    <li>What tools and software are used to develop websites? Look at some existing sites. Can you figure out how they’re written and maintained?</li>
    <li>How heavily would the techniques used depend on the business? How much does a site cost? And what different types of site can you have?</li>
    <br/>
    <h6>Front-end and Back-end:</h6> 
    <li>Research the terms ‘front-end’ and ‘back-end’. Which part of the website do each of these groups of people maintain?</li>
    <br/>
    <h6>Databases:</h6>
    <li>What are databases used for? How are they managed?</li>
    <br/>
    <h6>Security:</h6>
    <li> How is security performed on a website? If there is a password field, how is this handled so that your data is secure?</li>
    <ul>
      <li><em>NB: This is not easy. Don’t be worried if you don’t understand what you read - it’s complicated for a reason!!</em></li>
    </ul>
    <br/>
    <h6>Maintenance:</h6>
    <li>How is a website maintained? How do you upload files to a website?</li>
    <br/>
    <h6>Content Management System:</h6>
    <li>Find out what a Content Management System is and why it’s useful. We will cover this in a whole class, but it would be useful for you to get ahead before we do!</li>
    <br/>
    <h6>Other Features:</h6>
    <li>Are there any other interesting features of a website which are not mentioned here? List and discuss them here.</li>
  </ul>
  
quicklinks: |
  <h4>Quick Links:</h4>
  <ul>
    <li>BTEC Higher Nationals - Computing | <a href="/hnc">Homepage</a> | <a href="/hnc/lessons/0/">Lesson 0 - Introduction</a></li>
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
<ul style="list-style-type:disc;">
  {{ page.resource }}
</ul>
<br/>

{{ page.quicklinks }}

<br/>
