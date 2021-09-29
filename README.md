# DashboardsPlay

Lines 1 to 4 import the required libraries.
Each library provides a building block for yout applircation:
- dash helps you initialise your application
- dash_core_components allows you to create interactive components like graphs, dropdowns, or date ranges
- dash_html_components lets you access HTML tags
- pandas helps you read and organise the data

lines 6 to 9 read the data and preprocess it for use in the dashboard. 
You filter some of the data becasue the current version of your dashboard isn't intereactive, and the plotted values
wouldn't make sense otherwise.

line 11 creates an instance of the Dash class.

lines 13 to 46 define the layout properties of the app object. This property determines the looks of your application 
using tree structure made of Dash components.
Dash components come prepackaged in Python libraries. Some of them come with Dash when you install it. The rest you 
have to install separately.
You'll see two sets of components in almost every app.

1. Dash HTML Components - provide you with Python wrappers for HTML elements. For example, you could use this library
to create elements such as paragraphs, headings, or lists
   
2. Dash Core Components provides you with Python abstractions for creating interactive user interfaces. You can use it 
   to create interactive elements such as graphs, sliders or dropdowns. 
   
On lines 13 - 20 you can see the Dash HTML components in practice. You start by defining the parent component, an 
html.Div. Then you add two more elements, a heading (html.H1) and a paragraph (html.P), as its children.

the part of the layout shown on lines 13-20 will get transformed into the following HTML code:
<div>
  <h1>Avocado Analytics</h1>
  <p>
    Analyze the behavior of avocado prices and the number
    of avocados sold in the US between 2015 and 2018
  </p>
  <!-- Rest of the app -->
</div>

On lines 21 to 24 in the layout code snippet, you can see the graph component from Dash Core Components in practice. 
There are two dcc.Graph components in the app.layout. The first one plots the average prices of avocados during the 
period of study, and the second plots the number of avocados sold in the United States during the same period.

lines 48 & 49 make it possible to run your Dash application locally using Flask's built-in server. 
The debug=True parameter from app.run_server enables the hot-reloading option in your application. This means that when 
you make a change to your app, it reloads automatically, without you having to restart the server.

run the code like you normally would and you will get a webadress to open in your preferred browser. 