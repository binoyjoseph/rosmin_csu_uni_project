Summary

## A4 site now has 8 HTML pages + external CSS + external JS:

- index.html — home (introduces me for Verdant Web Solutions Pty Ltd)
- rroy_A4_about.html, rroy_A4_resume.html — carried over from A3, nav fixed
- 4 skill pages (matches the brief — one is Web Dev):
    - rroy_A4_web_skills.html — the "Javascriptpage" with the link that opens the form in a new tab
    - rroy_A4_communication.html, rroy_A4_problem_solving.html, rroy_A4_teamwork.html — new
- rroy_A4_newsletter.html — HTML5 signup form (post method, onload alert, onsubmit validation, all 5 radios, all 5 checkboxes, 60-col textarea, submit + reset)
- js/newsletter.js — external (for reusability/readability marks): showWelcomeAlert() + validateSignupForm()
- css/portfolio.css — extended with universal selector, pure-CSS form styling, print overrides
- README.md — requirement-to-implementation table and a testing plan you can paste into the design doc

## Two things worth flagging:

1. I picked Verdant Web Solutions Pty Ltd as the fictitious company (matches the existing olive/green theme). If A2 used a different company name, swap it in the four spots that mention it (home page intro, three skill-page headings, form welcome string, form footer, README).
2. The form's action points at https://httpbin.org/post as a safe public echo endpoint so you can demonstrate it actually submits. Replace with your hosting URL if needed.