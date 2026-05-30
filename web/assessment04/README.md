# ITC293 - Assessment 4 (Rosmin Roy)

Electronic work portfolio for the fictitious employer **Verdant Web Solutions Pty Ltd**.
Builds on Assessment 3 by adding three additional skill pages, an HTML5 newsletter
signup form (HTML + pure CSS + external JavaScript), and updated navigation.

## File / folder layout

```
assessment04/
├── index.html                      Home page (introduces me to employers)
├── rroy_A4_about.html              About page
├── rroy_A4_resume.html             Resume page (table of units, work, certifications)
├── rroy_A4_web_skills.html         Web Development skill page (the "Javascriptpage")
├── rroy_A4_communication.html      Communication skill page
├── rroy_A4_problem_solving.html    Problem Solving skill page
├── rroy_A4_teamwork.html           Teamwork skill page
├── rroy_A4_newsletter.html         Newsletter signup form for Verdant Web Solutions
├── css/portfolio.css               Single external stylesheet (no inline/internal CSS)
├── js/newsletter.js                External JS - onload alert + onsubmit validation
└── images/                         profile.png, certificate.png, work.png
```

That is **8 HTML pages** in total (well above the 6-page minimum), with 4 skill
pages, one of which is the Web Development skills page that links to the form.

## A4 form requirements - where each one lives

| # | Requirement | Where it's implemented |
|---|---|---|
| 1 | Form styled by pure CSS | `css/portfolio.css` (form#signupForm block, no inline CSS) |
| 2 | Form opens in a new window/tab from the Javascriptpage | `rroy_A4_web_skills.html` link with `target="_blank"` |
| 3 | Submitted using POST method | `<form method="post" action="...">` in `rroy_A4_newsletter.html` |
| 4 | Welcome alert on page load | `<body onload="showWelcomeAlert();">` calling `js/newsletter.js` |
| 5 | Instructive information ("required data" etc.) | Intro paragraph + red `*` markers on required fields |
| 6 | Text box max size 60 - First Name | `<input type="text" maxlength="60" ...>` |
| 7 | Text box max size 60 - Last Name | `<input type="text" maxlength="60" ...>` |
| 8 | Email box max size 60 | `<input type="email" maxlength="60" ...>` |
| 9 | 5 radio buttons for age ranges 15-25, 26-35, 36-45, 46-55, 55+ | `<fieldset>` "Age Range" |
| 10 | 5 checkboxes for company services | Web Dev, UX/UI, E-commerce, SEO, Cloud Hosting |
| 11 | Text area min 60 cols x 3 rows | `<textarea cols="60" rows="3">` |
| 12 | Submit + Reset buttons | `.form-buttons` paragraph at end of form |
| 13 | onsubmit validates both name fields are non-empty, alerts, prevents submit | `validateSignupForm(form)` in `js/newsletter.js`; called via `onsubmit="return validateSignupForm(this);"` |
| 14 | Plenty of code comments | See top-of-file comment blocks and inline notes in every file |

## Changes since Assessment 3

- Renamed page links across the site from `rroy_A3_*` to `rroy_A4_*`.
- Added the fictitious-company context (**Verdant Web Solutions Pty Ltd**) to the home page.
- Added 3 new skill pages: Communication, Problem Solving, Teamwork (each with concrete
  examples linking the skill back to a real-world experience).
- Rewrote the Web Skills page to include a JavaScript section and a call-to-action link
  that opens the new signup form in a new browser tab.
- Added `rroy_A4_newsletter.html` - HTML5 signup form for the fictitious company.
- Added `js/newsletter.js` - external JS for the welcome alert and submit-time validation.
  Kept external (not inline) so the same script could be reused by another signup page.
- Extended `css/portfolio.css` with: a universal selector (`*`), styling for the form
  (`fieldset`, `legend`, buttons, inputs), an inline `code` style, and a print-friendly
  override for the form. No inline or internal CSS anywhere in the site.

## Carried over from Assessments 2 + 3

- Single external CSS file (no internal or inline styles).
- CSS-button navigation bar present on every page.
- Print stylesheet (try Ctrl+P / Cmd+P): hides navigation, removes background colours,
  uses a larger font in `pt`.
- Logo / favicon (`images/profile.png`) on every page tab.
- Footer with contact details and copyright permission notice.
- Resume page has a 5-row x 3-column table of current units.

## Testing plan (suggested - to be expanded in the design doc)

1. Open `index.html` in Chrome at 1024 x 768 - verify no horizontal scroll bar.
2. Click each link in the nav bar - all 7 destinations should load.
3. On `rroy_A4_web_skills.html`, click "Open the Newsletter Signup Form" - it should
   open in a new tab. The page should show an alert with the welcome message.
4. Click **Sign Me Up** with both name fields empty - expect an alert and no submission.
5. Fill First Name only, click submit - expect an alert about Last Name and no submission.
6. Fill both names, click submit - expect the thank-you alert and the form to post.
7. Click **Clear Form** - all fields should reset.
8. On every page press Ctrl+P - the preview should hide the nav and use plain colours.
9. Validate each .html file with the W3C HTML5 validator and `portfolio.css` with the
   W3C CSS validator.
